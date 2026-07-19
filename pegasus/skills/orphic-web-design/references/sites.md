# Références Orphic — sites décortiqués

Sélection personnelle de Sacha + refs complémentaires validées. Chaque projet
doit pouvoir être positionné par rapport à ces pôles.

## Pôles 3D

### Igloo.inc — niveau 2, luxe froid minéral
- Par Abeto × Bureaux. Full WebGL : cristaux procéduraux, texte UI en shader,
  footer particules (données VDB converties navigateur).
- Stack : Three.js, three-mesh-bvh, Svelte, GSAP, Vite, vanilla JS.
  Assets : Houdini + Blender.
- Palette 2 couleurs : #b6bac5 / #383e4e.
- Leçons : (1) previs en grey-box avant exécution ; (2) obsession chargement —
  exporteurs custom, shaders précompilés ; sur du full-WebGL, la perf EST le
  design ; (3) caméra qui dérive entre objets encapsulés = navigation.

### Active Theory (activetheory.net) — niveau 3, immersif néon
- Studio Venice Beach, pionniers WebGL depuis 2012. Environnements 3D
  navigables (bureaux LA/Amsterdam), néons, framework maison **Hydra**
  (moteur 3D + GUI visuelle pour les designers).
- Leçon : le niveau 3 exige un outillage industriel. Ne pas s'y engager
  sans pipeline solide.

### Musée (musee.barvian.me) — niveau 2, la 3D "raisonnable"
- Maxwell Barvian, design Kevin Pham. **React Three Fiber + Framer Motion
  (useScroll/useSpring) + CSS scroll snapping.** Repo public : github.com/barvian/musee.
- Leçon : le niveau de finition atteignable en R3F déclaratif, maintenable,
  intégrable Next.js. Modèle réaliste pour 80% des projets 3D clients.

### Organimo (organimo.com) — niveau 2, e-commerce narratif
- Unseen Studio, SOTD. Monde surréaliste au scroll pour vendre un complément
  (sea moss). **WooCommerce** derrière. Palette #e7e6f0 / #2d2f36.
- Leçon : immersion AU SERVICE du tunnel de vente. Chemin d'achat toujours
  lisible. Prouve que WebGL + WordPress/WooCommerce est viable.

## Pôle 3D-surface (niveau 1 — sweet spot Orphic)

### Ryan Ritzenthaler (ryanritzenthaler.com)
- Next.js + Three.js + R3F + GLSL + Prismic. Intention déclarée : *illusion
  d'un site plat 2D, avec l'interactivité de shaders sur des plane geometries*.
- Leçon : LA technique "3D+2D classique" — imprégner une mise en page 2D de
  matière shader, pas coller un modèle 3D dans une page.

### Lusion (lusion.co)
- Studio d'Edan Kwan. Noir/blanc. Clients : Porsche, Google, Max Mara.
- Leçons : (1) assets customisés obtenus quand design et dev travaillent
  ENSEMBLE, pas en relais ; (2) refus des tendances : "on ne produit pas ce
  qui ressemble à tout le monde" — à citer dans toute critique anti-template.

### Akaru (akaru.fr)
- Lyon, 35+ Awwwards. Nuxt 3 + Sanity + Three.js + GLSL + Blender.
  WebGL discret au service d'un site qui RESSENT éditorial.
- Leçons fondatrices (citations) : *"utiliser uniquement les techniques que
  le projet justifie, sans démonstration de force"* ; *"des animations qui
  ne compromettent pas l'utilisabilité mais l'améliorent ; un site rapide
  et efficace était notre objectif."* → C'est la règle-mère incarnée.

## Pôles DA & concept

### Amir Mohseni (amirmohseni.com) — craft art director
- Creative art director (Deveb, Dopegood — SOTD). Le design prime, la
  technique sert. Leçon : même un site 3D s'effondre si typo, espacement,
  hiérarchie sont faibles. Contrepoids au tout-WebGL.

### Michael Gatt (michaelgatt.com) — univers narratif
- Compositeur (film/TV/jeux). Par Synchronized Studio × Zhenya Rynzhuk.
  Nuxt + Vue + WebGL. Loader interactif, about en scroll-storytelling,
  player-equalizer, détails personnels ("Guitar & Backpack").
