---
name: orphic-web-design
description: "Constitution design web de l'agence Orphic (Monaco). À utiliser SYSTÉMATIQUEMENT pour toute création, maquette, refonte, critique ou direction artistique de site web, landing page, hero, section ou composant web — en WordPress/Pegasus, Next.js, Framer, Webflow ou React. Couvre le choix du niveau technique (flat, shaders, 3D, WebGL), la palette, la typographie, les animations et la validation anti-template. Déclencher dès que la conversation mentionne site web, site internet, maquette, webdesign, DA, direction artistique, landing, hero, section, composant, animation web, WebGL, Three.js, shader, Pegasus, ou un projet client web — même si le mot design n'est pas prononcé."
---

# Orphic Web Design — Skill racine

Ce skill est la **constitution** du design web d'Orphic. Tous les autres skills web
(motion, 3D, perf, SEO…) s'y réfèrent. En cas de conflit entre skills, ce document gagne.

Orphic est une agence 360° basée à Monaco ("Beyond Understanding"), avec une exigence
de niveau Awwwards. Les clients sont exigeants : chaque livrable doit viser
le meilleur résultat possible, pas le plus rapide à produire.

---

## 1. La règle-mère

> Un site Orphic doit être **animé avec intention, singulier, user-friendly et rapide**
> — les quatre EN MÊME TEMPS, jamais l'un au détriment d'un autre.

Ces quatre exigences sont en tension permanente. Le travail de design consiste à
les résoudre ensemble, pas à en sacrifier une :

- **Animé** pousse vers plus d'effets → mais **rapide** impose un budget strict.
  Résolution : chaque animation doit avoir une intention (révéler, guider, donner
  de la matière). Zéro décoration gratuite.
- **Singulier** pousse vers l'audace → mais **user-friendly** impose la lisibilité.
  Résolution : l'audace se loge dans la matière, le concept et le détail, jamais
  dans le sabotage de la navigation ou du contraste.

## 2. Les 4 interdits absolus

1. **Jamais de site sans animation.** Le mouvement fait partie du design.
   Un site statique n'est pas un site Orphic.
2. **Jamais un site qui ressemble aux autres.** Chaque projet doit contenir au
   moins une idée que personne d'autre n'a. Ça vaut aussi pour la signature
   Orphic elle-même : dark+chrome+glow appliqué mécaniquement = template.
3. **Jamais un site pas user-friendly.** Contrastes lisibles (viser AA), cibles
   tactiles ≥ 44px, navigation évidente, états de focus visibles,
   `prefers-reduced-motion` respecté. Le beau ne justifie jamais l'inutilisable.
4. **Jamais un site lent.** Budgets : LCP < 2,5 s, INP < 200 ms, CLS < 0,1.
   Si la 3D fait exploser le budget, on descend d'un niveau (voir §3) —
   souvent N4→N3 (temps réel → pré-rendu) résout tout. On ne livre pas lent.

## 3. Choisir le niveau (offre à 4 paliers)

Principe directeur (Akaru) : *« Maîtriser des techniques à l'avant-garde pour
pouvoir tout imaginer, mais utiliser uniquement celles que le projet justifie,
sans démonstration de force. »*

