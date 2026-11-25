<div align="center">

# FaceOff

**Duelos de uno contra uno en el navegador. Gana nueve rondas para llevarte la partida.**

![Platform](https://img.shields.io/badge/Platform-Desktop%20Browser-blue?style=flat-square)
![Mode](https://img.shields.io/badge/Mode-1v1-orange?style=flat-square)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](license)

[Jugar en línea](https://bigbraindevbros.github.io/FaceOff/) · [Changelog](changelog.md) · [Security](security.md)

</div>

[English](readme.md) · [简体中文](readme.zh-cn.md) · [繁體中文](readme.zh-tw.md) · [日本語](readme.ja.md) · [Español](readme.es.md) · [Français](readme.fr.md) · [Deutsch](readme.de.md)

## Jugar un duelo

Abre **Play** con ratón y teclado. Elige Range, Depot, Skyline o Patio y uno de los cuatro niveles de dificultad del bot. Pulsa **Start Match**. Cada ronda dura 50 segundos. Las posiciones se revelan en los últimos 20 segundos.

Para jugar con otra persona, usad la misma versión en Chrome o Edge de escritorio. En **Online**, quien crea la sala comparte un código de cinco caracteres. PeerJS coordina la conexión WebRTC. El menú también ofrece códigos de conexión manual y diagnóstico de red.

En **Settings** puedes ajustar la sensibilidad, la mira, los gráficos, el sonido y las teclas. **How to Play** muestra los controles.

## Historial de estrellas

<a href="https://www.star-history.com/?type=date&repos=bigbraindevbros%2Ffaceoff">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
    <img alt="BigBrainDevBros/FaceOff Star History Chart" src="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
  </picture>
</a>

## Ejecución local

Inicia el servidor desde la raíz del repositorio y abre la dirección local. Conserva los tres paquetes de recursos y el cargador en el directorio assets.

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

[127.0.0.1:8000](http://127.0.0.1:8000/)

Los avisos de licencia de terceros se encuentran en [index.html](index.html).
