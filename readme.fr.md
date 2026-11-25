<div align="center">

# FaceOff

**Des duels en un contre un dans le navigateur. Remportez neuf manches pour gagner le match.**

![Platform](https://img.shields.io/badge/Platform-Desktop%20Browser-blue?style=flat-square)
![Mode](https://img.shields.io/badge/Mode-1v1-orange?style=flat-square)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](license)

[Jouer en ligne](https://bigbraindevbros.github.io/FaceOff/) · [Changelog](changelog.md) · [Security](security.md)

</div>

[English](readme.md) · [简体中文](readme.zh-cn.md) · [繁體中文](readme.zh-tw.md) · [日本語](readme.ja.md) · [Español](readme.es.md) · [Français](readme.fr.md) · [Deutsch](readme.de.md)

## Jouer un duel

Ouvrez **Play** avec une souris et un clavier. Choisissez Range, Depot, Skyline ou Patio, puis un des quatre niveaux de difficulté du bot. Sélectionnez **Start Match**. Chaque manche dure 50 secondes. Les positions sont révélées pendant les 20 dernières secondes.

Pour affronter un ami, utilisez la même version dans Chrome ou Edge sur ordinateur. Dans **Online**, la personne qui crée le salon partage un code de cinq caractères. PeerJS assure la signalisation de la connexion WebRTC. Le menu propose aussi des codes de connexion manuels et un diagnostic réseau.

Dans **Settings**, réglez la sensibilité, le réticule, les graphismes, le son et les touches. **How to Play** présente les commandes.

## Historique des étoiles

<a href="https://www.star-history.com/?type=date&repos=bigbraindevbros%2Ffaceoff">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
    <img alt="BigBrainDevBros/FaceOff Star History Chart" src="https://api.star-history.com/chart?repos=bigbraindevbros%2Ffaceoff&type=date&legend=top-left" />
  </picture>
</a>

## Lancer le jeu en local

Démarrez le serveur depuis la racine du dépôt et ouvrez son adresse dans votre navigateur. Gardez les trois paquets de ressources et le chargeur dans le dossier assets.

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

[127.0.0.1:8000](http://127.0.0.1:8000/)

Les mentions de licence des composants tiers figurent dans [index.html](index.html).
