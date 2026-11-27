# Changelog

All notable changes, gameplay systems, and architectural capabilities of FaceOff (formerly DustIII) are documented in this file.

The format follows Keep a Changelog, and this project uses Semantic Versioning.

---

## [Unreleased]

## [10.1.0] - 2026-11-27

### Added

- Ranked page with serverless matchmaking (PeerJS lobby: the first player online coordinates, others take over when they leave), live online / searching / in-match counts, and ranked bots whose difficulty follows the player's rank (V9).
- Account and rank system: tiers Rookie to Legend, placement matches, rank page, save codes, Bilibili Toy profile support (V8).
- Quick-buy keys (`F1` full buy, `F2` eco, `F3` rebuy last round) routed through the normal buy command so they also work for online guests, plus `F4` to skip the buy phase in bot matches. Rebuilt from the community `foEnhance` prototype inside the source modules.
- Round damage summary (damage dealt, damage taken, headshot rate), expose-phase edge pulse and ring, match-point / overtime tension beat (toggle in Settings → Audio), and contact shadows under players.
- Author credit links between the GitHub Pages and Bilibili Toy builds.

### Changed

- Gunplay follows CS2: damage, armor penetration, ×4 headshots, range falloff, armor points that wear down, Kevlar $650 / Kevlar + Helmet $1000, fixed spray patterns with recoil decay, 45% view-punch tracking, run-and-gun inaccuracy, CS2 prices, fire rates, magazines, movement speeds and economy ($800 start, $16000 cap, $3250 round win, $1400–$3400 loss bonus).
- Only Ranked matches change rank points; Practice (bots) and Rooms (friends) only record stats.
- Network protocol version bumped to 5; players must run the same build to play together.
- README rewritten for FaceOff in English and Simplified Chinese.

### Fixed

