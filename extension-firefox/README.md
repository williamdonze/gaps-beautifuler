# GAPS Beautifuler · extension Firefox

Le même style que `gaps-heig-moderne.css`, mais sans Stylus. L'extension ne contient que du CSS : aucun script, aucune donnée collectée, et elle n'agit que sur `gaps.heig-vd.ch`.

Fichier à installer : `gaps-beautifuler.xpi`.

> Désactive le style dans Stylus si tu installes l'extension. Sinon, le CSS est appliqué deux fois. Ce n'est pas grave, mais c'est inutile.

## Installer

Firefox (version normale) n'installe pour de bon que les extensions **signées par Mozilla**. Trois possibilités :

### 1. Signer gratuitement chez Mozilla (recommandé, définitif)

1. Crée un compte sur <https://addons.mozilla.org/developers/>.
2. Clique sur « Submit a New Add-on », puis choisis **« On your own »**. L'extension n'est pas publiée dans le catalogue : elle reste privée.
3. Envoie `gaps-beautifuler.xpi`. La signature automatique prend en général quelques minutes.
4. Télécharge le `.xpi` signé et glisse-le dans une fenêtre Firefox. L'extension reste installée après redémarrage.

### 2. Essai rapide (jusqu'à la fermeture de Firefox)

1. Ouvre `about:debugging#/runtime/this-firefox`.
2. Clique sur « Charger un module complémentaire temporaire… ».
3. Choisis `gaps-beautifuler.xpi` (ou `src/manifest.json`).

### 3. Firefox Developer Edition, Nightly ou ESR

1. Dans `about:config`, mets `xpinstall.signatures.required` à `false`.
2. Glisse le `.xpi` non signé dans une fenêtre Firefox.

Cette option ne fonctionne pas dans la version normale de Firefox.

## Changer le logo

Place ton image dans ce dossier sous le nom `logo.png` (ou `.jpg`, `.jpeg`, `.webp`), puis lance `python3 build.py`. Une image carrée d'au moins 128 × 128 px donne le meilleur résultat ; sinon, elle est centrée sur un fond transparent. Sans `logo.png`, une icône « G » rouge est générée.

Le logo actuel vient de `logo.svg` (le fichier d'origine), exporté en `logo.png` 512 × 512 et recadré sur le dessin pour qu'il reste lisible en 16 px dans la barre d'outils.

## Mettre à jour après une modification du CSS

```sh
python3 build.py
```

Le script régénère `src/gaps.css` à partir de `../gaps-heig-moderne.css`, en retirant l'enveloppe `@-moz-document` que Firefox n'accepte plus hors Stylus. Il reprend aussi le `@version` dans le manifeste et refait le `.xpi`. Si l'extension est signée (option 1), il faut envoyer la nouvelle version chez Mozilla pour la signer à nouveau.

Firefox 142 ou plus récent est nécessaire.
