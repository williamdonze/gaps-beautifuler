# GAPS Beautifuler · extension Chrome

Même style et même logo que l'extension Firefox. Fonctionne aussi dans Edge, Brave, Opera, Vivaldi et Arc, qui acceptent les extensions Chrome.

L'extension ne contient que du CSS : aucun script, aucune permission, aucune donnée collectée. Elle n'agit que sur `gaps.heig-vd.ch` et `mse.hes-so.ch` (le même GAPS, à une autre adresse).

> Désactive le style dans Stylus si tu installes l'extension. Sinon, le CSS est appliqué deux fois.

## Installer pour soi, sans publier (mode développeur)

1. Décompresse `gaps-beautifuler-chrome.zip` dans un dossier que tu gardes : Chrome lit l'extension depuis ce dossier.
2. Ouvre `chrome://extensions`, puis active **Mode développeur** (en haut à droite).
3. Clique sur **Charger l'extension non empaquetée** et choisis le dossier décompressé, celui qui contient `manifest.json`.

L'extension reste installée après redémarrage. Chrome peut afficher de temps en temps un rappel sur les extensions en mode développeur : il suffit de le fermer.

## Publier sur le Chrome Web Store

1. Ouvre <https://chrome.google.com/webstore/devconsole> et connecte-toi avec un compte Google. L'inscription coûte **5 $ une seule fois**.
2. Clique sur **Nouvel élément** et envoie `gaps-beautifuler-chrome.zip` tel quel, sans le décompresser.
3. Fiche :
   - catégorie « Outils » ou « Accessibilité » ;
   - langue française ;
   - une icône 128 × 128 (`src/icons/icon-128.png`) ;
   - au moins une capture d'écran en 1280 × 800 ou 640 × 400 ;
   - une description qui précise **non officielle, sans lien avec la HEIG-VD**.
4. Onglet **Pratiques de confidentialité** :
   - « Objectif unique » : *Restyler l'interface de GAPS (gaps.heig-vd.ch et mse.hes-so.ch) avec du CSS.*
   - Aucune donnée collectée : coche les attestations.
   - Aucune permission à justifier.
   - Pas de code distant, puisqu'il n'y a pas de script.
   - URL des règles de confidentialité : <https://github.com/williamdonze/gaps-beautifuler/blob/main/PRIVACY.md> (voir `../PRIVACY.md`).
5. **Envoyer pour examen.** Une extension uniquement CSS est en général acceptée en quelques jours.

Choisis la visibilité :
- **Public** : visible dans la recherche ;
- **Non répertorié** : installable seulement par celles et ceux qui ont le lien.

## Mettre à jour après une modification du CSS

```sh
python3 build.py
```

Le script régénère `src/` et le `.zip` à partir de `../gaps-heig-moderne.css` et de `../extension-firefox/logo.png`, et reprend le `@version`. Pour une mise à jour sur le Web Store, envoie le nouveau zip dans « Package » ; le numéro de version doit avoir augmenté.
