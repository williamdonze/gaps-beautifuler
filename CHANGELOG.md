# GAPS HEIG-VD · Précision — CHANGELOG

## 7.7.0 — adresse mse.hes-so.ch

- Le style s'applique aussi à **mse.hes-so.ch**, qui sert le même GAPS à une autre adresse. Avant, l'extension ne faisait rien sur cette adresse.
- Les adresses couvertes n'existent plus qu'à un seul endroit : les `domain("…")` de l'enveloppe `@-moz-document` du UserCSS. `build.py` en tire les `matches` des manifestes Firefox et Chrome.
- Politique de confidentialité et README mis à jour.
- Aucun changement de style.
- Extensions Firefox et Chrome reconstruites en 7.7.0. À la mise à jour, Chrome et Firefox demandent d'autoriser le nouveau site.

## 7.6.1 — menus dans la fenêtre

- **Menus de la barre** : les sous-menus et sous-sous-menus ne sortent plus de la page.
  - Les panneaux d'Utilitaires, Élections et Masters s'alignent sur le bord droit de leur entrée au lieu du bord gauche.
  - Les sous-sous-menus s'ouvrent vers la gauche, sauf sous Horaires et Étudiant·e où il reste de la place à droite. Le chevron indique le côté d'ouverture.
  - Les libellés longs (candidats aux élections…) passent sur plusieurs lignes au lieu d'élargir le panneau.
  - Un pont invisible relie le panneau à son sous-sous-menu : la souris peut traverser l'espace qui les sépare.
  - Mobile : le sous-sous-menu se déplie dans le panneau, en retrait, avec un chevron tourné vers le bas.
- Extensions Firefox et Chrome reconstruites en 7.6.1.

## 7.6.0 — grille semestrielle, annonces compactes

- **Nouvelle page couverte : la grille semestrielle** (`/consultation/horaires/grillesemestrielle.php`, ciblée par `#control` et `#pages`) :
  - Titre « Grille semestrielle » avec le surtitre rouge « Horaires », comme les autres pages.
  - Les réglages « Mise en forme » deviennent une carte : cases à cocher en grille (trois colonnes sur ordinateur, une sur mobile), bouton « Générer le PDF » avec une icône de téléchargement.
  - « Aperçu » devient un intertitre, avec la mention « Format A3 paysage, tel qu'il sera exporté en PDF ».
  - Chaque feuille A3 est posée comme une page de papier (coins arrondis, ombre), réduite pour tenir dans la largeur. Elle n'est plus décalée de 390 px vers la gauche ni coupée. Sur mobile, elle défile en largeur.
  - Le contenu des feuilles garde exactement la mise en forme de GAPS (police Open Sans condensée, texte noir, interlignage). Cela vaut aussi pour la copie qui sert à l'export : le PDF ne change pas, et le texte ne devient plus clair en mode sombre.
- **Annonces** (accueil et page de connexion) : bloc beaucoup plus compact (372 → 183 px de haut sur ordinateur avec deux annonces) :
  - Surtitre « Annonces » dans une colonne étroite à gauche.
  - Titre et date sur une seule ligne, auteur·e à droite.
  - Le texte est limité à deux lignes, la troisième s'efface. Tout le texte s'affiche au survol, au toucher ou au focus d'un lien.
  - Sur la page de connexion, les annonces prennent la largeur de la carte et se placent au-dessus d'elle.
- Extensions Firefox et Chrome reconstruites en 7.6.0.

## 7.5.2 — republication

- Numéro de version augmenté pour pouvoir renvoyer l'extension au Chrome Web Store, qui refuse un paquet de même version que celui déjà publié (7.5.1).
- Aucun changement de style par rapport à 7.5.1.
- Extensions Firefox et Chrome reconstruites en 7.5.2.

## 7.5.1 — logo intégré

- Le logo HEIG-VD de la barre du haut est maintenant intégré au CSS (PNG en data URI, 7 Ko), au lieu d'être chargé depuis Wikimedia Commons. Le style ne fait plus aucune requête vers un autre site.
- Aucun changement visuel.
- Extensions Firefox et Chrome reconstruites en 7.5.1.