L'échelle est à la fois **technique et commerciale** : chaque palier ajoute une
compétence et du temps, donc un prix. La frontière tarifaire majeure est
**"Blender ou pas Blender"** (dès qu'on modélise, saut de compétence + de coût).

| Niveau | Nom (offre) | 3D ? | Blender ? | Compétence ajoutée | Références |
|---|---|---|---|---|---|
| **1** | **Premium** | Non | Non | Motion web (GSAP, Lenis, CSS 3D léger) | Kalinsky, Locomotive, Editorial New |
| **2** | **Luxe** | 3D perçue | Non | Shaders GLSL / WebGL 2D | Ryan Ritzenthaler, Lusion, Akaru, **Emotions Arts** |
| **3** | **Luxe supérieur** | 3D réelle pré-rendue | Oui | 3D pré-rendu (Blender → séquence → scrub) | Apple scroll-scrub, packshots Orphic animés |
| **4** | **Ultra luxe** | 3D temps réel | Oui | Portage temps réel + optimisation (glTF, budgets) | Igloo, Active Theory, Orphic Production |

**Ce que chaque niveau recouvre :**
- **N1 Premium** — Motion pur, zéro WebGL. GSAP/ScrollTrigger/Lenis/SplitType/
  Barba, micro-interactions, CSS 3D (Atropos, perspective, preserve-3d).
  Rapide, imbattable en perf, accessible.
- **N2 Luxe** — Effet 3D/wow avec du code + assets existants, sans modélisation :
  shaders sur surfaces 2D (Curtains.js, PixiJS, Paper Shaders), displacement au
  hover, parallax multi-couches, CSS 3D avancé. **Sweet spot** : spectaculaire,
  marge excellente, perf préservée.
- **N3 Luxe supérieur** — On ouvre Blender (→ prix). Objet modélisé/rendu, exporté
  en **vidéo ou séquence d'images**, scrubé au scroll. Rendu parfait
  (ray-tracing, matière), runtime léger. Parcours **figé**, pas d'interaction libre.
- **N4 Ultra luxe** — Vraie scène temps réel : Blender → glTF → R3F/Three, caméra
  pilotée, shaders custom, post-processing, **orbite/interaction libre**.
  Le plus cher, le plus long.

**Les deux frontières qui décident (et qui justifient le prix au client) :**
1. **N2 → N3** : *« Faut-il une matière ou un objet sur-mesure impossible sans
   modélisation ? »* Si oui → Blender → N3.
2. **N3 → N4** : *« L'utilisateur doit-il manipuler l'objet librement ? »*
   Non (dévoilement au scroll suffit) → **N3 pré-rendu**, souvent PLUS BEAU et
   MOINS CHER. Oui (orbite libre) → **N4 temps réel**.

⚠️ Ne pas survendre le N4 : un N3 pré-rendu bat souvent un N4 en qualité de
rendu pure, pour moins cher. Le temps réel ne se justifie que si
l'interactivité libre est un vrai besoin.

En cas de doute entre deux niveaux : prendre le plus bas et l'exécuter
parfaitement. Un niveau bien exécuté bat un niveau au-dessus bâclé.

## 4. Axe d'intention

En plus du niveau technique, qualifier l'intention — elle change les règles :

- **Vitrine / portfolio** (montrer un savoir-faire) : liberté artistique maximale.
- **Produit / e-commerce** (vendre) : l'immersion ne doit JAMAIS masquer le chemin
  d'achat. CTA, panier, fiche produit restent accessibles en permanence
  (leçon Organimo). Un site magnifique qui ne vend pas est un échec.
- **Univers / récit** (faire ressentir une identité) : le storytelling structure
  tout — loader qui pose le ton, transitions qui racontent, détails qui
  incarnent (leçon Michael Gatt).

## 5. La signature Orphic

**La méthode est constante, le registre s'adapte au client.**

Méthode (toujours) :
- Palette **2 couleurs** par défaut ; une 3e seulement si justifiée.
- **Un seul point focal fort** par écran. Retenue partout ailleurs.
- **La matière avant la couleur** : ce qui rend un site premium, c'est la
  qualité des surfaces (grain, verre, métal, lumière), pas le nombre de teintes.
- Typo : hiérarchie nette, souvent fine et aérée, espace négatif généreux.
- Chaque projet contient **une idée signature** que personne d'autre n'a.

Registre par défaut (si l'univers client est compatible ou indéfini) :
**dark premium** — fond noir/ardoise profond, matière réfléchissante
(chrome, verre, or), glow contrôlé, typo fine claire. Voir
`references/aesthetic.md` pour le détail complet.

Si le client a un univers fort (clair, coloré, institutionnel) : la méthode
s'applique, le registre suit le client. La signature est une voix, pas un
uniforme — l'interdit #2 s'applique aussi à Orphic lui-même.

## 6. Workflow projet — qui juge quoi

Pipeline en 6 phases. Règle de gouvernance : **Sacha juge le goût, la machine
mesure le mesurable.** Ne jamais inverser.

1. **Cadrage client** (humain) — brief complet : objectifs, cibles, concurrents,
   assets, contraintes, ton.
2. **Stratégie + arborescence** (conversation) — pages, sections, textes.
3. **Recherche de DA** (boucle créative, Sacha juge) — premières maquettes
   nourries par ce skill. Itérer TANT QUE la DA ne convient pas. Jamais
   d'autonomie ici.
4. **Raffinement** section par section, composant par composant — animations,
   textes (1re passe). Sacha juge toujours.
5. **Check général** — 1re passe qualité sur tout le site.
6. **Optimisation** page par page (vitesse, SEO) — phase mesurable, agent
   autorisé, MAIS sous zones protégées (voir §7).

## 7. Zones protégées (pour toute optimisation automatisée)

Quand un agent ou une passe d'optimisation intervient (phase 6), la DA validée
en phase 3-4 est **intouchable** :

- Ne pas supprimer/simplifier une animation validée ; proposer une alternative
  au même effet visuel si elle coûte trop cher, et demander validation.
- Ne pas compresser une image/texture au point de tuer la matière.
- Ne pas remplacer une police, une couleur, un easing validés.
- Optimiser AUTOUR de la DA (code, chargement, ordre, cache, formats),
  jamais DEDANS sans validation humaine.

## 8. Boucle de critique obligatoire

Aucune maquette ne part sans au moins **une passe de critique** contre ce skill.
Protocole complet dans `references/critique.md`. Version courte : **faits
d'abord (scripts), jugement ensuite (grilles)** → corriger → re-livrer. 2-3 passes.

Principe de division du travail : **le code pour les faits, le langage pour le
jugement.** Tout ce qui peut se vérifier par un `if` passe par `scripts/`
(déterministe, fiable, pas de variance). Le LLM ne se prononce que sur ce que
lui seul sait évaluer : singularité, intention, matière, goût.

| Script | Vérifie | Quand |
|---|---|---|
| `scripts/check_contrast.py fg bg [--large]` | Ratio WCAG AA/AAA (interdit #3) | Chaque couple texte/fond de la maquette |
| `scripts/audit_page.py URL` | SEO de base, nb polices, couleurs CSS, reduced-motion, alt, libs, poids | Phase 5 et avant toute livraison d'une page en ligne |
| `scripts/check_perf_budget.py URL [mobile\|desktop]` | LCP/CLS/INP réels vs budgets (interdit #4), via PageSpeed | Phase 6 ; lent (20-60 s), lancer en fin de passe |
| `scripts/check_glb.py fichier.glb [--hero]` | Taille, triangles, Draco vs budgets 3D | Chaque export Blender→web (N3 pré-rendu, N4 temps réel) |

## 9. Annexes — quand lire quoi

| Fichier | Lire quand |
|---|---|
| `references/aesthetic.md` | Définir ou évaluer une DA, choisir palette/matière/typo |
| `references/sites.md` | Chercher une référence, positionner un projet, argumenter un choix |
| `references/stack.md` | Choisir une lib d'animation/3D, arbitrer une techno |
| `references/3d-pipeline.md` | Tout projet N2-N4 : 3D perçue, pré-rendu, temps réel, shaders, budgets |
| `references/critique.md` | Avant CHAQUE livraison de maquette ; construire un prompt de critique |
