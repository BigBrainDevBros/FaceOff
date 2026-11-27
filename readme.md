<div align="center">

# 对枪 FACEOFF

**1v1 round-based shooter that runs in your browser**
*Buy, duel, win the round. CS2 damage, armor and spray patterns, eight weapons, four compact maps, ranked matchmaking, bots and peer-to-peer online play. No install, no server.*

[![Play: Live](https://img.shields.io/badge/Play-Live%20on%20GitHub%20Pages-success.svg?style=flat-square&logo=githubpages)](https://bigbraindevbros.github.io/FaceOff/)
[![Bilibili Toy](https://img.shields.io/badge/Also%20on-Bilibili%20Toy-00A1D6.svg?style=flat-square&logo=bilibili&logoColor=white)](https://www.bilibili.com/toy/faceoff)
[![Version](https://img.shields.io/badge/Version-V10.1-blue.svg?style=flat-square)](#changes-in-v10)
[![Engine: Three.js](https://img.shields.io/badge/Engine-Three.js-black.svg?style=flat-square)](https://threejs.org)
[![Mode: 1v1](https://img.shields.io/badge/Mode-1v1%20Duel-orange.svg?style=flat-square)](#how-a-match-works)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](license)

[Play Online](https://bigbraindevbros.github.io/FaceOff/) · [Bilibili Toy](https://www.bilibili.com/toy/faceoff) · [中文说明](readme.zh-cn.md) · [MIT License](license)

[Player Guide](docs/wiki/home.md) · [Contributing](contributing.md)

</div>

> [!NOTE]
> **Official releases, same creator.** FACEOFF is published in exactly two places:
> this repository (played at [bigbraindevbros.github.io/FaceOff](https://bigbraindevbros.github.io/FaceOff/)) and
> [bilibili.com/toy/faceoff](https://www.bilibili.com/toy/faceoff). Both are made by the same creator; neither is a copy of the other.
> The main menu of each version links to the other one.

---

## Star History

<a href="https://www.star-history.com/?type=date&repos=BigBrainDevBros%2FFaceOff">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=BigBrainDevBros%2FFaceOff&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=BigBrainDevBros%2FFaceOff&type=date&legend=top-left" />
    <img alt="BigBrainDevBros/FaceOff Star History Chart" src="https://api.star-history.com/chart?repos=BigBrainDevBros%2FFaceOff&type=date&legend=top-left" />
  </picture>
</a>

---

**[English](readme.md)** • **[简体中文](readme.zh-cn.md)**

## Contents

- [Play](#play)
- [How A Match Works](#how-a-match-works)
- [Weapons And Gear](#weapons-and-gear)
- [Maps](#maps)
- [Ranked](#ranked)
- [Online Play](#online-play)
- [Controls](#controls)
- [Changes In V10](#changes-in-v10)
- [Privacy](#privacy)
- [Self-Hosting](#self-hosting)
- [License](#license)

---

## Play

Open **[bigbraindevbros.github.io/FaceOff](https://bigbraindevbros.github.io/FaceOff/)** in a desktop browser (Chrome, Edge, Firefox or Safari) and pick a mode from the main menu:

| Mode | What it is | Rank points |
| :--- | :--- | :--- |
| **Ranked** | Find a real opponent, or play a ranked bot whose difficulty follows your rank | Yes |
| **Practice** | Pick any map and bot difficulty | No |
| **Rooms** | Create a room and share the code with a friend | No |

Click the game view to capture the mouse. The interface is in Chinese. Keyboard and mouse are required; touch devices are not supported.

## How A Match Works

- **First to 9 rounds.** At 8:8 the match goes to overtime: the first player two rounds ahead wins.
- **Every round:** a short buy phase in your spawn, then the fight. Kill your opponent to win the round. If time runs out, the player with more health wins.
- **No camping:** near the end of each round both players' positions are revealed at intervals.
- **Economy:** start with $800. Winning, losing streaks and kills all pay out. Dying drops everything except your default pistol, so sometimes saving money is the right call.

## Weapons And Gear

| Slot | Weapons |
| :--- | :--- |
| Rifles | AK-47, M4A4 |
| Sniper | AWP |
| SMG | MAC-10 |
| Pistols | USP-S, Tec-9, Desert Eagle |
| Melee | Knife |

- **CS2 numbers.** Damage, armor penetration, fire rate, magazine size, prices and movement speed follow CS2. Headshots deal ×4, legs ×0.75, and damage falls off with distance.
- **One-taps.** The AK-47 and Desert Eagle kill with one headshot even through a helmet; the M4A4 and USP-S need two. The AWP kills with one shot to the head or body.
- **Fixed spray patterns.** Every gun kicks the same way every time (the AK climbs for about 10 shots, then swings left and right), so you can learn to pull down against it. The first shot always lands on the crosshair.
- **Stop before you shoot.** Shooting while running or jumping is very inaccurate; release the movement keys (or tap the opposite one) and you are accurate again within about 0.1 s.
- **Sights:** every gun can aim down sights (right mouse button); add a holo / red dot ($200) or 2x scope ($500).
- **Armor:** Kevlar ($650) protects the body; Kevlar + Helmet ($1000, or $350 for just the helmet) also protects the head. Armor has 100 points and wears down as you take hits.

## Maps

| Map | Layout |
| :--- | :--- |
| 靶场 RANGE | Crates in the middle, long east corridor, raised platforms at both ends |
| 货场 DEPOT | Container alleys and a second-floor steel walkway |
| 天台 SKYLINE | High-rise rooftop with a central steel platform |
| 庭院 PATIO | Alley corners, a courtyard and balconies |

## Ranked

- **Tiers:** Rookie → Gunner → Marksman → Elite → Ace → Master (each III → I) → Legend.
- **Find Match:** pairs you with an online player of similar skill. If nobody turns up within 30 seconds you can switch to a ranked bot.
- **Ranked bot:** difficulty follows your rank (Rookie: Easy, Gunner: Normal, Marksman: Hard, Elite and up: Pro) and gives a share of the points of a real match. From Ace up, bot matches no longer give points.
- **Placement:** your first 5 matchmade games set your starting rank.
- **Your account:** on Bilibili Toy the game uses your Bilibili nickname and avatar (after you allow it). On GitHub Pages it creates a local profile. Progress is stored in your browser; a **save code** on the rank page moves it to another device.
- The ranked page shows how many players are online, searching and in a match. Matchmaking runs without a server: the first player online hosts the lobby, and someone else takes over when they leave.

## Online Play

- **Room codes:** one player creates a room and shares the 5-character code; the other joins.
- **Peer-to-peer:** the host's browser runs the match and the other player connects directly. There is no game server.
- **If a room code doesn't connect,** use the manual invite / answer codes, or open **联机对战 → 网络诊断** (network diagnostics) to see what is blocked.
- Both players must run the same version. The GitHub Pages and Bilibili Toy builds of the same version can play each other.

## Controls

| Action | Key |
| :--- | :--- |
| Move | `W` `A` `S` `D` |
| Fire | Left mouse |
| Aim down sights / heavy knife | Right mouse |
| Jump / Crouch | `Space` / `Ctrl` |
| Walk (silent) | `Shift` |
| Reload | `R` |
| Primary / Pistol / Knife / Utility | `1` `2` `3` `4` |
| Pick up weapon | `E` |
| Buy menu | `B` |
| Quick buy: full / eco / rebuy last round | `F1` / `F2` / `F3` |
| Skip buy phase (bot matches) | `F4` |
| Scoreboard | `Tab` |
| Menu | `Esc` |

Most keys can be rebound in **Settings → Keybinds**. `B`, `Tab` and `Esc` are fixed.

## Changes In V10

- **CS2 gunplay:** CS2 damage, ×4 headshots, armor points, fixed spray patterns, run-and-gun penalty, CS2 prices and economy.
- **Ranked page (V9):** matchmaking, ranked bots that follow your rank, live player counts. Practice and Rooms no longer change your rank.
- **Merged community fixes:** tighter hitboxes, cleaner wall penetration through crates, grenades that no longer slip into wall seams, extra bot navigation links, and smarter bots (no wallhack knowledge of your gun or health, aim at visible body parts, shoot through smoke, read your playstyle across rounds).
- **New:** quick-buy keys, a round damage summary, expose-phase pulse, match-point tension beat, and contact shadows.

## Privacy

- **No analytics, no tracking, no ads.**
- **Local storage only:** settings, stats and rank progress stay in your browser.
- **Online play** connects to the public PeerJS signaling service and public STUN servers only to set up the direct connection between the two players. After that, game traffic goes player-to-player.
- **On Bilibili Toy**, your nickname and avatar are read through Bilibili's own permission dialog and used only for display.

## Self-Hosting

The site is a static bundle: `index.html` plus `assets/pack-*.js` and `assets/boot.js`. Serve the repository root from any static host (GitHub Pages, Cloudflare Pages, Netlify, nginx).

To try it locally:

```bash
git clone https://github.com/BigBrainDevBros/FaceOff.git
cd FaceOff
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## License

[MIT](license) © AMFI-Disable