## 7.5.0 — annonces de l'accueil

- **Annonces** (`#news_root`, en haut de la page d'accueil) :
  - Une carte à la largeur du tableau de bord, au lieu d'une boîte de 600 px.
  - Surtitre rouge « Annonces » avec un pictogramme de haut-parleur.
  - Chaque annonce : titre en gras, date en dessous, auteur·e à droite avec une icône, texte aéré limité à 72 caractères par ligne, liens soulignés en rouge.
  - Plusieurs annonces sont séparées par un filet.
  - Le fond violet `#eef` et la bordure noire disparaissent. Le texte devenu illisible en mode sombre est corrigé.
  - La hauteur fixe posée par GAPS ne coupe plus le texte.
  - Mobile : l'auteur·e passe sous la date et la carte ne déborde plus (601 px auparavant).
- Les autres pages sont identiques à la version 7.4.1.
- Extensions Firefox et Chrome reconstruites en 7.5.0.

## Extension Chrome (sur la base de 7.4.1)

- Nouveau dossier `extension-chrome/` : GAPS Beautifuler pour Chrome, Edge, Brave et Opera (Manifest V3, `gaps-beautifuler-chrome.zip`). Même CSS et même logo que la version Firefox, générés par `build.py`. Installation et publication : voir `extension-chrome/README.md`.

## Extension Firefox (sur la base de 7.4.1)

- Nouveau dossier `extension-firefox/` : extension Firefox **GAPS Beautifuler**, qui applique le style sans Stylus (`gaps-beautifuler.xpi`). Elle ne contient que du CSS, sans aucun script. Le CSS est généré depuis le UserCSS par `build.py`. Installation : voir `extension-firefox/README.md`.

## 7.4.1 — connexion centrée

- **Connexion** : la carte est centrée verticalement dans la fenêtre. La page occupe toute la hauteur de l'écran. Si la fenêtre est trop basse, ou sur mobile, la page défile normalement.
- Les 30 autres pages sont identiques au pixel près.

## 7.4.0 — page de connexion

- **Nouvelle page couverte : la connexion** (affichée à toute adresse tant qu'on n'est pas identifié·e ; ciblée par `#wayf_div`).
  - Une carte centrée : surtitre « Connexion à GAPS », grand titre « Bienvenue », explication en texte courant.
  - Choix de l'organisation edu-ID : libellé « Organisation », liste pleine largeur, bouton « Continue » pleine largeur (44 px). Le cadre gris `#F0F0F0` disparaît ; le logo edu-ID passe en gris, inversé en sombre.
  - Liens d'aide soulignés discrètement en rouge.
  - « Accès école » devient une rangée repliable avec un chevron à la place du « ➕ ». Le dépliage reste géré par le JS de GAPS. Une fois ouvert : champs empilés pleine largeur, bouton « Entrer » pleine largeur.
  - Le cadre de contact `#DDF` à bordure noire devient une note discrète sous la carte.
  - Mobile : la carte de 600 px et le cadre de 450 px ne débordent plus.
- Les 30 pages déjà couvertes sont identiques au pixel près.

## 7.3.0 — bulletin de notes

- **Nouvelle page couverte : le bulletin de notes** (`/consultation/notes/bulletin.php`, tableau `#record_table`).
  - Le total des crédits ECTS passe en tête, en chiffre clé.
  - Chaque module est une ligne forte : code, intitulé, situation en pastille, année, note en grand, crédits.
  - Les unités sont en retrait sous leur module, avec le détail Cours / Examen en petit.
  - L'en-tête des colonnes reste visible au défilement.
  - Les fonds `#bbd` / `#eef` et les bordures noires disparaissent ; les textes illisibles en mode sombre sont corrigés.
  - Mobile : trois colonnes (intitulé, note, crédits), sans débordement.
- Aperçus : le nom de l'étudiant·e est flouté dans les captures du bulletin et des contrôles continus.

## 7.2.1 — contrôles continus

- **Page couverte : contrôles continus** (`/consultation/controlescontinus/consultation.php`).
  - Le titre `h3.title` (bleu, italique, illisible en sombre) devient un grand titre avec le surtitre « Mes études » et le nom de l'étudiant·e en lien avec une icône.
  - La période académique devient une barre d'outils compacte (Année, Semestre).
  - Les notes sont présentées par unité : en-tête de l'unité, colonne « Cours / moyenne / poids », lignes avec survol, chiffres alignés.
  - La légende n'est plus une petite fenêtre fixe `#8888FF` posée par-dessus la page (qui débordait en mobile) : elle est placée sous le tableau, en ligne, avec ses symboles en puces.
- **Correctif transverse** : le composant « message d'état » ne s'applique plus à une boîte contenant un champ (`select`, `input`, `textarea`). Le sélecteur de période était pris pour un message. Les pages Évaluation, Awards, Sujets TB et Erreur sont inchangées au pixel près.

## 7.2.0 — fiches d'unité et de module

- **Nouvelle page couverte : la fiche d'unité** (`/consultation/fiches/uv/uv.php`, atteinte par « Voir la fiche d'unité »). Le même gabarit `.sheet-box` sert aussi aux fiches de module (`mv.php`), donc le style s'y applique également.
  - En-tête : bouton « ← Retour à la liste », surtitre « Fiche d'unité d'enseignement », grand titre, code de l'unité en puce, module parent.
  - Outils à droite : sélecteur de programme et bouton PDF.
  - Programmes en contrôle segmenté.
  - Une carte par section :
    - infos clés en grille libellé / valeur, sans les « : » ;
    - périodes en chiffres clés ;
    - temporalité avec le semestre actif en pastille rouge ;
    - prérequis, objectifs, contenu (périodes alignées à droite) et bibliographie ;
    - évaluation : contrôle des connaissances et note finale côte à côte.
  - Le bandeau bleu `#8888FF`, le fond `#DDDDFF`, le titre violet et les séparateurs bleus disparaissent. Le second bouton « Retour » reste en bas de page, sans bandeau.
