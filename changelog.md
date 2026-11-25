# Changelog

All notable changes, gameplay systems, and architectural capabilities of FaceOff (formerly DustIII) are documented in this file.

The format follows Keep a Changelog, and this project uses Semantic Versioning.

---

## [Unreleased]

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
