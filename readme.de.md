<div align="center">

# FaceOff

**Browserduelle eins gegen eins. Wer neun Runden gewinnt, gewinnt das Match.**

![Platform](https://img.shields.io/badge/Platform-Desktop%20Browser-blue?style=flat-square)
![Mode](https://img.shields.io/badge/Mode-1v1-orange?style=flat-square)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](license)

[Online spielen](https://bigbraindevbros.github.io/FaceOff/) · [Changelog](changelog.md) · [Security](security.md)

</div>

[English](readme.md) · [简体中文](readme.zh-cn.md) · [繁體中文](readme.zh-tw.md) · [日本語](readme.ja.md) · [Español](readme.es.md) · [Français](readme.fr.md) · [Deutsch](readme.de.md)

## Ein Duell Spielen

Öffne **Play** mit Maus und Tastatur. Wähle Range, Depot, Skyline oder Patio und eine von vier Bot-Schwierigkeiten. Mit **Start Match** beginnt das Duell. Eine Runde dauert 50 Sekunden. In den letzten 20 Sekunden werden die Positionen sichtbar.

Für ein Duell mit Freunden nutzt dieselbe Version in Chrome oder Edge am Computer. Unter **Online** teilt der Gastgeber einen fünfstelligen Raumcode. PeerJS vermittelt die WebRTC-Verbindung. Das Menü bietet auch manuelle Verbindungscodes und eine Netzwerkdiagnose.

Unter **Settings** kannst du Empfindlichkeit, Fadenkreuz, Grafik, Ton und Tastenbelegung anpassen. **How to Play** erklärt die Steuerung.

## Sternverlauf

<a href="https://www.star-history.com/?type=date&repos=bigbraindevbros%2Ffaceoff">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
    <img alt="BigBrainDevBros/FaceOff Star History Chart" src="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
  </picture>
</a>

## Lokal Starten

Starte den Server im Stammverzeichnis und öffne die lokale Adresse. Die drei Datenpakete und der Loader gehören zusammen in den Ordner assets.

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

[127.0.0.1:8000](http://127.0.0.1:8000/)

Lizenzhinweise zu Drittanbietern stehen in [index.html](index.html).
