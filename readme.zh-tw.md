<div align="center">

# FaceOff

**在瀏覽器中進行 1 對 1 回合制對決。先贏九個回合即可獲勝。**

![Platform](https://img.shields.io/badge/Platform-Desktop%20Browser-blue?style=flat-square)
![Mode](https://img.shields.io/badge/Mode-1v1-orange?style=flat-square)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](license)

[線上遊玩](https://bigbraindevbros.github.io/FaceOff/) · [Changelog](changelog.md) · [Security](security.md)

</div>

[English](readme.md) · [简体中文](readme.zh-cn.md) · [繁體中文](readme.zh-tw.md) · [日本語](readme.ja.md) · [Español](readme.es.md) · [Français](readme.fr.md) · [Deutsch](readme.de.md)

## 開始對局

使用滑鼠和鍵盤開啟 **Play**，從靶場、貨場、天台和庭院選一張地圖，再從四級難度中選擇對手。按下 **Start Match**。每回合 50 秒，最後 20 秒會顯示位置。

與朋友連線時，雙方使用桌面版 Chrome 或 Edge 開啟同一版本。在 **Online** 中，房主將五碼房號分享給朋友。房號透過 PeerJS 信令建立 WebRTC 連線。選單也提供手動連線碼和網路診斷。

在 **Settings** 中可調整滑鼠靈敏度、準星、畫面、聲音和按鍵配置。**How to Play** 列出遊戲操作。

## GitHub 星標歷史

<a href="https://www.star-history.com/?type=date&repos=bigbraindevbros%2Ffaceoff">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
    <img alt="BigBrainDevBros/FaceOff Star History Chart" src="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
  </picture>
</a>

## 本機執行

在儲存庫根目錄啟動伺服器，再用瀏覽器開啟本機網址。三個資源包和載入程式都應放在 assets 目錄。

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

[127.0.0.1:8000](http://127.0.0.1:8000/)

第三方授權聲明請見 [index.html](index.html)。
