---
name: orphic-build
description: "Construire ou mettre à jour un site LOCAL depuis un wireframe validé dans Olympus. À utiliser dès qu'un prompt demande de mettre à jour / construire / générer un site pour qu'il corresponde à un BRIEF.md, un wireframe ou une arborescence — en particulier le prompt du bouton « Génération automatique » d'Olympus (« Mets à jour ce site en local pour qu'il corresponde au wireframe décrit dans …/BRIEF.md »). Couvre la lecture de l'espace ~/Pegasus/<slug>/ (BRIEF.md, wireframe.json, moodboard.json, site.json, content.json, wordpress/), le diagnostic de l'existant, la construction WordPress locale ou statique, l'auto-vérification par scripts, et le rendu final. Déclencher aussi sur : BRIEF.md, wireframe, brief de construction, génération automatique, « fais correspondre le site au wireframe »."
---

# Orphic Build — du wireframe validé au site local

Ce skill est **le chaînon entre Olympus et le site réel** : un wireframe a été
validé dans Olympus, un brief de construction a été généré, ton travail est de
faire exister (ou évoluer) le site **en local** pour qu'il corresponde à ce brief.

Deux règles avant tout :

1. **Tout se passe en local.** Tu ne touches JAMAIS au site en ligne. Pas
   d'appel `pegasus_update_content` ou `pegasus_install_theme` vers la prod
   dans ce skill : la mise en ligne est une décision humaine, prise plus tard,
   via le bouton « Pousser en ligne » d'Olympus (voir §7).
2. **La doctrine design reste** [`orphic-web-design`](../orphic-web-design/SKILL.md).
   Ce skill dit QUOI construire et OÙ ; le skill design dit COMMENT ça doit
   être beau, animé, lisible et rapide. Ne réinvente rien : lis-le.

---

## 1. Déclenchement et contexte d'exécution

Le cas nominal : Olympus lance Claude dans `~/Pegasus/<slug>/` avec le prompt

> « Mets à jour ce site en local pour qu'il corresponde au wireframe décrit
> dans `<chemin>/BRIEF.md`. Crée ou adapte les pages, sections, boutons et
> connexions entre pages, en respectant la charte du moodboard indiquée dans
> le brief. »

Le répertoire courant est l'espace du site. Tout ce dont tu as besoin est
dedans. Si le prompt arrive hors de cet espace (Sacha qui demande à la main),
localise d'abord le bon `~/Pegasus/<slug>/` avant d'écrire quoi que ce soit.

## 2. Les entrées — qui dit quoi

| Fichier | Rôle | Autorité |
|---|---|---|
| `wireframes/build-<id>/BRIEF.md` | Brief de construction généré | **Source de vérité de la STRUCTURE** (pages, sections, boutons, liens, menus) |
| `wireframes/build-<id>/wireframe.json` | Version figée du wireframe | Données brutes (ids, `wp_id`, cibles de sections) si le BRIEF est ambigu |
| `moodboard.json` | Charte : couleurs, typos, logo, notes, refs | **Source de vérité du VISUEL** |
| `site.json` / `content.json` / `home.html` | Snapshot du site réel | État actuel — à lire, jamais une cible d'écriture |
| `wordpress/` (si présent) | WordPress local complet | Le chantier : c'est LÀ que tu construis |
| `arborescence.json` | Wireframe de travail (vivant) | Contexte seulement — le brief figé prime |

Format du BRIEF.md : `## Charte graphique` (couleurs/typos/logo/notes/références)
puis `## Pages (N)` avec `### Header` (menu global), `### <Page> — niveau N`,
des lignes `- Section « X » — bouton → Page` et `- Lien → Page`, et `### Footer`.
Un exemple réel complet : [`references/exemple-BRIEF.md`](references/exemple-BRIEF.md)
(fixture générée par Olympus — le contrat de format à respecter des deux côtés).
Chaque ligne du brief est un engagement : une section nommée doit exister, un
bouton `→ Page` doit réellement mener à cette page.

## 3. Diagnostic AVANT d'écrire — le plan des écarts

Interdiction de poser une ligne de code avant d'avoir ce plan. Dans l'ordre :

1. **Inventorier l'existant.** `wordpress/` présent → lister les pages WP
   (base locale ou `wp post list` via wp-cli local si dispo), le thème actif,
   les menus. Sinon → lister les `.html` du dossier et lire `content.json`
   pour savoir quelles pages du site réel existent.
2. **Comparer au brief**, page par page, section par section, lien par lien.
3. **Écrire le plan des écarts** (dans ta tête ou un fichier de travail,
   jamais dans les fichiers d'Olympus) :
   - pages à **créer** ;
   - pages existantes : sections à **ajouter / renommer / retirer** ;
   - boutons et liens à **câbler** (chaque `→ Page` du brief) ;
   - menus Header/Footer à mettre en conformité ;
   - pages à **ne PAS toucher** (conformes au brief) — elles deviennent des
     zones protégées de fait : conformes = intouchables.
4. **Annoncer le plan** en début de réponse avant d'exécuter. Si le brief
   contredit frontalement l'existant (page supprimée du wireframe mais riche
   en contenu réel), signale-le : tu retires du menu et des liens, tu ne
   détruis pas du contenu sans le dire.

