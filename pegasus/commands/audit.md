---
description: Audit SEO complet d'un site géré par Pegasus
---

Lance un audit SEO du site Pegasus « $ARGUMENTS » avec l'outil `pegasus_seo_audit`.

Si aucun site n'est précisé, appelle d'abord `pegasus_list_clients` et demande lequel auditer.

Ensuite, présente les résultats de façon lisible : ce qui va bien, puis les problèmes classés par priorité (title/meta description manquants ou trop longs, H1, canonical, Open Graph, images sans alt, langue, sitemap/robots), avec pour chacun une recommandation concrète. Propose de corriger les points faisables directement via Pegasus (`pegasus_seo_set`, `pegasus_seo_site`).