- **À vérifier sur le vrai site** :
  - le découpage des périodes qui s'affiche au clic sur une case de temporalité ;
  - le voile de rechargement (`.rfreloading`) au changement de programme ;
  - une fiche de module (`mv.php`), qui n'a pas été capturée.

## 7.1.1 — codes couleur conservés, sélecteurs robustes

- **Codes couleur rétablis sur les cours** : dans le parcours Étudiant·e, chaque statut a sa couleur, identique dans la légende, les pastilles des cours et le total.
  - suivi : bleu franc `#2563eb`, distinct de la lavande GAPS ;
  - à suivre : vert ;
  - équivalence : orange ;
  - échange : orange hachuré ;
  - souhaitable : jaune ;
  - remplacé : gris barré.

  La v7.0 rendait « suivi » en gris neutre, si bien que l'information disparaissait des cours.
- **Mises en avant rouges des pages Élections** : rétablies en rouge, avec `--accent-text`, lisible en clair comme en sombre.
- **Sélecteurs sur les styles inline rendus tolérants aux espaces** : les captures SingleFile compactent les styles (`width:18px`), alors que le vrai site peut les écrire avec des espaces (`width: 18px`). Les 23 sélecteurs concernés acceptent maintenant les deux formes, ainsi que les couleurs à 6 chiffres (`#6699ff`…).
  - Test : chaque page a été re-générée avec tous ses styles inline espacés. Les 27 rendus sont identiques au pixel près à ceux des captures compactes, alors que l'ancienne version différait.
- **Audit des couleurs porteuses d'information** (script `colors.js`) : chaque élément coloré des pages d'origine a été comparé avant/après. Étudiant·e garde 70 éléments sur 70, Graphe 4 sur 4, Élections 7 sur 7. Seuls deux textes d'aide décoratifs passent volontairement en gris : la consigne bleue de Candidatures et la note rouge de la brochure.

## 7.1.0 — états de chargement