## 4. Construction

### Cas A — `wordpress/` présent : thème custom local

Modèle éprouvé : le thème **emotionsarts**. Un thème custom, pas un page
builder :

- `front-page.php` pour la home ; **un template par type de page** du brief
  (`page-<slug>.php` ou template dédié) — chaque section du brief = une
  section identifiable dans le template.
- `functions.php` avec un hook `after_switch_theme` qui **crée les pages
  manquantes** (titres + slugs du brief, en s'appuyant sur les `wp_id` du
  wireframe.json quand ils existent pour ne pas dupliquer), **construit les
  menus** Header/Footer conformes au brief, et règle les
  **permaliens `/%postname%/`**.
- Enqueue propre des styles/scripts (charte du moodboard en variables CSS,
  GSAP & co selon le niveau retenu — voir skill design §3).
- Les boutons `→ Page` du brief : de vrais liens vers les permaliens des
  pages cibles, pas des `#`.

Tu écris les fichiers PHP **dans le WordPress local uniquement**. La doctrine
Pegasus (jamais d'écriture PHP à distance, déploiement par zip de thème via
`pegasus_install_theme`) concerne la mise en ligne — qui n'est pas ton
travail ici.

### Cas B — pas de `wordpress/` : site statique

- `index.html` pour la home, un `<slug>.html` par page du brief.
- Liens relatifs entre pages ; menu Header/Footer identique partout (fragment
  partagé ou dupliqué à l'identique).
- CSS avec la charte en variables, animations selon le niveau retenu.

Dans les deux cas : **mise à jour incrémentale**. Si le site existe déjà, tu
adaptes ; tu ne repars de zéro que si rien d'existant n'est récupérable, et
tu le justifies.

## 5. Le visuel — la doctrine vient d'ailleurs

- **Le registre visuel sort du `moodboard.json`**, pas d'un défaut. Pas de
  sombre-dramatique automatique : si le moodboard dit bordeaux/ivoire, le
  site est bordeaux/ivoire. Moodboard vide → demande, ou propose un registre
  argumenté par le secteur — ne tranche pas en silence.
- **Motion avec intention**, niveau technique N1-N4 choisi et justifié,
  interdits absolus (jamais statique, jamais template, jamais illisible,
  jamais lent), **zones protégées** sur tout ce qui a déjà été validé :
  tout cela est dans [`orphic-web-design/SKILL.md`](../orphic-web-design/SKILL.md)
  et ses `references/`. Lis-le au moment de designer, ne le paraphrase pas.
- Les contenus texte : reprends l'existant (`content.json`, pages WP) quand
  la page existe ; pour une page neuve, un contenu de travail sobre et
  crédible dans la langue du site — jamais de lorem ipsum brut.

## 6. Auto-vérification — les scripts avant de rendre la main

Les scripts du skill design sont **les faits** ; ton jugement vient après.
Depuis `${CLAUDE_PLUGIN_ROOT}/skills/orphic-web-design/scripts/` :

1. `check_contrast.py '#fg' '#bg' [--large]` sur **chaque couple texte/fond**
   issu de la charte appliquée.
2. `audit_page.py URL` sur la home locale et les pages créées/modifiées
   (WordPress local → son URL locale ; statique → sers le dossier le temps
   de l'audit).
3. **Vérifier chaque câblage du brief** : chaque `- Section « X » — bouton
   → Page` et chaque `- Lien → Page` mène à une page qui existe et répond.
   Un lien mort = un FAIL.

Un FAIL = tu corriges et tu re-vérifies **avant** de rendre la main. Si un
FAIL est structurellement incorrigible (ex. contraste imposé par la charte
du moodboard), tu ne bricoles pas la charte : tu le documentes dans le rendu
final pour arbitrage humain.

Ces scripts couvrent le **mesurable**. La passe de goût, elle, reste la
boucle de critique du skill design (§9 — `/pegasus:critique`, agent
orphic-critique) : rien ne part chez un client sans elle. Rappelle-le dans
le rendu final si le site a vocation à être montré.

## 7. Fin de course — le rendu

Ta réponse finale contient, dans cet ordre :

1. **Écarts brief ↔ réalisé** : ce qui a été créé, adapté, câblé — et ce qui
   n'a pas pu l'être, avec la raison.
2. **Verdicts scripts** : PASS/FAIL par vérification, corrections faites,
   FAIL restants à arbitrer.
3. **Ce qui n'a pas été touché** (pages conformes, contenu existant préservé).
4. **Le rappel de mise en ligne** : le site modifié est LOCAL. La mise en
   ligne passe exclusivement par le bouton **« Pousser en ligne »** d'Olympus
   (backups avant/après automatiques) — jamais déclenchée par ce skill,
   jamais automatique, toujours sur décision explicite de Sacha.
