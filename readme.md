<div align="center">

# FaceOff

**One-on-one browser duels. Win nine rounds to take the match.**

![Platform](https://img.shields.io/badge/Platform-Desktop%20Browser-blue?style=flat-square)
![Mode](https://img.shields.io/badge/Mode-1v1-orange?style=flat-square)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](license)

[Play Online](https://bigbraindevbros.github.io/FaceOff/) · [Changelog](changelog.md) · [Security](security.md)

</div>

[English](readme.md) · [简体中文](readme.zh-cn.md) · [繁體中文](readme.zh-tw.md) · [日本語](readme.ja.md) · [Español](readme.es.md) · [Français](readme.fr.md) · [Deutsch](readme.de.md)

## Play A Duel

Open **Play** with a mouse and keyboard. Pick Range, Depot, Skyline or Patio, then choose one of four bot difficulty levels. Select **Start Match**. Each round lasts 50 seconds. Positions are revealed in the final 20 seconds.

For a game with a friend, both players should use the same version in desktop Chrome or Edge. In **Online**, the host shares a five-character room code. The room-code flow uses PeerJS signaling for a WebRTC connection. The menu also offers manual connection codes and network diagnostics.

Open **Settings** to adjust sensitivity, crosshair, graphics, audio and key bindings. **How to Play** lists the controls.

## Star History

<a href="https://www.star-history.com/?type=date&repos=bigbraindevbros%2Ffaceoff">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
    <img alt="BigBrainDevBros/FaceOff Star History Chart" src="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
  </picture>
</a>

## Run Locally

From the repository root, serve the page and open the local address in your browser. Keep the three asset packs together with the loader in the assets directory.

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

[127.0.0.1:8000](http://127.0.0.1:8000/)

Third-party license notices are included in [index.html](index.html).