- **« Chargement ... » remplacé** : GAPS affiche un `<h1 class="loading">` brut pendant que son JavaScript remplit la page.
  - **Fiche Étudiant·e** (`h1.loading` suivi de `#studentDataDiv`) : un squelette à la forme de la fiche (portrait, surtitre, nom, champs, boutons), balayé par un reflet. Il existe une version empilée pour le mobile. Les formes sont dessinées par un masque SVG, donc aux couleurs des tokens dans les deux thèmes.
  - **Toute autre page** utilisant `.loading` : un anneau d'accent qui tourne et le libellé « Chargement ».
  - Les deux n'apparaissent qu'après 150 ms (fondu) : pas de flash quand la page charge vite. Avec `prefers-reduced-motion`, l'anneau et le reflet s'immobilisent.
- **À vérifier** : les autres pages GAPS qui chargent leur contenu après coup peuvent utiliser un autre élément que `.loading` ; si c'est le cas, envoyer une capture.

## 7.0.3 — correctif Élu·e·s (candidatsexternes.php)

- **Liste des élu·e·s coupée** : à l'ouverture, GAPS fixe la hauteur de la liste en la calculant pour des cartes de 120 px, ce qui coupait les cartes v7, plus hautes. Ouverte, la liste prend maintenant sa hauteur naturelle. Repliée (hauteur 0), elle disparaît sans marge résiduelle.

## 7.0.2 — correctif Candidat·e·s

- **Texte tronqué et flèche sans effet** : GAPS fige chaque carte à 120 px (style inline), ajoute une flèche aux cartes qui débordent, puis recalcule la hauteur au clic. La marge interne ajoutée en v7 faussait ce calcul : une flèche apparaissait même sur des cartes sans texte, et le dépliage n'aboutissait pas. Les cartes prennent désormais leur hauteur naturelle (`height: auto !important`). Le texte s'affiche en entier, sans clic, et la flèche est retirée. Le portrait occupe toute la hauteur de la carte, et les cartes d'une même rangée ont la même hauteur. Même traitement pour la liste des élu·e·s.

## 7.0.1 — correctif Plages communes

- **Photo de survol démesurée** : quand on cherche une personne, GAPS insère sa photo (`#photo_gestac`) à côté de la liste de suggestions. Rien ne limitait sa taille : elle s'affichait à 300 × 406 px par-dessus le formulaire. Elle devient une vignette de 96 px, qui n'intercepte plus la souris. Elle est masquée sur petit écran et sur les appareils tactiles, où il n'y a pas de survol.
- **Champ « Personne » en mobile** : il dépassait de 9 px (`width: 100%` plus le padding, en `content-box`). Il passe en `border-box`, et la liste d'auto-complétion est bornée à la largeur de l'écran.

## 7.0.0 — toutes les pages dans le même style

La v6 couvrait l'accueil et l'horaire. La v7 étend le design system « Précision » aux 26 pages capturées, sans nouveau token de couleur : tout passe par les variables de `:root`. La seule exception est la palette sémantique, comme pour les types de cours (voir plus bas).

### Ce qui change pour tout le site

- **Composants transverses (section 9)** :
  - titre de page avec surtitre rouge (`--page-kicker`), comme sur `.schedule-name` ;
  - carte `table.displayArray` ;
  - message d'état centré (« Erreur », « Saisie fermée ») ;
  - liste déroulante à chevron maison ;
  - icônes `--i-check`, `--i-download`, `--i-lock`, `--i-alert`, `--i-folder`, `--i-search`, `--i-filter`, `--i-plus`, `--i-minus` (SVG au trait, 24×24, `stroke-width` 2).
- **Bug v6 corrigé** : la règle `table.box:not(:has(table))`, écrite pour le pied de page de l'accueil, capturait aussi toute boîte de contenu sans tableau imbriqué. Elle masquait le titre et centrait le texte en gris. Les pages Programme (12 671 px de haut au lieu de 3 669), Évaluation, Awards et Sujets TB étaient touchées. Elle est maintenant neutralisée partout sauf sur l'accueil et l'horaire.
- **Accessibilité** : le bloc `prefers-reduced-motion` est désormais le dernier du fichier, et aucune `transition` n'est en `!important`. Le mouvement réduit l'emporte donc toujours.
- **Bleus GAPS** : aucun bleu ne reste, survols compris. C'est vérifié automatiquement sur toutes les couleurs calculées (fond, texte, bordures) des 26 pages × 3 modes.

