---
description: Rapport d'état du parc de sites WordPress gérés par Pegasus
---

Lance le monitoring du parc Pegasus sur « $ARGUMENTS » (un ou plusieurs
sites, ou rien = tout le parc).

Délègue l'exécution à l'agent **orphic-monitoring** : boucle
`pegasus_list_clients` puis, site par site, `pegasus_health`,
`pegasus_diagnostic`, `pegasus_seo_audit`, `pegasus_inspect` — les faits
d'abord, une seule synthèse à la fin. Transmets-lui les sites demandés
et, si Sacha veut la perf, dis-le explicitement (le script perf est lent,
il ne tourne pas par défaut).

Au retour, présente le rapport tel quel : l'en-tête et le tableau du
parc, puis la section « 🔴 à traiter » priorisée, puis les
recommandations. **L'agent observe et rapporte, il ne modifie rien sur
les sites** — pour corriger, propose à Sacha les voies indiquées dans les
recommandations (`/pegasus:audit`, `pegasus_seo_set`, mise à jour
manuelle…) et attends son accord avant toute action.
