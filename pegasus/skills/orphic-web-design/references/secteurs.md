# Secteurs Monaco / Riviera — fiches d'ingrédients

Fiches d'**INGRÉDIENTS** par secteur, jamais de modèles : chaque fiche donne
des intentions, registres, matières et pièges à recombiner selon le cadre du
projet (croisement business × niveau × registre, SKILL.md §7). Copier une
fiche telle quelle = template = interdit #2.

Ces fiches démarrent volontairement incomplètes : elles s'enrichissent par
l'usage (protocole d'évolution, SKILL.md §10). Quand un projet apprend
quelque chose sur un secteur, proposer l'ingrédient en candidat dans la
bibliothèque Orphic (`pegasus_add_reference`, kind `secteur`) — validation
humaine avant de le tenir pour acquis. Interroger aussi
`pegasus_get_references` (filtre `business`) : la banque vivante prime sur
ces fiches si elles divergent.

## Luxe (maisons, retail haut de gamme)

- Intention dominante : univers/récit ou vitrine ; l'achat se conclut souvent
  hors ligne — le site vend un monde, pas un panier.
- Niveaux : N2 sweet spot (matière en shader) ; N3 si un objet héros existe.
- Registres : sombre-dramatique ou clair-épuré ; le luxe = la retenue.
- Ingrédients : matières nobles en shader (or liquide, soie, marbre) — le
  créneau "ultra-luxe + shader-surface + zéro 3D" est quasi vide sur le
  marché (voir sites.md, opportunité Orphic). Typo fine, tracking généreux.
- Pièges : glow multicolore, surcharge dorée (l'or = accent, pas aplat),
  vocabulaire "premium" générique.

## Hôtellerie (palaces, boutique-hôtels)

- Intention : produit déguisé en univers — la réservation est le chemin
  d'achat, elle reste visible en permanence (leçon Organimo).
- Niveaux : N1 exécuté parfaitement ou N2 (lumière/matière sur photos).
- Registres : clair-épuré (bord de mer, sobriété) ou chaleureux selon la
  maison ; sombre pour les établissements nocturnes.
- Ingrédients : la photographie porte tout — shaders discrets SUR les photos
  (displacement, lumière) plutôt qu'à côté ; transitions de pages comme un
  déplacement dans l'hôtel.
- Pièges : carrousel générique de chambres, immersion qui cache le bouton
  Réserver, poids des photos non optimisé (interdit #4).

## Casino / nightlife

- Intention : univers/récit — l'excitation, la nuit, la promesse.
- Niveaux : N2-N4 selon budget ; le spectaculaire est attendu ici.
- Registres : sombre-dramatique naturel ; c'est LE secteur où le néon et le
  glow assumés sont légitimes (cf. aesthetic.md — univers client assumé).
- Ingrédients : lumière qui sculpte le noir, particules, reflets ; le loader
  peut poser le ton (leçon Gatt) ; micro-interactions de jeu.
- Pièges : RGB "gamer" sans direction, tout-glow (si tout brille, rien ne
  brille), lisibilité sacrifiée au spectacle (interdit #3).

## Immobilier de luxe

- Intention : produit — chaque bien est une fiche produit à très fort enjeu ;
  le contact/la visite est le CTA.
- Niveaux : N1-N2 ; N3 pré-rendu pour un programme neuf avec objet 3D
  (la maquette de l'immeuble en scroll-scrub).
- Registres : clair-épuré (confiance, précision) ; sombre pour le très haut
  de gamme nocturne (penthouses, skyline).
- Ingrédients : plans, chiffres et surfaces mis en scène typographiquement ;
  parallax mesuré sur les vues ; carte/localisation travaillée comme un
  écran signature.
- Pièges : templates immobiliers (grilles de cards identiques partout),
  photos écrasées par la compression (tuer la matière = interdit).

## Yachting

- Intention : univers/récit (le rêve) + produit (charter/vente, specs).
- Niveaux : N2-N3 ; un yacht est un objet héros parfait pour du pré-rendu
  Blender scrubé au scroll (profil, pont, intérieurs).
- Registres : clair-épuré marin (blanc cassé, précision) ou
  sombre-dramatique (coque de nuit, reflets sur l'eau).
- Ingrédients : la ligne de flottaison comme axe de composition ; matière
  eau/reflets en shader ; specs techniques en typographie display (longueur,
  nœuds — les chiffres comme spectacle).
- Pièges : bleu marine + or cliché nautique, galeries plates sans matière.

## Événementiel

- Intention : vitrine (prouver le savoir-faire) ; chaque événement passé est
  une preuve.
- Niveaux : N1-N2 ; le motion EST la démonstration du métier.
- Registres : chaleureux-ludique ou sombre selon le positionnement
  (mariages vs nightlife corporate).
- Ingrédients : le site se comporte comme un événement — séquencé, rythmé,
  avec des moments ; typo variable animée ; aucune zone morte (leçon
  Trionn : menu, footer, 404 travaillés).
- Pièges : grille de logos clients sans mise en scène, vidéos de fond
  lourdes non compressées.

## Joaillerie / horlogerie

- Intention : produit-objet — TOUT tourne autour de la pièce.
- Niveaux : N3 est le naturel du secteur (la pièce en pré-rendu parfait,
  ray-tracing, scrubée au scroll) ; N4 seulement si la manipulation libre
  est un vrai besoin ; N2 (caustiques, dispersion en shader) en budget serré.
- Registres : sombre-dramatique (écrin noir, lumière qui sculpte) ou
  clair-épuré (blanc galerie).
- Ingrédients : mono-focal absolu — une pièce par écran, le reste se tait ;
  aberration chromatique subtile, caustiques ; l'échelle (macro extrême).
- Pièges : rendre la pièce petite dans la page, multiplier les produits par
  écran, compression qui détruit les reflets.

## Restauration (gastronomie)

- Intention : vitrine + conversion (réserver une table).
- Niveaux : N1 parfaitement exécuté suffit souvent ; N2 pour une signature
  de chef (matière = l'assiette).
- Registres : chaleureux-ludique (convivialité) ou sombre-dramatique
  (gastronomie de nuit, cave) ; clair-conversion pour les maisons de jour.
- Ingrédients : la photographie culinaire en pleine matière ; le menu comme
  objet typographique (pas un PDF) ; réservation accessible en permanence.
- Pièges : PDF de menu, musique auto, immersion qui retarde l'accès aux
  horaires/adresse (l'utilisateur pressé prime — interdit #3).

## Artistes / spectacle vivant

- Intention : univers/récit — le site incarne l'œuvre ; souvent + conversion
  (dates, billets, devis).
- Niveaux : N1-N2 (référence maison : Emotions Arts, N2 clair en
  Curtains+GSAP+Theatre).
- Registres : suit l'univers artistique — clair-conversion (Emotions Arts),
  chaleureux, ou sombre théâtral.
- Ingrédients : le loader pose le ton comme un lever de rideau ; transitions
  qui racontent ; détails qui incarnent la personne (leçon Gatt : le
  "Guitar & Backpack") ; le mouvement scénique traduit en motion web.
- Pièges : agenda/billetterie enfoui, singer l'affiche du spectacle au lieu
  de traduire son mouvement.