### Vérifications faites (26 pages × clair 1440 / sombre 1440 / mobile 390)

- `scrollWidth ≤ largeur de la fenêtre` : 78/78.
- Contraste AA (texte ≥ 4,5:1, grand texte ≥ 3:1) : 0 échec. Le script remonte les fonds réels, y compris en mode sombre.
- Les 1 109 sélecteurs ont été testés un à un dans Chromium : aucun n'est rejeté. Un `:has()` imbriqué dans un autre `:has()` est ignoré en silence par le navigateur ; un tel cas a été trouvé puis corrigé.
- En-tête partagé : comparaison au pixel v6 → v7 sur les 25 pages qui l'ont. L'écart maximal est de 1/255, dû au flou `backdrop-filter` de la barre en verre qui échantillonne le contenu situé dessous. Il est invisible.

---

## Pages

### Étudiant·e (détail) — `#studentDataDiv`
**Critique.** La fiche est un tableau bleu à deux colonnes séparées par un pointillé, avec un nom noyé dans « Nom : Morel ». Le parcours est un mur de lignes bleues alternées, de liens violets et de cellules `#69f`, sans hiérarchie entre année, module et unité. Les absences sont un bandeau `#8888FF` au-dessus d'un tableau vide à 15 colonnes.
**Organisation.**
- **Héros** : la fiche. Photo arrondie, surtitre « Étudiant·e », **Prénom Nom** en grand (les deux lignes sont réordonnées avec `order`), puis des paires libellé / valeur sur deux colonnes, la formation en second groupe. Le bulletin (PDF, version web), les contrôles continus et l'horaire actuel deviennent des boutons secondaires avec icône.
- **Cœur** : le parcours. L'année est un intertitre, le module un groupe sur `--surface-2`, l'unité une ligne avec survol. Les crédits sont une pastille arrondie dans la cellule. Les statuts gardent leur code couleur, identique dans la légende et sur chaque cours : suivi en bleu, à suivre en vert, équivalence en orange, échange en orange hachuré, souhaitable en jaune, remplacé en gris barré (v7.1.1). « Afficher le programme de formation » devient un interrupteur ; la légende devient une rangée de pastilles.
- **Absences** : une carte titre + filtres + tableau. Quand il n'y a aucune absence, les 15 en-têtes sont masqués au profit d'un état vide (« Aucune absence » avec une coche), parce qu'ils n'apportent rien.

**À vérifier sur le vrai site.**
- Lignes « programme virtuel » (`#anneeVirtuelle`, `#moduleVirtuel`…) affichées par l'interrupteur : elles héritent du style du tableau, mais leurs couleurs inline n'ont pas été vues.
- Vue « par unité » (`#the_div_2`, remplie par le JavaScript).
- `#documentsdiv` (documents dépliables).
- Tableau d'absences rempli.

### Programmes de formation (liste) — `ul.filieres`
**Critique.** Une colonne de bandeaux `#66a`, de « + » et de liens violets, avec beaucoup de bleu et peu de lisibilité.
**Organisation.** Une carte, une ligne par domaine : le domaine à gauche, ses orientations à droite. Chaque orientation est une rangée cliquable avec un chevron qui glisse au survol. En mobile, la mise en page passe sur une colonne avec des zones de 44 px.
**À vérifier.** Le contenu révélé au clic sur une orientation (`li` en `display:none` dans la capture) reçoit un style de liste générique.

### Programme de formation (détail) — `#teachingplanbox`
**Critique.** Tableau `#DDDDFF` / `#BBBBDD` ; l'examen n'est signalé que par un « bord gras » quasi invisible. La v6 cassait la page : `padding` de 20 px sur chaque cellule, texte centré et grisé.
**Organisation.**
- Titre « Programme de formation GCOM 2025 PT ».
- Deux actions secondaires : graphe des prérequis, brochure PDF (avec la mention de délai en note discrète).
- Le tableau en héros : modules en intertitres (ECTS et seuils en sous-ligne), unités en lignes, années en bandes très légères. Les cellules d'examen sont une pastille avec un liseré droit, fidèle à la légende d'origine (« bords gras = examen »). Les groupes d'unités alternatives (« A (75) ») ont un discret liseré rouge.
- La légende devient une note en carte, sur deux colonnes.
- En mobile, la première colonne reste collante et le tableau défile horizontalement.

