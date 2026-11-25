<div align="center">

# FaceOff

**ブラウザーで遊べる1対1の対戦ゲーム。先に9ラウンド取った側が勝利します。**

![Platform](https://img.shields.io/badge/Platform-Desktop%20Browser-blue?style=flat-square)
![Mode](https://img.shields.io/badge/Mode-1v1-orange?style=flat-square)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](license)

[オンラインで遊ぶ](https://bigbraindevbros.github.io/FaceOff/) · [Changelog](changelog.md) · [Security](security.md)

</div>

[English](readme.md) · [简体中文](readme.zh-cn.md) · [繁體中文](readme.zh-tw.md) · [日本語](readme.ja.md) · [Español](readme.es.md) · [Français](readme.fr.md) · [Deutsch](readme.de.md)

## 対戦を始める

マウスとキーボードで **Play** を開き、Range、Depot、Skyline、Patio のいずれかと、4段階のボット難易度を選びます。**Start Match** で対戦開始。1ラウンドは50秒で、残り20秒になると位置が表示されます。

友達と遊ぶときは、両者ともデスクトップ版 Chrome または Edge で同じバージョンを開きます。**Online** でホストが5文字のルームコードを共有します。WebRTC 接続のシグナリングには PeerJS を使います。手動接続コードとネットワーク診断も用意されています。

**Settings** で感度、照準、画質、音量、キー割り当てを調整できます。操作方法は **How to Play** で確認できます。

## スター数の推移

<a href="https://www.star-history.com/?type=date&repos=bigbraindevbros%2Ffaceoff">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
    <img alt="BigBrainDevBros/FaceOff Star History Chart" src="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
  </picture>
</a>

## ローカルで起動する

リポジトリのルートでサーバーを起動し、ブラウザーでローカルアドレスを開きます。3つのアセットパックとローダーは assets ディレクトリにまとめて配置します。

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

[127.0.0.1:8000](http://127.0.0.1:8000/)

第三者のライセンス表記は [index.html](index.html) にあります。