- Leçon : l'axe "univers/récit" — loader qui pose le ton, transitions qui
  racontent, détails qui incarnent. Modèle pour le futur site Orphic
  Production (storytelling spatial).

### Trionn (trionn.com) — personnalité & micro-interactions partout
- Studio de Sunny Rathod, "AI-powered digital studio". **Next.js + GSAP +
  Three.js** — la stack par défaut Orphic, prouvée au niveau Awwwards.
  Univers de marque total (jungle/tigre) porté par la 3D et le motion.
- Leçons : (1) **aucune zone morte** — menu, footer, 404, hovers : chaque
  point de contact est travaillé, la singularité se joue aussi dans les
  recoins ; (2) un univers de marque peut être ludique et chaleureux —
  complément du registre atmosphérique de Gatt, utile quand le dark premium
  ne convient pas au client ; (3) miroir du positionnement Orphic
  (studio augmenté par l'IA).

### Emotions Arts (emotions-arts.com) — N2 en registre clair, projet Orphic
- Compagnie de spectacle vivant (jumelles De Masi, Monaco). WordPress +
  Elementor + thème custom, **Curtains.js + GSAP + ScrollTrigger + Theatre.js**
  (audité : donc N2, 3D-surface, pas N1 malgré l'apparence éditoriale).
- Polices : Cormorant Garamond + Jost (2 familles, combo serif/sans classe).
  Trilingue FR/EN/IT. `prefers-reduced-motion` présent.
- Leçons : (1) preuve qu'Orphic livre du **N2 en registre clair/chaleureux**,
  hors dark premium — la signature est une méthode, pas un uniforme ;
  (2) intention vitrine+conversion (devis) : le motion sert la séduction et le
  CTA, pas la démonstration technique.

## Pôle N1 Premium (sans 3D)

### Kalinsky (kalinsky.design) — minimalisme clair
- Max Kalinsky, creative designer, **Framer**. Rien de superflu : équilibre,
  alignement, contraste. Leçon : la voie no-code élégante existe pour les
  projets qui ne justifient pas du custom.

### Editorial New (Locomotive × Pangram Pangram)
- CSS/HTML5/GSAP/PHP, zéro WebGL, noir/blanc. Tout le site = une police
  variable mise en scène. Leçon : UNE idée typo poussée à fond suffit
  pour un SOTD.

### Basement Foundry (basement.studio)
- Next.js, orange #FF4D00 / noir. Registre brut-énergique. Leçon : élargit
  le vocabulaire hors des palettes givrées ; typo comme spectacle.

### Locomotive® (locomotive.ca)
- Montréal, 100+ awards. Noir/blanc, grille éditoriale rigoureuse,
  détails maniaques. Leçon (case study Baillat) : navigation minimale +
  usage massif de la typo + concept bichrome = un univers auto-suffisant.
  Modèle du site d'agence intemporel.

## Les 4 interdits — et leurs tensions à arbitrer

1. **Sans animation** → mais l'animation a une intention, sinon elle dégage
   (tension avec #4).
2. **Ressemble aux autres** → vaut aussi pour la signature Orphic appliquée
   mécaniquement. Test : "quelle est l'idée que personne d'autre n'a ici ?"
3. **Pas user-friendly** → neutralise le piège neumorphism ; contrastes AA,
   cibles 44px, focus visibles, `prefers-reduced-motion`.
4. **Lent** → décide du niveau technique. Si le budget perf casse, on descend
   de niveau, on ne livre pas lent.

## Registres non couverts par les goûts de Sacha (à savoir)

- Le combo "ultra-luxe + shader-surface + zéro 3D" est un créneau quasi vide
  sur le marché (vérifié sur Awwwards Luxury). C'est une OPPORTUNITÉ de
  positionnement Orphic : matières nobles en shader (or liquide, soie,
  marbre) sur mise en page luxe. Outils de départ : Paper Shaders
  (shaders.paper.design), Curtains.js, technique mesh-gradient adaptée.
- Référence luxe+WebGL-surface la plus proche identifiée : Julien Calot
  (juliencalot.com, Webflow + WebGL, par FLOT NOIR) — registre artistique
  feutré.
