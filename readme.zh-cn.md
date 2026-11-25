<div align="center">

# FaceOff

**浏览器里的 1 对 1 回合制对枪。先赢九个回合即获胜。**

![Platform](https://img.shields.io/badge/Platform-Desktop%20Browser-blue?style=flat-square)
![Mode](https://img.shields.io/badge/Mode-1v1-orange?style=flat-square)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](license)

[在线游玩](https://bigbraindevbros.github.io/FaceOff/) · [Changelog](changelog.md) · [Security](security.md)

</div>

[English](readme.md) · [简体中文](readme.zh-cn.md) · [繁體中文](readme.zh-tw.md) · [日本語](readme.ja.md) · [Español](readme.es.md) · [Français](readme.fr.md) · [Deutsch](readme.de.md)

## 开始对局

用鼠标和键盘打开**开始对局**，在靶场、货场、天台和庭院中选一张地图，再从四档难度中选择对手。点击**开打**。每回合 50 秒，最后 20 秒会暴露位置。

与朋友联机时，双方用桌面版 Chrome 或 Edge 打开同一版本。在**联机对战**中，房主将五位房间码发给朋友。房间码通过 PeerJS 信令建立 WebRTC 连接。菜单也提供手动连接码和网络诊断。

在**设置**中调整鼠标灵敏度、准星、画面、声音和键位。**操作说明**列出游戏按键。

## GitHub 星标历史

<a href="https://www.star-history.com/?type=date&repos=bigbraindevbros%2Ffaceoff">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
    <img alt="BigBrainDevBros/FaceOff Star History Chart" src="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
  </picture>
</a>

## 本地运行

在仓库根目录启动服务器，用浏览器打开本地地址。三个资源包和加载器应放在同一个 assets 目录中。

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

[127.0.0.1:8000](http://127.0.0.1:8000/)

第三方许可声明见 [index.html](index.html)。