- Ported the community fixes from the packed bundle into source: neck hitbox gap (standing body top 1.54, head 1.68; crouched 1.07 / 1.20), single-penetration counting through thick or stacked crates using entry / exit face detection, 0.004 m post-hit step, 5-ray grenade bounce collision, validated navigation links on `depot` and `patio`, bot fixes (no knowledge of the opponent's weapon or health, aim at visible body parts, shoot into smoke, flash-dodge using the real grenade trajectory, cross-round opponent modeling, wired `memory` / `flankChance` / `holdChance` / `peekPatience`), MSAA disabled at `devicePixelRatio >= 1.5`, and the sight description (1.35x).
- Bots no longer get stuck jumping in place: progress checks ignore vertical movement.

### Removed

- Localized READMEs other than English and Simplified Chinese.

## [8.1.0] - 2026-11-26

### Added

- Standardized repository scaffolding: `readme.md`, `changelog.md`, `license`, `security.md`, and GitHub issue and pull request templates.
- Browser-game README covering controls, local serving, architecture, diagnostics, privacy, and licensing.
- Localized README documentation in six additional languages (`readme.de.md`, `readme.es.md`, `readme.fr.md`, `readme.ja.md`, `readme.zh-cn.md`, `readme.zh-tw.md`) with multi-language selector navigation.
- GitHub Actions Pages workflow publishing the static build at [the live demo](https://amfi-disable.github.io/DustIII/), plus a live-demo badge in every localized readme.
- Custom domain configuration (`CNAME`) for GitHub Pages pointing to `dustiii.is-cool.dev`.
- Automated offline quality checks in GitHub Actions CI (`ci.yml`) validating JavaScript syntax, YAML configurations, lowercase filenames, and commit message conventions.
- Packed game bundle (`assets/pack-00.js`, `assets/pack-01.js`, `assets/pack-02.js`) with in-memory `DecompressionStream` unpacking in `index.html` for `assets/game.js`, GLB weapon and operator models, audio banks, bundled fonts, and five arenas (`depot`, `greybox`, `patio`, `range`, `skyline`).
- PeerJS/WebRTC networking configuration (`window.FACEOFF_NET`) and bundled `PeerJS` runtime support in the `FACEOFF` build.

### Changed

- Extracted the `DecompressionStream` single-file unpacker from `index.html` into `assets/boot.js` with CSP violation diagnostics, `blob:` module fallback loading, and updated bundle payloads (`assets/pack-00.js`, `assets/pack-01.js`, `assets/pack-02.js`).
- Lowercased marker texture assets to `mark_a.png` and `mark_b.png`, and updated the `js/world.js` references.
- Modernized GitHub Pages deployment workflow actions to standard versions (`actions/checkout@v6`, `actions/configure-pages@v6`, `actions/upload-pages-artifact@v5`, `actions/deploy-pages@v5`).
- Replaced the unbundled `js/*.js` ES module files and loose `assets/` subdirectories (`chars/`, `fx/`, `tex/`, `ui/weapons/`, `weapons/`, `world/`) with the packed `FACEOFF` game bundle and `index.html` loader.
- Expanded the JavaScript syntax validation glob in `.github/workflows/ci.yml` to check `assets/*.js` alongside `js/*.js`.

### Fixed

- **Game Modes**: Added Mirror Duel (identical rotating loadouts each round) and Escalation (8-weapon Gun Game 1v1 ending on knife) alongside Classic 1v1 in the Play menu and via `?mode=` URL parameters.
- **Cross-Round Bot Modeling**: Added rolling per-match player tendency tracking (rush rate, AWP frequency, contact distance) driving dynamic counter-plans across Normal, Hard, and Pro tiers.
- **Gameplay Flow Shortcuts**: Added one-key buy presets (`F1` Full Buy, `F2` Eco, `F3` Rebuy Last), `Space` skip-buy in solo bot matches, and a compact post-round damage and headshot summary bar.
- **Visual And Audio Polish**: Added dynamic operator contact shadows, Expose-phase pulsing radar ring VFX, and subtle 104 BPM adaptive in-match tension stems during Expose and Match Point / Overtime.
- **Interface Language Toggle**: Added an in-page `EN / 中文` switcher persisted in `localStorage`.
- **Distinct Bot Difficulty Behavior**: Overhauled `easy`, `normal`, `hard`, and `pro` profiles with distinct tactical plans, hold timings, peek styles, AWP bolt-cycle punishes, and Pro Expose ping-reversal jukes.
- **Loader And Render Performance**: Deferred pack and boot script tags in `index.html`, disabled MSAA when `devicePixelRatio >= 1.5`, pruned unused `assets/models/smg.glb`, and synced `assets/boot.js` `TOTAL` byte count.
- **Hitbox And AI Fixes**: Closed standing (`1.50` -> `1.54`) and crouched (`1.02` -> `1.06`) neck hitbox gaps, removed AI `enemyWeapon` / `enemyHp` omniscience, fixed projected flash-dodge trajectory and turn-away timing, wired dead `PM` keys (`memory`, `flankChance`, `holdChance`, `peekPatience`), fixed `sight` description (`1.25x` -> `1.35x`), and updated `kr.defaultMap` to `range`.
- **Tight-Space And Penetration Fixes (#2)**: Added visibility-aware exposed-part and narrow-slit targeting in `H()` so bots never empty magazines into head-glitch cover, fixed `ft()` and `g1()` entry/exit tracking so single penetrable crates (> 0.5m) incur only one penetration penalty, and reduced the post-hit surface-clear step from `0.06m` to `0.004m` so targets flush behind thin cover are never skipped.
- **Grenade Physics And Navmesh Fixes (#4)**: Upgraded `gS()` from a single zero-thickness ray to a 5-ray swept-sphere envelope with seam-normal smoothing and normal depenetration to eliminate doorframe/railing clipping and erratic seam bounces; eliminated all dead-end navmesh nodes across `range`, `depot`, `skyline`, and `patio` and added 4 collision-validated balcony `drop` edges to `patio`.
- **Under-Fire Flinch And ADS Gate Fixes (#1)**: Added a `0.18s` hit-dampening cooldown, cumulative flinch cap, and non-deferring `nextFix` recovery in `bS.punch()` so continuous 600–800 RPM sprays no longer stun-lock bots; added difficulty-scaled `aimPunch` (`f.punchY`/`f.punchP`) compensation in `H()`; and allowed bots to fire while ADSing when taking fire or in close-mid range.
- **Smoke Suppression And Edge Tactics (#3)**: Added honest difficulty-tiered smoke-suppression bursts in `Qe()` when an opponent just vanished into smoke (`< 1.5s`) or fired audibly behind smoke (`hard` 55% / `pro` 78% with realistic angular spread; `normal` 15% restrained; `easy` 0%), and replaced hardcoded post-smoke pushes with weapon-aware edge-hold, flash-through, and flank tactics in `Qe()` and `Ei()`.
- **3D Model, Hitbox, And Map Collision Alignment (#11)**: Audited `operator_animated.glb`, `operator_lod1.glb`, `helmet.glb`, `sockets_viewer.json`, and all four map GLB/collision meshes; aligned standing (`[1.68, 0.16]`, spanning `1.52–1.84m`) and crouched (`[1.20, 0.15]`, spanning `1.05–1.35m`) head hitboxes to cover the full `helmet.glb` crown (`1.561–1.835m`) with zero neck gap, and updated all 24 `skyline` skylight `glass` collision triangles from `triFlags = 0` to `triFlags = 2` (penetrable).
- **Close-Range Angular Tracking Fix (#6)**: Replaced hard-zero angular velocity cutoffs (`Math.abs(lt) < 6 ? lt : 0`) in `PL` -> `H()` with bounded clamping (`[-8, 8]` rad/s yaw, `[-6, 6]` rad/s pitch), exponential velocity smoothing, and teleport/first-engagement reset (`> 28 rad/s` or `justEngaged`) so bots track close-range strafes smoothly without stalling or twitching.
- **Bot Gunplay Intelligence (#7)**: Added weapon- and HP-aware exposed-part selection in `H()` (AWP prioritizes center-mass; Hard/Pro finish low-HP `<= 35` opponents on body mass; rifles/pistols keep head priority at full HP), weapon/distance/bloom-aware firing cadence (MAC-10 close sprays, AK/M4 mid-range 3–5 round bursts and long-range bloom-gated 1–2 round taps, Deagle bloom pacing), and deterministic dry-mag sidearm swaps on Hard/Pro.
- Updated all seven player guides and the page description for the current first-to-nine duel, four selectable arenas and online room flow.

- Corrected internal heading anchor links across documentation for table of contents navigation.

---

## [1.0.0] - 2026-10-20

Inaugural import of the Dust II Defusal browser game.

### Added

- **Competitive Ruleset**: MR12 match flow, halftime side swap, freeze time, buy window, and the full C4 plant and defuse loop.
- **Economy Model**: Starting money, round cap, loss-bonus ladder, kill awards, and plant or defuse bonuses.
- **Weapon Sandbox**: 34 firearms across pistols, SMGs, shotguns, rifles, and machine guns, plus knives, the Zeus x27, C4, and six grenades.
- **Ballistics**: Per-weapon spray patterns, recoil recovery, armor penetration, hitgroup multipliers, distance falloff, and wall penetration.
- **Bot Director AI**: Four difficulty tiers, team-level execute directors, vision and hearing perception, flash reaction, and post-plant behavior.
- **Dust II World**: Full callout coverage, baked map and navigation data, BVH-accelerated raycasts, and movement-only clip ramps.
- **HUD And Presentation**: Radar, buy menu, scoreboard, kill feed, procedural weapon and character models, first-person viewmodel, and postprocessing.
- **Synthesized Audio**: Positional gunfire, footsteps, reloads, radio lines, and bomb cues.
- **Static Delivery**: Zero-backend ES module application with a pinned import map.

### Security

- Fully client-side simulation with zero telemetry, zero analytics, and zero backend services.