### Graphe des prérequis — `#prerequisites`
**Critique.** Les réglages et la légende sont collés dans un tableau bleu ; le graphe flotte sans cadre.
**Organisation.**
- Titre de page.
- Une carte réglages | légende séparée par un filet. Chaque type d'arc est représenté par un trait de sa couleur : vert, violet, orange, rouge (palette sémantique, inchangée parce qu'elle porte le sens).
- Le graphe dans un cadre pointillé, défilable horizontalement.
- En mobile, la légende passe après les réglages.

**À vérifier.** Le canvas vis.js garde ses nœuds bleu clair (#97C2FC) : ils sont dessinés par le JavaScript et seul un `filter` pourrait les changer, ce qui fausserait aussi la couleur des arcs. Le cadre du canvas reste blanc en mode sombre pour que le texte noir des nœuds reste lisible.

### Élections · présentation (2 pages) — `table.electionnoborder`
**Critique.** Contenu SharePoint collé : tableaux imbriqués sur six niveaux, Tahoma, rouge vif partout, deux colonnes de longueurs très inégales.
**Organisation.**
- Titre de page.
- Une carte de lecture pour l'introduction, avec le logo CORE à droite et des lignes limitées à 66 caractères. La phrase d'appel à candidature devient un callout `--accent-soft`.
- Les rubriques (Marche à suivre, Composition, Électorat, Règles, Textes de loi) en grille de cartes.
- Les mises en avant rouges deviennent du gras ; seule la date de la séance constitutive garde l'accent.

### Candidat·e·s (2 pages) — `.candidats-list`
**Critique.** Onglets façon 2005, bandeaux `rgba(136,136,255)` sur chaque carte, barre « déplier » bleue.
**Organisation.**
- Les collèges en contrôle segmenté, défilant en mobile.
- La ligne « Législature… » en méta discrète.
- Les candidat·e·s en grille de cartes portrait. Le dépliage devient un fondu avec un chevron.
- « Afficher les élu·e·s » devient un bouton secondaire pleine largeur.
- Un collège vide affiche un état vide en pointillé.

**À vérifier.**
- Carte dépliée au clic : la hauteur inline pilotée par GAPS est conservée, la grande photo (`.big-picture`) est stylée mais n'a pas été vue.
- Liste des élu·e·s ouverte (sa hauteur est animée par le JavaScript).
- Le libellé du bouton est réécrit en « Afficher les élu·e·s », parce que le `content` d'origine est mal encodé.

### Candidatures — `#divcandidature`
**Critique.** Un formulaire tableau à bordures noires, un fieldset `#eef`, une aide en bleu `#2c4db1`, un interrupteur vert.
**Organisation.**
- Titre de page.
- L'échéance en callout.
- Une seule carte : les faits (collège, sièges, législature, statut avec pastille) en paires clé / valeur, puis « Informations sur votre candidature » en intertitre.
- Le consentement photo dans un encart, avec un interrupteur Oui / Non à l'accent.
- La zone de texte en pleine largeur.
- Le bouton principal reste le seul rouge.

**À vérifier.**
- États « déjà candidat·e » (boutons modifier / supprimer, masqués dans la capture).
- Messages d'erreur `.formulaire_div_message`.
- Compteur de caractères en direct.

### Votes — `#main_box`
**Critique.** Un bandeau bleu pour dire « le scrutin n'est pas ouvert ».
**Organisation.** Un état clair et centré (pictogramme d'urne, titre, phrase), puis les répondant·e·s juste dessous, à la même largeur.
**À vérifier.** Le scrutin ouvert : bulletin de vote non capturé, il reçoit seulement le style générique de carte.

### Résultats (2 pages) — `div.rates`
**Critique.** Quatre lignes de texte pour quatre chiffres clés.
**Organisation.** Le titre, puis une rangée de quatre tuiles chiffrées (la participation globale sur `--accent-soft`), puis les remerciements en carte.
**À vérifier.** Les résultats détaillés, s'ils apparaissent après le scrutin.

### Enseignements à choix (saisie) — `table.explanations`
**Critique.** Titre bleu en italique et bloc « Explications » `#DDDDFF`.
**Organisation.** Titre de page avec surtitre ; l'explication devient un callout `--accent-soft` avec une icône.
**À vérifier.** La période de saisie ouverte : le formulaire de préférences n'a pas été capturé.

### Statistiques des enseignements à choix — `#tabsdiv` / `#unitlistdiv`
**Critique.** Filtres aux bordures noires épaisses, sélection `#2B6FB6` ; tableau à 62 % de la largeur ; plus de 100 lignes sans repère.
**Organisation.**
- Filtres en puces étiquetées « Département » et « Formation », la sélection à l'encre.
- Le tableau en pleine largeur tant que le panneau de droite est vide : résumé à gauche, compteur à droite, en-têtes **collants sous la barre** pendant le défilement, chiffres en `tabular-nums`, codes d'unités en encre (et non en rouge) pour garder l'accent rare.

**À vérifier.**
- Panneau de droite (`#colonnedroiteplandiv`) rempli au clic : il passe en carte, sous le tableau.
- Infobulles `.popup_content`.

### Liste des enseignements — `form[name="teachingBox"]`
**Critique.** La page n'a pas de titre, juste un mini-formulaire centré de 220 px et une ligne d'aide Outlook.
**Organisation.**
- Titre « Liste des enseignements » ajouté.
- Le formulaire devient une barre de filtres horizontale : quatre champs + « Afficher ». Il passe sur deux colonnes, puis une seule en mobile.
- L'aide Outlook devient une ligne discrète avec une icône « ? ».

**À vérifier.** Le tableau de résultats après « Afficher » n'a pas été capturé. Le texte d'aide Outlook déplié est stylé en encart.

### Remédiations — `div.gaps-main-box`
**Critique.** Bandeau bleu, boîte de 300 px de haut pour une phrase.
**Organisation.** Titre + sélecteur d'année sur une ligne, puis le contenu en carte. Sans remédiation, la carte affiche un état vide avec une coche.
**À vérifier.** La liste de remédiations (`#uvlinks`) quand il y en a.

### Archives des horaires
**Critique.** Deux listes à puces de liens, séparées par des virgules, sous des titres violets.
**Organisation.**
- L'année en cours en titre de page.
- T1 à T4 en tuiles avec icône calendrier.
- Les années précédentes en rangées : l'année à gauche, des puces T1 à T4 à droite. Les virgules sont des nœuds texte : chacune tombe dans une colonne de grille de largeur nulle et la puce suivante la recouvre.

### Plages communes — `#master_box`
**Critique.** Formulaire `#DDDDFF` à bordure noire, libellés de 95 px.
**Organisation.**
- Titre.
- Le formulaire en carte : libellés à gauche, champs à droite, recherche de personne avec une loupe.
- Les personnes sélectionnées en puces.
- La complétion automatique jQuery UI en popover.

**À vérifier.**
- Menu d'auto-complétion ouvert.
- Puces des personnes choisies (le DOM réel n'a pas été vu).
- `#divschedules` (la grille des plages communes, générée par le JavaScript).
- Photo au survol `#photo_gestac`.

### Documentation Master — `table.boxtree`
**Critique.** Un `select` seul, puis un arbre en Verdana 11 px.
**Organisation.** Titre « Documentation », sélecteur du master, arbre en carte avec de vraies icônes : dossier en accent, fichier en neutre, rangées de 36 px.

### Horaire Master (synthèse) — `#horaires`
**Critique.** Titre caché sous la navigation, cases à cocher brutes, grille de fieldsets gris et liens rouges.
**Organisation.**
- La page est réordonnée en flex, uniquement ici : titre, puis sélecteur d'année ‹ en contrôle segmenté, puis filtres.
- Les catégories de modules (MA, PI, MC-CM, MC-FTP, MC-TSM) deviennent des puces dont la pastille colorée sert **aussi de légende**. Leur palette est celle des types de cours.
- PDF en bouton secondaire.
- La grille hebdomadaire en carte : un site par encart, un module par ligne avec un liseré de catégorie.
- « Autres horaires » sous la grille, comme sur la page Horaire.

**À vérifier.**
- Menus déroulants de `#menu_horaires`.
- Infobulle de l'icône ⊕ d'un module.
- Filtres appliqués (modules masqués).

### Modules centraux [MC] / d'approfondissement [MA] — `#master_box:has(> .region_gauche)`
**Critique.** Colonne de 150 px de `select` tronqués, liste à bordures noires, sélection bleu ciel ; fiche en lignes de formulaire à 95 px et tableaux gris.
**Organisation.** Un vrai maître / détail.
- **Gauche** : barre latérale collante avec les filtres, la liste défilante (élément sélectionné en `--accent-soft`) et l'export Excel.
- **Droite** : la fiche, dont le titre du module devient l'en-tête, avec l'abréviation en puce. Les autres champs sont en paires clé / valeur et les tableaux internes sont nets.
- La grille des spécialisations est faite de deux tables (en-tête + corps) : leurs colonnes sont forcées sur les mêmes pourcentages pour rester alignées.
- Les icônes « i » d'origine (images bleues) passent en niveaux de gris.

**À vérifier.**
- Dialogues jQuery UI (`.ui-dialog`, Aide…).
- Changement de module au clic.
- Grille plus longue que la capture.

### Évaluation des enseignements, HEIG-VD Awards, Sujets de TB
**Critique.** Des boîtes « Erreur » / « Saisie fermée » rendues comme un pied de page par la v6.
**Organisation.** Un composant **message d'état** : carte centrée, pictogramme (cadenas, calendrier, info), titre, explication.
**À vérifier.** Ces pages ouvertes (sondage, vote Awards, liste de sujets) n'ont pas été capturées.

### Erreur (sans menu) — `div.body:not(:has(#menu_root))`
**Critique.** Logo GAPS JPEG sur dégradé bleu, page étroite.
**Organisation.** La barre en verre du site est reconstruite (logo HEIG-VD), puis le message d'état avec un pictogramme d'alerte.

---

## Limites et points à connaître

- **Accueil et Horaire.** Les fichiers de référence n'étaient pas dans le dossier fourni ; seule « Horaire Master » y figure, et c'est une autre page. La non-régression a donc été assurée par construction :
  - les sections 1 à 8 de la v6 sont reprises octet pour octet (vérifié par diff ; seules `@version` et `@description` changent) ; seul le bloc « mouvement réduit » est déplacé, inchangé, à la fin ;
  - toute règle nouvelle susceptible de toucher ces pages exclut explicitement l'accueil (`table.box table[style*="border-collapse"]`) et l'horaire (`#scheduleDiv`) ;
  - l'en-tête commun a été comparé au pixel près.

  À refaire sur le vrai site : ouvrir l'accueil et l'horaire et vérifier qu'ils sont inchangés.
- **Mobile.** GAPS n'a pas de `<meta name="viewport">` : un vrai téléphone rend la page sur 980 px virtuels et le CSS ne peut pas changer ça. Les règles ≤ 639 px (et les captures « mobile 390 ») concernent les fenêtres étroites et les navigateurs ou extensions qui imposent une largeur d'appareil.
- **Couleurs en dur.** En dehors des tokens, il n'y en a que quatre sortes :
  - la palette sémantique (types de cours, statuts du parcours, catégories de modules Master, arcs du graphe) ;
  - `#fff` pour la pastille des interrupteurs ;
  - `#fff` pour le fond du logo CORE et du canvas du graphe, nécessaire en mode sombre pour garder lisibles les contenus noirs non stylables.
- **Logo.** Le logo HEIG-VD externe (`--g-logo`) ne se charge pas dans un environnement sans réseau ; c'est normal.
- **Captures.** Les données personnelles (photos, nom, coordonnées, candidat·e·s) sont floutées **dans les aperçus seulement**, par le script de rendu ; le CSS livré ne floute rien.
