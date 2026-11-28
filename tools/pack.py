#!/usr/bin/env python3
"""Reproducible resource unpacker, packer, and verifier for FaceOff.

Manages the chunked base64/deflate-raw asset packs (`assets/pack-NN.js`),
keeps `assets/boot.js` (`TOTAL`) and `index.html` script tags synchronized,
and verifies bundle integrity and deterministic packaging in CI.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

PACK_PREFIX = "(window.__FO_B=window.__FO_B||[]).push("
PACK_SUFFIX = ");"
DEFAULT_PACK_COUNT = 3
COMPRESS_RATIO_THRESHOLD = 0.98

MIME_BY_EXT = {
    ".js": "text/javascript",
    ".mjs": "text/javascript",
    ".json": "application/json",
    ".glb": "model/gltf-binary",
    ".gltf": "model/gltf+json",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
    ".mp3": "audio/mpeg",
    ".ogg": "audio/ogg",
    ".wav": "audio/wav",
    ".woff2": "font/woff2",
    ".woff": "font/woff",
    ".css": "text/css",
    ".txt": "text/plain",
}

TOTAL_RE = re.compile(r"(\bTOTAL\s*=\s*)(\d+)")
PACK_SCRIPT_RE = re.compile(r'<script\b[^>]*\bsrc="(assets/pack-\d+\.js)"[^>]*></script>')


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def guess_mime(rel_path: str) -> str:
    ext = Path(rel_path).suffix.lower()
    return MIME_BY_EXT.get(ext, "application/octet-stream")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def deflate_raw(data: bytes) -> bytes:
    comp = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=-zlib.MAX_WBITS)
    return comp.compress(data) + comp.flush()


def inflate_raw(data: bytes) -> bytes:
    return zlib.decompress(data, -zlib.MAX_WBITS)


def parse_pack_file(pack_path: Path) -> list[list]:
    raw_text = pack_path.read_text(encoding="utf-8").strip()
    if not raw_text.startswith(PACK_PREFIX) or not raw_text.endswith(PACK_SUFFIX):
        raise ValueError(f"Unexpected pack wrapper format in {pack_path}")
    inner = raw_text[len(PACK_PREFIX) : -len(PACK_SUFFIX)]
    entries = json.loads("[" + inner + "]")
    if not isinstance(entries, list):
        raise ValueError(f"Pack payload is not a list in {pack_path}")
    return entries


def list_pack_files(assets_dir: Path) -> list[Path]:
    return sorted(assets_dir.glob("pack-*.js"))


def read_all_packs(assets_dir: Path) -> tuple[list[Path], list[dict]]:
    pack_files = list_pack_files(assets_dir)
    if not pack_files:
        raise FileNotFoundError(f"No pack-*.js files found in {assets_dir}")

    records: list[dict] = []
    seen_paths: set[str] = set()
    for pack_path in pack_files:
        entries = parse_pack_file(pack_path)
        for idx, item in enumerate(entries):
            if not isinstance(item, list) or len(item) != 5:
                raise ValueError(f"Invalid entry #{idx} in {pack_path.name}")
            rel_path, mime, z_flag, raw_n, b64_str = item
            if not isinstance(rel_path, str) or not rel_path.startswith("assets/"):
                raise ValueError(f"Invalid asset path {rel_path!r} in {pack_path.name}")
            if rel_path in seen_paths:
                raise ValueError(f"Duplicate asset path {rel_path!r} across packs")
            seen_paths.add(rel_path)
            if z_flag not in (0, 1):
                raise ValueError(f"Invalid compression flag {z_flag!r} for {rel_path}")
            if not isinstance(raw_n, int) or raw_n < 0:
                raise ValueError(f"Invalid raw size {raw_n!r} for {rel_path}")

            payload = base64.b64decode(b64_str, validate=True)
            data = inflate_raw(payload) if z_flag == 1 else payload
            if len(data) != raw_n:
                raise ValueError(
                    f"Decoded byte length mismatch for {rel_path}: "
                    f"expected {raw_n}, got {len(data)}"
                )
            records.append(
                {
                    "pack": pack_path.name,
                    "path": rel_path,
                    "mime": mime,
                    "z": z_flag,
                    "raw_n": raw_n,
                    "b64_len": len(b64_str),
                    "sha256": sha256_bytes(data),
                    "data": data,
                }
            )
    return pack_files, records


def sync_boot_total(boot_path: Path, total_raw: int) -> bool:
    text = boot_path.read_text(encoding="utf-8")
    m = TOTAL_RE.search(text)
    if not m:
        raise ValueError(f"Could not locate TOTAL assignment in {boot_path}")
    current = int(m.group(2))
    if current == total_raw:
        return False
    updated = TOTAL_RE.sub(lambda match: f"{match.group(1)}{total_raw}", text, count=1)
    boot_path.write_text(updated, encoding="utf-8")
    return True


def read_boot_total(boot_path: Path) -> int:
    text = boot_path.read_text(encoding="utf-8")
    m = TOTAL_RE.search(text)
    if not m:
        raise ValueError(f"Could not locate TOTAL assignment in {boot_path}")
    return int(m.group(2))


def sync_index_packs(index_path: Path, pack_names: list[str]) -> bool:
    text = index_path.read_text(encoding="utf-8")
    matches = list(PACK_SCRIPT_RE.finditer(text))
    if not matches:
        raise ValueError(f"Could not locate pack script tags in {index_path}")
    existing = [m.group(1) for m in matches]
    target = [f"assets/{name}" for name in pack_names]
    all_deferred = all("defer" in m.group(0) for m in matches)
    if existing == target and all_deferred:
        return False
    block_start = matches[0].start()
    block_end = matches[-1].end()
    replacement = "\n".join(f'<script defer src="{src}"></script>' for src in target)
    updated = text[:block_start] + replacement + text[block_end:]
    index_path.write_text(updated, encoding="utf-8")
    return True


def read_index_packs(index_path: Path) -> list[str]:
    text = index_path.read_text(encoding="utf-8")
    return PACK_SCRIPT_RE.findall(text)


def read_index_packs_deferred(index_path: Path) -> bool:
    text = index_path.read_text(encoding="utf-8")
    matches = list(PACK_SCRIPT_RE.finditer(text))
    return bool(matches) and all("defer" in m.group(0) for m in matches)


def encode_asset(rel_path: str, data: bytes) -> list:
    mime = guess_mime(rel_path)
    raw_n = len(data)
    compressed = deflate_raw(data)
    if raw_n > 0 and len(compressed) < int(raw_n * COMPRESS_RATIO_THRESHOLD):
        z_flag = 1
        payload = compressed
    else:
        z_flag = 0
        payload = data
    b64_str = base64.b64encode(payload).decode("ascii")
    return [rel_path, mime, z_flag, raw_n, b64_str]


def partition_entries(encoded_entries: list[list], pack_count: int) -> list[list[list]]:
    if pack_count < 1:
        raise ValueError("pack_count must be >= 1")
    buckets: list[list[list]] = [[] for _ in range(pack_count)]
    weights = [0] * pack_count

    # Keep assets/game.js in pack-00.js for fast initial extraction.
    game_entries = [e for e in encoded_entries if e[0] == "assets/game.js"]
    other_entries = [e for e in encoded_entries if e[0] != "assets/game.js"]

    for entry in game_entries:
        buckets[0].append(entry)
        weights[0] += len(entry[4])

    # Deterministic LPT bin packing by encoded size, breaking ties by path.
    other_entries.sort(key=lambda e: (-len(e[4]), e[0]))
    for entry in other_entries:
        target_idx = min(range(pack_count), key=lambda i: (weights[i], i))
        buckets[target_idx].append(entry)
        weights[target_idx] += len(entry[4])

    # Sort entries deterministically inside each bucket (game.js first if present).
    for bucket in buckets:
        bucket.sort(key=lambda e: (0 if e[0] == "assets/game.js" else 1, e[0]))

    return buckets


def write_packs(
    src_dir: Path,
    assets_out_dir: Path,
    pack_count: int = DEFAULT_PACK_COUNT,
) -> tuple[list[Path], int, int]:
    assets_src = src_dir / "assets"
    if not assets_src.is_dir():
        raise FileNotFoundError(f"Expected assets/ directory inside {src_dir}")

    asset_files: list[tuple[str, Path]] = []
    for root, dirs, files in os.walk(assets_src):
        dirs.sort()
        for fname in sorted(files):
            if fname.startswith(".") or fname == "pack-manifest.json":
                continue
            full_path = Path(root) / fname
            rel_path = full_path.relative_to(src_dir).as_posix()
            if re.match(r"^assets/pack-\d+\.js$", rel_path) or rel_path == "assets/boot.js":
                continue
            asset_files.append((rel_path, full_path))

    if not asset_files:
        raise ValueError(f"No asset files found under {assets_src}")

    asset_files.sort(key=lambda pair: pair[0])
    encoded_entries = [encode_asset(rel, fp.read_bytes()) for rel, fp in asset_files]
    total_raw = sum(e[3] for e in encoded_entries)

    buckets = partition_entries(encoded_entries, pack_count)
    assets_out_dir.mkdir(parents=True, exist_ok=True)

    # Remove stale pack files if pack_count shrank.
    expected_names = {f"pack-{i:02d}.js" for i in range(pack_count)}
    for old_pack in assets_out_dir.glob("pack-*.js"):
        if old_pack.name not in expected_names:
            old_pack.unlink()

    written_packs: list[Path] = []
    total_pack_bytes = 0
    for idx, bucket in enumerate(buckets):
        pack_path = assets_out_dir / f"pack-{idx:02d}.js"
        encoded_items = ",".join(
            json.dumps(item, separators=(",", ":"), ensure_ascii=True)
            for item in bucket
        )
        content = f"{PACK_PREFIX}{encoded_items}{PACK_SUFFIX}\n"
        pack_path.write_text(content, encoding="utf-8")
        written_packs.append(pack_path)
        total_pack_bytes += len(content.encode("utf-8"))

    return written_packs, total_raw, total_pack_bytes


def cmd_unpack(args: argparse.Namespace) -> int:
    root = repo_root()
    assets_dir = Path(args.assets_dir) if args.assets_dir else root / "assets"
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    pack_files, records = read_all_packs(assets_dir)
    manifest_entries = []
    for rec in records:
        dest = out_dir / rec["path"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(rec["data"])
        manifest_entries.append(
            {
                "path": rec["path"],
                "pack": rec["pack"],
                "mime": rec["mime"],
                "z": rec["z"],
                "raw_n": rec["raw_n"],
                "sha256": rec["sha256"],
            }
        )

    manifest = {
        "packs": [p.name for p in pack_files],
        "count": len(records),
        "total_raw_bytes": sum(r["raw_n"] for r in records),
        "entries": manifest_entries,
    }
    manifest_path = out_dir / "pack-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(
        f"Unpacked {len(records)} assets ({manifest['total_raw_bytes']:,d} raw bytes) "
        f"from {len(pack_files)} packs into {out_dir}"
    )
    return 0


def cmd_pack(args: argparse.Namespace) -> int:
    root = repo_root()
    src_dir = Path(args.src).resolve()
    assets_dir = Path(args.assets_dir) if args.assets_dir else root / "assets"
    boot_path = Path(args.boot) if args.boot else assets_dir / "boot.js"
    index_path = Path(args.index) if args.index else root / "index.html"

    written_packs, total_raw, total_pack_bytes = write_packs(
        src_dir=src_dir,
        assets_out_dir=assets_dir,
        pack_count=args.packs,
    )

    boot_changed = False
    if args.sync_boot and boot_path.is_file():
        boot_changed = sync_boot_total(boot_path, total_raw)

    index_changed = False
    if args.sync_index and index_path.is_file():
        index_changed = sync_index_packs(index_path, [p.name for p in written_packs])

    print(
        f"Packed {len(written_packs)} pack files ({total_pack_bytes:,d} packed bytes, "
        f"{total_raw:,d} raw bytes)"
    )
    for p in written_packs:
        digest = sha256_bytes(p.read_bytes())[:12]
        print(f"  {p.name}: {p.stat().st_size:,d} bytes (sha256:{digest})")
    if boot_changed:
        print(f"Synced {boot_path.name}: TOTAL = {total_raw}")
    if index_changed:
        print(f"Synced {index_path.name} script tags")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    root = repo_root()
    assets_dir = Path(args.assets_dir) if args.assets_dir else root / "assets"
    boot_path = Path(args.boot) if args.boot else assets_dir / "boot.js"
    index_path = Path(args.index) if args.index else root / "index.html"

    pack_files, records = read_all_packs(assets_dir)
    by_path = {r["path"]: r for r in records}
    total_raw = sum(r["raw_n"] for r in records)

    # 1. Verify required core files.
    for required in ("assets/game.js", "assets/maps/index.json"):
        if required not in by_path:
            raise ValueError(f"Missing required asset in packs: {required}")

    # 2. Verify all maps declared in assets/maps/index.json exist in packs.
    maps_index = json.loads(by_path["assets/maps/index.json"]["data"].decode("utf-8"))
    for entry in maps_index.get("maps", []):
        for key in ("json", "glb", "thumb"):
            val = entry.get(key)
            if isinstance(val, str) and val.startswith("assets/"):
                if val not in by_path:
                    raise ValueError(
                        f"Map {entry.get('id', '?')} references missing asset: {val}"
                    )

    # 3. Verify boot.js TOTAL matches sum of raw bytes.
    boot_total = read_boot_total(boot_path)
    if boot_total != total_raw:
        raise ValueError(
            f"assets/boot.js TOTAL mismatch: boot.js has {boot_total}, "
            f"packs sum to {total_raw}"
        )

    # 4. Verify index.html script tags match pack files on disk and retain defer.
    disk_packs = [f"assets/{p.name}" for p in pack_files]
    html_packs = read_index_packs(index_path)
    if html_packs != disk_packs:
        raise ValueError(
            f"index.html pack scripts mismatch: index.html has {html_packs}, "
            f"disk has {disk_packs}"
        )
    if not read_index_packs_deferred(index_path):
        raise ValueError(
            "index.html pack script tags must include the defer attribute"
        )

    # 5. Optional Node.js syntax check on unpacked assets/game.js.
    if args.check_js:
        node_bin = shutil.which("node")
        if not node_bin:
            raise RuntimeError("node binary not found for --check-js")
        with tempfile.TemporaryDirectory() as tmp:
            game_tmp = Path(tmp) / "game.js"
            game_tmp.write_bytes(by_path["assets/game.js"]["data"])
            res = subprocess.run(
                [node_bin, "--check", str(game_tmp)],
                capture_output=True,
                text=True,
                check=False,
            )
            if res.returncode != 0:
                raise ValueError(f"Packed assets/game.js syntax error:\n{res.stderr}")

    # 6. Optional deterministic round-trip verification.
    if args.check_roundtrip:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            unpacked_dir = tmp_path / "unpacked"
            run1_dir = tmp_path / "run1"
            run2_dir = tmp_path / "run2"

            for rec in records:
                dest = unpacked_dir / rec["path"]
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(rec["data"])

            packs1, raw1, _ = write_packs(unpacked_dir, run1_dir, len(pack_files))
            packs2, raw2, _ = write_packs(unpacked_dir, run2_dir, len(pack_files))

            if raw1 != total_raw or raw2 != total_raw:
                raise ValueError(
                    f"Round-trip raw byte mismatch: orig={total_raw}, run1={raw1}, run2={raw2}"
                )

            for p1, p2 in zip(packs1, packs2):
                if p1.read_bytes() != p2.read_bytes():
                    raise ValueError(f"Non-deterministic output detected in {p1.name}")

            _, rt_records = read_all_packs(run1_dir)
            rt_hashes = {r["path"]: r["sha256"] for r in rt_records}
            orig_hashes = {r["path"]: r["sha256"] for r in records}
            if rt_hashes != orig_hashes:
                raise ValueError("Round-trip SHA-256 content mismatch")

    print(
        f"PASS: Verified {len(records)} assets across {len(pack_files)} packs "
        f"(TOTAL={total_raw:,d}, boot.js & index.html synced"
        + (", game.js syntax ok" if args.check_js else "")
        + (", deterministic round-trip ok" if args.check_roundtrip else "")
        + ")"
    )
    return 0


def cmd_inspect(args: argparse.Namespace) -> int:
    root = repo_root()
    assets_dir = Path(args.assets_dir) if args.assets_dir else root / "assets"
    pack_files, records = read_all_packs(assets_dir)
    total_raw = sum(r["raw_n"] for r in records)
    total_pack_bytes = sum(p.stat().st_size for p in pack_files)

    print(f"Packs: {len(pack_files)} | Assets: {len(records)} | Raw: {total_raw:,d} B | Packed: {total_pack_bytes:,d} B")
    for p in pack_files:
        p_recs = [r for r in records if r["pack"] == p.name]
        print(f"\n[{p.name}] {p.stat().st_size:,d} B ({len(p_recs)} entries)")
        for r in p_recs:
            print(
                f"  {r['path']:44s} {r['mime']:22s} z={r['z']} "
                f"raw={r['raw_n']:9,d} b64={r['b64_len']:9,d} sha256={r['sha256'][:10]}"
            )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Reproducible asset unpacker, packer, and verifier for FaceOff."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_unpack = sub.add_parser("unpack", help="Unpack assets/pack-*.js into a directory")
    p_unpack.add_argument("--out", default="build/unpacked", help="Output directory")
    p_unpack.add_argument("--assets-dir", help="Override assets directory")
    p_unpack.set_defaults(func=cmd_unpack)

    p_pack = sub.add_parser("pack", help="Deterministically pack assets into pack-NN.js")
    p_pack.add_argument("--src", required=True, help="Source directory containing assets/")
    p_pack.add_argument("--packs", type=int, default=DEFAULT_PACK_COUNT, help="Number of pack files")
    p_pack.add_argument("--assets-dir", help="Override output assets directory")
    p_pack.add_argument("--boot", help="Override assets/boot.js path")
    p_pack.add_argument("--index", help="Override index.html path")
    p_pack.add_argument("--no-sync-boot", dest="sync_boot", action="store_false", default=True)
    p_pack.add_argument("--no-sync-index", dest="sync_index", action="store_false", default=True)
    p_pack.set_defaults(func=cmd_pack)

    p_verify = sub.add_parser("verify", help="Verify packs, boot.js TOTAL, index.html, and integrity")
    p_verify.add_argument("--assets-dir", help="Override assets directory")
    p_verify.add_argument("--boot", help="Override assets/boot.js path")
    p_verify.add_argument("--index", help="Override index.html path")
    p_verify.add_argument("--no-check-js", dest="check_js", action="store_false", default=True)
    p_verify.add_argument("--check-roundtrip", action="store_true", default=False)
    p_verify.set_defaults(func=cmd_verify)

    p_inspect = sub.add_parser("inspect", help="Inspect packed assets and sizes")
    p_inspect.add_argument("--assets-dir", help="Override assets directory")
    p_inspect.set_defaults(func=cmd_inspect)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
