# Stack Orphic — quelle lib pour quoi

## Scroll & orchestration (le socle de tout site Orphic)

- **GSAP + ScrollTrigger** — la timeline maître. Toute chorégraphie scroll
  passe par lui.
- **Lenis** — smooth scroll. TOUJOURS câblé avec ScrollTrigger
  (`lenis.on('scroll', ScrollTrigger.update)` + ticker GSAP), jamais en
  parallèle non synchronisé.
- **Barba.js** — transitions de page fluides sur multipage (sensation SPA).
  Sur Next/Nuxt, préférer les transitions natives du framework + GSAP.

## Typographie animée

- **SplitType** — découpe lignes/mots/caractères pour animer au caractère
  (reveals, staggers). Attendre le chargement des fonts avant split.
- **Anime.js** — animations légères ponctuelles hors timeline GSAP.
  Ne pas mélanger GSAP et Anime sur le même élément.

## WebGL / 3D

- **Three.js** — la base. Vanilla pour le full-custom (registre Igloo/Lusion).
- **React Three Fiber + Drei** — la voie par défaut en environnement
  React/Next : déclaratif, maintenable, composable. Le choix "Musée".
- **Theatre.js** — séquenceur visuel : chemins de caméra, keyframes
  synchronisées au scroll. L'outil du pattern "scène persistante" (voir
  3d-pipeline.md).
- **PixiJS** — 2D WebGL : particules, distorsions, effets sur canvas 2D.
- **Curtains.js** — plans WebGL sur images/vidéos DOM (displacement au hover,
  transitions matiérées). L'outil du niveau 1 par excellence.
- **Shery.js** — surcouche prête à l'emploi (image effects, mouse follower).
  ⚠️ Opinionated et reconnaissable : utiliser comme prototype, puis
  customiser les shaders, sinon effet "vu 1000 fois" (interdit #2).
- **Paper Shaders** (@paper-design/shaders-react) — matières prêtes (liquid
  metal, etc.) pour logos/formes. Bon point de départ luxe-surface.

## Motion assets

- **Rive** — dès qu'il y a de l'interactif ou des états (state machines) :
  boutons riches, mascotte réactive, loaders interactifs. Plus léger et
  réactif que Lottie.
- **Lottie** — animations After Effects linéaires, décoratives. Pas
  d'interactivité complexe.
- Règle : interactif/état → Rive ; décoratif linéaire → Lottie.

## Physique & micro-interactions

- **Matter.js** — physique 2D (objets qui tombent, collisions, tas
  d'éléments draggables). Effet signature possible sur un footer ou un 404.
- **Atropos** — parallax 3D au survol de cartes. Doser : une zone, pas
  toutes les cartes du site.

## Règles de décision

1. **WebGL vs CSS/GSAP** : si l'effet est réalisable en CSS/GSAP avec le même
   rendu perçu, PAS de WebGL. Le WebGL se justifie pour : matière (shaders),
   3D réelle, distorsions d'image, particules massives.
2. **Vanilla Three vs R3F** : projet dans un écosystème React/Next → R3F.
   Expérience full-custom hors framework, équipe créa-dev fusionnée → vanilla.
3. **Un seul moteur d'animation DOM** par projet (GSAP par défaut). Anime.js
   seulement en appoint isolé.
4. **Toute lib ajoutée = coût perf justifié.** Vérifier le poids bundle avant
   d'ajouter. Tree-shaking, imports ciblés.

## Stacks par contexte de production

| Contexte | Stack | Quand |
|---|---|---|
| WordPress/OVH (Pegasus) | Child theme + template custom (option C) servant un bundle Vite (Three/GSAP/Lenis) | Sites clients WP existants, WooCommerce |
| Next.js | Next + R3F + Drei + Theatre + GSAP + CMS headless (Sanity/Prismic) | Projets custom premium, back-office lié |
| Framer | Framer + interactions natives | Niveau 0 rapide et élégant, petits budgets |
| Webflow | Webflow + custom code (GSAP, WebGL embarqué) | Client voulant éditer lui-même, N1-N2 |

## Garde-fous perf (rappel, détail dans 3d-pipeline.md)

- Lazy-load de toute scène WebGL hors viewport initial.
- `prefers-reduced-motion` : version calme obligatoire.
- Fallback mobile : image/vidéo si le device ne tient pas 60 fps.
- Fonts : `font-display: swap` + preload des display fonts.
- Mesurer après chaque ajout de lib : LCP < 2,5 s, INP < 200 ms, CLS < 0,1.
