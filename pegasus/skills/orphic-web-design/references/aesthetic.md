# Esthétique Orphic — la signature en profondeur

## 1. Le registre par défaut : dark premium

Fond **noir profond ou ardoise** (#0a0a0c → #2d2f36), jamais de blanc clinique
par défaut. Sur ce fond, UNE matière qui capte la lumière :

- **Chrome / métal liquide** — reflets nets, hautes lumières brûlées contrôlées
- **Verre / cristal** — réfraction, aberration chromatique subtile, caustiques
- **Or** — chaleur, luxe, à doser (accent, pas aplat)
- **Givre / minéral** — registre Igloo : froid, mat + brillant

Le fond disparaît, la lumière sculpte. Un seul objet/élément lumineux focal
par écran. Le reste se tait.

## 2. Glow et lumière

- Glow = accent, jamais ambiance générale. Un liseré, un halo derrière le focal,
  une lueur au hover. Si tout brille, rien ne brille.
- Sources de lumière cohérentes : si l'objet est éclairé de gauche, les ombres
  portées et reflets UI suivent.
- Éviter le glow multicolore RGB "gamer" sauf univers client assumé
  (esports, gaming, nightlife).

## 3. Palette

- **2 couleurs par défaut.** Preuve par les références : Igloo (#b6bac5/#383e4e),
  Lusion (noir/blanc), Organimo (#e7e6f0/#2d2f36), Basement (#FF4D00/noir),
  Editorial New (noir/blanc). La retenue chromatique fait le luxe.
- 3e couleur = décision argumentée (accent CTA, code sémantique), jamais décor.
- Les dégradés animés type Stripe = registre **corporate tech**, pas luxe.
  Pour le luxe : matières nobles en shader (or liquide, soie, marbre) plutôt
  que dégradés colorés.

## 4. Typographie

- Hiérarchie nette : 1 display fort + 1 texte lisible suffisent.
- Registre Orphic : fines, aérées, tracking généreux sur les capitales,
  contrastes de taille marqués (display énorme / labels minuscules).
- La typo peut être LE spectacle (Editorial New, Basement Foundry) : typo
  variable animée, SplitType au caractère, typo en shader (registre Igloo).
- Interdit : plus de 2 familles ; graisses multiples sans logique.

## 5. Les deux minimalismes Orphic

Deux registres valides, même philosophie (la retenue) :

| | Sombre-dramatique | Clair-épuré |
|---|---|---|
| Référence | Images signature (chevaux chrome/or), Igloo, Gatt | Kalinsky |
| Fond | Noir/ardoise | Blanc cassé/gris chaud |
| Force | Matière + lumière | Espace + précision |
| Pour | Luxe, production, cinéma, nightlife, tech premium | Corporate élégant, éditorial, portfolio sobre |

Le choix se fait en phase 3 selon l'univers client. Ne jamais mélanger les
deux registres dans un même site sans concept fort (ex. duality noir/blanc
de Baillat par Locomotive — mais c'est LE concept du site, pas un accident).

## 6. Pièges connus de ce registre

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

La DA web Orphic et la DA 3D d'Orphic Production sont LE MÊME univers :
objet-matière sur fond noir, une source lumineuse qui sculpte, contraste
extrême. Les packshots Blender (lentille cinéma, showroom nocturne) sont la
banque d'assets et de références internes. Tout projet niveau 2-3 doit
puiser dans cette continuité : le site est la version temps réel du packshot.
