# GAPS Beautifuler

Refonte moderne et **non officielle** de [GAPS](https://gaps.heig-vd.ch) (HEIG-VD, aussi à l'adresse [mse.hes-so.ch](https://mse.hes-so.ch)) : design system « Précision », thème clair et sombre, sur toutes les pages. Uniquement du CSS : aucun script, aucune donnée collectée.

## Contenu

- `gaps-heig-moderne.css` : le style UserCSS (à utiliser avec Stylus), source unique de tout le reste, y compris les adresses couvertes : les `domain("…")` de son `@-moz-document` deviennent les `matches` des manifestes.
- `extension-firefox/` : extension Firefox, construite par `python3 build.py` → `gaps-beautifuler.xpi`.
- `extension-chrome/` : extension Chrome / Edge / Brave / Opera (Manifest V3), construite par `python3 build.py` → `gaps-beautifuler-chrome.zip`.
- `CHANGELOG.md` : historique des versions.

Les scripts de build nécessitent Python 3 et Pillow (`pip install pillow`). Voir le README de chaque extension pour l'installation.

Projet sans lien avec la HEIG-VD.
