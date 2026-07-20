---
description: Rapport client prêt à envoyer pour un site géré par Pegasus
---

Génère le rapport client Orphic pour « $ARGUMENTS » (nom du client ou du
site, éventuellement suivi d'une période — ex. « emotionsarts juin 2026 »).

Si aucun client n'est précisé : appelle `pegasus_list_clients` et demande
pour lequel produire le rapport (et sur quelle période, si pertinent).

Délègue l'exécution à l'agent **orphic-reporting** : collecte des faits
via `pegasus_health`, `pegasus_inspect`, `pegasus_seo_audit` et
`pegasus_list_content`, puis rédaction du rapport en français, vulgarisé
pour un client non technique (ce qui a été fait / santé du site / Google +
actions concrètes / recommandations d'évolution N1-N4). Transmets-lui le
client, la période, et tout contexte utile de la conversation — en
particulier les travaux récents effectués sur ce site, que les outils ne
voient pas toujours.

Au retour, présente à Sacha :
1. le rapport client tel quel — bloc markdown prêt à copier et envoyer ;
2. la note interne éventuelle (corrections faisables via Pegasus) —
   séparée, jamais mélangée au rapport client.

Règles absolues : le rapport ne part jamais tout seul — Sacha relit,
ajuste et envoie lui-même. Aucune donnée inventée : ce que les outils ne
mesurent pas (trafic, positions Google…) est annoncé « au prochain
rapport », jamais estimé.
