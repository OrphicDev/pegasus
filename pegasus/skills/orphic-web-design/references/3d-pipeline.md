# Pipeline 3D Orphic — de Blender au navigateur

À lire pour tout projet N2-N4 (3D perçue, pré-rendu ou temps réel). L'avantage compétitif d'Orphic : la
production d'assets 3D de qualité (Blender) est déjà le métier quotidien.
Ce pipeline transforme cet avantage en sites.

## 0. Obtenir de la "3D" — l'arbre de décision

La sensation 3D/wow ne nécessite PAS toujours une scène 3D temps réel. Du plus
léger au plus lourd :

| Technique | 3D réelle ? | Blender ? | Niveau | Outils |
|---|---|---|---|---|
| CSS 3D + parallax | Non (illusion) | Non | N2 | perspective, preserve-3d, translateZ, Atropos |
| SVG animé | Non (2D) | Non | N2 | GSAP, MorphSVG, masques |
| Shaders sur plans 2D | Non (plans plats) | Non | N2 | Curtains.js, PixiJS, R3F plane+shader |
| Vidéo / séquence scrubée | Oui, **pré-rendue** | Oui | N3 | Blender→PNG/mp4, scrub GSAP |
| Scène temps réel | Oui, temps réel | Oui | N4 | Blender→glTF→R3F/Three |

Les deux questions qui tranchent :
1. **Faut-il une matière/un objet impossible sans modélisation ?**
   Non → rester en N2 (CSS/SVG/shaders). Oui → Blender → N3 ou N4.
2. **L'utilisateur doit-il manipuler l'objet librement ?**
   Non (chemin figé, scroll) → **N3 pré-rendu** (plus beau, moins cher).
   Oui (orbite libre) → **N4 temps réel**.

## 0bis. Workflow N3 — la 3D pré-rendue (Blender → scrub)

Le meilleur rapport qualité/coût/perf pour un objet héros non-interactif.
Principe : le GPU du visiteur ne calcule RIEN, il affiche des images.

1. **Modéliser + animer** dans Blender le parcours voulu (rotation, dévoilement,
   caméra qui tourne autour de l'objet).
2. **Rendre en séquence** : PNG (transparence possible) ou mp4. Qualité illimitée
   — ray-tracing, matière parfaite, post-processing DaVinci si besoin.
   30-60 frames pour un tour complet suffit souvent.
3. **Optimiser** : WebP/AVIF aux dimensions écran, ou vidéo mp4/webm compressée.
   Budget : viser < 3-5 Mo pour toute la séquence.
4. **Scrub au scroll** : GSAP ScrollTrigger mappe la progression scroll sur
   l'index de frame (canvas) ou sur `currentTime` d'une balise vidéo.
   Précharger toutes les frames avant activation.
5. **Fallback** : première frame fixe si mobile faible ou `prefers-reduced-motion`.

Avantages : rendu parfait, runtime quasi nul, pas de budget triangles/GPU.
Limite : parcours figé → si besoin d'orbite, passer N4.

## 1. Le pattern "scène persistante" (modèle Orphic Production)

Concept : UNE scène 3D continue, pas une scène par page.
- La **home** tourne autour d'un objet central (ex. la lentille cinéma).
- Chaque **page** = une position/cible de caméra dans la scène.
- Chaque **section** = un push-in de caméra sur un sous-objet de la zone.
- Le **scroll pilote la caméra** le long d'un chemin défini.
- Navigation = mouvement de caméra, jamais rechargement.

Implémentation de référence : R3F + **Theatre.js** (chemin de caméra et
keyframes séquencés visuellement) + GSAP ScrollTrigger + Lenis (le scroll
drive la progression Theatre). Références : Igloo (caméra qui dérive),
Musée (scroll snapping + springs).

## 2. Pipeline d'assets Blender → Web

1. **Modélisation** Blender (packshots, showroom — assets existants Orphic).
2. **Optimisation** : decimate/retopo vers budgets temps réel (voir §4).
   Les objets héros modélisés en millions de polys pour le render NE
   passent PAS tels quels.
3. **UV + bake** : matériaux procéduraux Blender (marbre, cuir, métal) →
   bake en textures (basecolor, roughness, metallic, normal). Le procédural
   Blender ne s'exporte pas en glTF.
4. **Export glTF/.glb** : compression **Draco** (géométrie) + textures
   **KTX2/Basis** (GPU-compressed). Outil : gltf-transform.
5. **Import R3F** : useGLTF + Drei. Ce que le glTF ne porte pas (verre
   réaliste, glow, aberration) → shaders custom côté web.

## 3. Shaders — le vrai levier créatif

Ce qui sépare un site 3D générique (modèle qui tourne) d'un Igloo :
- **Matière custom en GLSL** : verre avec réfraction/dispersion, métal
  liquide, or, givre, soie. Fragment shaders sur les matériaux héros.
- **Shaders sur surfaces 2D** (niveau 1) : displacement au hover sur images,
  transitions matiérées, typo en shader. Outils : Curtains.js, PixiJS,
  R3F plane + shaderMaterial.
- **Post-processing** (EffectComposer / @react-three/postprocessing) :
  bloom (contrôlé), chromatic aberration (subtile), depth of field, grain.
  Le post-processing donne la sensation "cinéma" — c'est la continuité
  directe du travail DaVinci d'Orphic Production.
- Précompiler les shaders au chargement (warm-up) pour éviter les janks
  à la première apparition.

## 4. Budgets perf 3D (durs — interdit #4)

| Poste | Budget |
|---|---|
| Objet héros | ≤ 150k triangles (viser moins) |
| Scène complète visible | ≤ 500k triangles |
| Textures | ≤ 2K par map, KTX2 ; 4K uniquement sur le héros si indispensable |
| .glb initial | ≤ 8 Mo compressé ; le reste en streaming |
| Framerate | 60 fps desktop ; 30 fps minimum mobile sinon fallback |
| DPR | clamp à 1.5–2 (jamais le devicePixelRatio brut des Retina) |
| Lights temps réel | ≤ 3 ; le reste en baked/IBL (HDRI) |

Vérification automatique : `scripts/check_glb.py <fichier.glb> [--hero]`
valide taille, triangles et présence Draco contre ces budgets. À lancer
sur CHAQUE export avant intégration.

Techniques obligatoires : lazy-load des scènes hors viewport, instancing
pour les répétitions, frustum culling actif, `<Detailed>` (LOD) sur les
objets lourds, suspense + placeholder pendant le chargement (jamais un
canvas noir qui freeze).

## 5. Chargement — la leçon Igloo

Sur un site 3D, le chargement fait partie de la DA :
- **Loader = première scène** : il pose le ton (leçon Gatt), il n'est pas
  une barre de progression générique.
- Précharger pendant le loader : géométrie critique, textures du premier
  écran, compilation shaders.
- Streaming progressif du reste pendant que l'utilisateur explore.

## 6. Fallbacks obligatoires

- **Mobile faible** : détecter (GPU tier) → servir une version niveau 1
  (images + shaders légers) ou une capture vidéo de la scène.
- **`prefers-reduced-motion`** : caméra statique, transitions en fondu,
  pas d'auto-rotation.
- **WebGL indisponible** : version image complète et navigable. Le contenu
  reste accessible à 100% sans 3D (interdit #3).
