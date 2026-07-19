# Boucle de critique Orphic — protocole obligatoire

Aucune maquette ne part sans au moins une passe complète. C'est la boucle
qui sépare "correct" de "signature". 2-3 itérations par livrable.

## Le protocole

0. **Faits d'abord (scripts, zéro jugement)** — lancer ce qui s'applique :
   `check_contrast.py` sur chaque couple texte/fond, `audit_page.py` si la
   page est en ligne, `check_glb.py` sur chaque asset 3D,
   `check_perf_budget.py` en phase d'optimisation. Un FAIL script = correction
   obligatoire AVANT la critique de goût. Ne jamais demander au LLM
   d'estimer ce qu'un script peut mesurer.
1. **Générer** la maquette/section selon le brief + ce skill.
2. **Critiquer** — passe séparée, regard froid, contre les 4 grilles
   ci-dessous. Écrire la critique explicitement (pas de correction
   silencieuse : Sacha veut comprendre ce qui clochait).
3. **Corriger** en répondant point par point à la critique.
4. **Répéter** jusqu'à ce que la grille passe, puis livrer à Sacha
   (juge final du goût).

## Grille 1 — Les 4 interdits

- [ ] Y a-t-il du mouvement, et chaque animation a-t-elle une intention
      nommable (révéler / guider / matérialiser) ? Ce qui est purement
      décoratif dégage.
- [ ] **Quelle est l'idée que personne d'autre n'a ?** Si la réponse est
      "le style dark/glow", c'est un template — recommencer. Il faut un
      concept, une matière custom ou un détail propre à CE client.
- [ ] Contrastes lisibles (viser AA), cibles ≥ 44px, navigation évidente,
      focus visibles, `prefers-reduced-motion` prévu ?
- [ ] Budget perf tenable ? (LCP < 2,5 s, INP < 200 ms, CLS < 0,1 ;
      budgets 3D de 3d-pipeline.md si N2-N4)

## Grille 2 — La signature

- [ ] Palette : 2 couleurs ? La 3e est-elle argumentée ?
- [ ] Un seul point focal fort par écran ?
- [ ] La matière est-elle travaillée (grain, lumière, surface) ou est-ce
      des aplats plats ?
- [ ] Typo : hiérarchie nette, max 2 familles, contrastes de taille marqués ?
- [ ] Espace négatif généreux ou écran saturé ?

## Grille 3 — Positionnement contre les références

Poser la maquette face aux pôles (references/sites.md) :
- De quel pôle est-elle la plus proche ? Est-ce voulu ?
- Qu'est-ce que Lusion dirait ? (*"ça ressemble à ce que tout le monde fait"*
  = échec)
- Qu'est-ce qu'Akaru dirait ? (technique justifiée par le projet, ou
  démonstration de force ?)
- Niveau technique choisi (N1-N4) : est-il justifié par budget/délai/intention,
  ou par envie de montrer ?
- Trop proche d'une réf (fournie par le client ou de la banque) ? Une réf
  donne des ingrédients, jamais un modèle — recombiner ou recommencer.

## Grille 4 — Intention (selon l'axe du projet)

- **Produit/e-commerce** : le chemin d'achat est-il visible à chaque instant ?
  Un utilisateur pressé peut-il acheter sans subir l'expérience ?
- **Univers/récit** : le loader pose-t-il le ton ? Les transitions
  racontent-elles ? Y a-t-il des détails qui incarnent (leçon Gatt) ?
- **Vitrine** : est-ce mémorable en 5 secondes ? Screenshot-test : un écran
  pris au hasard donne-t-il envie ?

## Questions de critique types (à poser telles quelles)

- "Où est l'idée singulière ? Nomme-la en une phrase."
- "Qu'est-ce qui fait template ici ? Sois impitoyable."
- "Quelle animation n'a pas d'intention ? Supprime-la."
- "Où le contraste ou la lisibilité souffrent-ils pour l'esthétique ?"
- "Qu'est-ce qui pèse le plus, et le rendu le justifie-t-il ?"
- "Si Igloo/Lusion/Akaru voyaient ça, que critiqueraient-ils en premier ?"

## Zones protégées — rappel pour la phase d'optimisation

Une fois la DA validée par Sacha, elle devient intouchable pour toute passe
d'optimisation automatisée. L'optimisation travaille sur : code, ordre de
chargement, formats, cache, lazy-loading, minification — jamais sur :
animations validées, matières, couleurs, typos, easings. Toute exception
demande validation humaine explicite avec alternative proposée.

## Rappel de gouvernance

La machine mesure (perf, SEO, accessibilité). **Sacha juge le goût.**
La boucle de critique prépare son jugement, elle ne le remplace jamais.
