# Esthétique Orphic — la signature en profondeur

## 1. Les registres Orphic — aucun par défaut

La signature est une **méthode** (retenue, mono-focal, matière, hiérarchie
typo, palette 2 couleurs, une idée singulière) qui s'exécute dans un
**registre choisi selon le client** (croisement business × niveau ×
registre, SKILL.md §7) — jamais par goût personnel. Quatre registres à
égalité :

| Registre | Référence | Fond | Force | Pour |
|---|---|---|---|---|
| **Sombre-dramatique** | Images signature (chevaux chrome/or), Igloo, Gatt | Noir/ardoise | Matière + lumière | Luxe, production, cinéma, nightlife, tech premium |
| **Clair-épuré** | Kalinsky | Blanc cassé/gris chaud | Espace + précision | Corporate élégant, éditorial, portfolio sobre |
| **Chaleureux-ludique** | Trionn | Teintes chaudes assumées | Personnalité + micro-interactions partout | Marques vivantes, restauration, événementiel |
| **Clair-conversion** | Emotions Arts (projet Orphic) | Clair chaleureux | Séduction au service du CTA | Vitrine + devis/vente, spectacle, artisanat |

Ne jamais mélanger deux registres dans un même site sans concept fort
(ex. duality noir/blanc de Baillat par Locomotive — mais c'est LE concept
du site, pas un accident).

## 2. Le sombre-dramatique en détail

Le goût personnel de Sacha et le pont direct avec l'univers Blender/packshots
d'Orphic Production — le registre le plus documenté ici, PAS le défaut.

Fond **noir profond ou ardoise** (#0a0a0c → #2d2f36), jamais de blanc
clinique. Sur ce fond, UNE matière qui capte la lumière :

- **Chrome / métal liquide** — reflets nets, hautes lumières brûlées contrôlées
- **Verre / cristal** — réfraction, aberration chromatique subtile, caustiques
- **Or** — chaleur, luxe, à doser (accent, pas aplat)
- **Givre / minéral** — registre Igloo : froid, mat + brillant

Le fond disparaît, la lumière sculpte. Un seul objet/élément lumineux focal
par écran. Le reste se tait.

## 3. Glow et lumière

- Glow = accent, jamais ambiance générale. Un liseré, un halo derrière le focal,
  une lueur au hover. Si tout brille, rien ne brille.
- Sources de lumière cohérentes : si l'objet est éclairé de gauche, les ombres
  portées et reflets UI suivent.
- Éviter le glow multicolore RGB "gamer" sauf univers client assumé
  (esports, gaming, nightlife).

## 4. Palette

- **2 couleurs par défaut.** Preuve par les références : Igloo (#b6bac5/#383e4e),
  Lusion (noir/blanc), Organimo (#e7e6f0/#2d2f36), Basement (#FF4D00/noir),
  Editorial New (noir/blanc). La retenue chromatique fait le luxe.
- 3e couleur = décision argumentée (accent CTA, code sémantique), jamais décor.
- Les dégradés animés type Stripe = registre **corporate tech**, pas luxe.
  Pour le luxe : matières nobles en shader (or liquide, soie, marbre) plutôt
  que dégradés colorés.

## 5. Typographie

- Hiérarchie nette : 1 display fort + 1 texte lisible suffisent.
- Registre Orphic : fines, aérées, tracking généreux sur les capitales,
  contrastes de taille marqués (display énorme / labels minuscules).
- La typo peut être LE spectacle (Editorial New, Basement Foundry) : typo
  variable animée, SplitType au caractère, typo en shader (registre Igloo).
- Interdit : plus de 2 familles ; graisses multiples sans logique.

## 6. Pièges connus (surtout en registre sombre)

- **Neumorphism** : magnifique en shot Dribbble, illisible en usage (contrastes
  trop faibles). S'inspirer de la matière (surfaces extrudées, ombres douces)
  mais garantir des contrastes utilisables et des états interactifs évidents.
  Interdit #3 prime.
- **Dark-mode générique** : fond noir + cartes grises + glow violet = déjà un
  template Pinterest. La signature se joue dans la matière custom (shader
  propre au projet), le concept, le détail que personne d'autre n'a.
- **Tout-glow** : réserver au focal.
- **Shots vs sites** : les références d'ambiance (Pinterest/Dribbble) montrent
  une direction, pas une exécution. Toujours re-valider en conditions réelles
  (responsive, perf, accessibilité).

## 7. Le pont Blender ↔ Web

En registre sombre-dramatique, la DA web Orphic et la DA 3D d'Orphic
Production sont LE MÊME univers :
objet-matière sur fond noir, une source lumineuse qui sculpte, contraste
extrême. Les packshots Blender (lentille cinéma, showroom nocturne) sont la
banque d'assets et de références internes. Tout projet niveau 2-3 doit
puiser dans cette continuité : le site est la version temps réel du packshot.
