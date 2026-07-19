---
description: Boucle de critique Orphic sur une maquette, une page ou un asset 3D
---

Lance la boucle de critique Orphic sur « $ARGUMENTS » (URL, chemin de fichiers
d'une maquette, ou fichier .glb).

Si aucune cible n'est précisée : demande laquelle critiquer (et si le contexte
de la conversation contient une maquette en cours, propose-la).

Délègue l'exécution à l'agent **orphic-critique** (protocole complet dans
`skills/orphic-web-design/references/critique.md` : scripts d'abord — faits,
zéro jugement — puis les 4 grilles). Transmets-lui la cible, le niveau
technique visé (N1-N4) et l'axe d'intention (vitrine / produit / univers)
s'ils sont connus de la conversation.

Au retour, présente la critique telle quelle à Sacha — les FAIL scripts en
premier, puis les verdicts de grilles, l'idée singulière (ou son absence),
et les corrections priorisées. Ne corrige rien sans son accord : **Sacha juge
le goût, la machine mesure le mesurable.**
