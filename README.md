# Pegasus 🦄 — outil interne Orphic Agency

Gérer les sites WordPress des clients d'Orphic **directement depuis Claude Code** — contenus, thèmes, plugins, SEO, médias, multilingue — **sans FTP ni accès hébergeur**.

Ce dépôt est une **marketplace de plugin Claude Code**. Pegasus s'installe en deux commandes dans l'app Claude Code, sans toucher au terminal.

---

## 🚀 Installer (app Claude Code desktop — sans terminal)

1. Barre latérale → **Personnaliser** → **Plugins** → bouton **Ajouter** → **Ajouter une marketplace** → coller `OrphicDev/pegasus` → valider.
2. Dans la liste (onglet marketplace **orphic**), cliquer **+** sur **Pegasus** → **Installer** (scope *User*).
3. Dans le chat, taper `/pegasus:installer` → **coller la clé d'équipe** (fournie par l'admin) → **redémarrer Claude Code**.

C'est tout. Vous avez maintenant :
- les outils `pegasus_*` (Claude peut piloter les sites)
- les commandes `/pegasus:sites`, `/pegasus:audit`, `/pegasus:connecter`, `/pegasus:installer`

> Prérequis : Node.js (déjà là si vous avez Claude Code). Le serveur MCP est **sans aucune dépendance** — rien à installer.
>
> **En terminal (CLI)** : `/plugin marketplace add OrphicDev/pegasus` puis `/plugin install pegasus@orphic` fonctionnent aussi.

---

## 🔌 Connecter un site client

```
/pegasus:connecter
```

Guide pas à pas : installer le zip du plugin WordPress (fourni avec Pegasus) sur le site du client, puis cliquer **« Connecter ce site à Claude »** dans le wp-admin. Le mot de passe est créé, chiffré et enregistré tout seul — aucun copier-coller.

---

## 🔑 Pour l'admin (Sacha) — la clé d'équipe

La clé d'équipe donne accès au registre Supabase des sites + à la clé de déchiffrement des mots de passe. Générez-la sur votre Mac (celui qui détient les secrets) :

```
node scripts/make-team-key.mjs
```

Partagez le blob affiché **via 1Password** (jamais dans un dépôt, un chat, ou un e-mail). Chaque nouveau dev la colle une fois à l'installation.

---

## 🔒 Sécurité

- **Aucun secret dans ce dépôt** (voir `.gitignore`). Les secrets vivent dans la clé d'équipe (côté dev) et sur le Mac de l'admin.
- Auth par **Application Passwords WordPress natives** ; chaque route du plugin vérifie une capacité WP. **Pas d'écriture de fichiers PHP à distance.**
- Mots de passe des sites **chiffrés RSA-2048** dans Supabase (registre append-only, lecture réservée à la clé service). Clé publique embarquée dans le plugin WP ; clé privée uniquement dans la clé d'équipe.

## 🧱 Architecture

```
OrphicDev/pegasus (ce dépôt = marketplace)
├── .claude-plugin/marketplace.json     ← catalogue
└── pegasus/                            ← le plugin Claude Code
    ├── .claude-plugin/plugin.json      ← manifeste + userConfig (clé d'équipe)
    ├── .mcp.json                       ← lance server.mjs, injecte la clé d'équipe
    ├── server.mjs                      ← serveur MCP (zéro dépendance)
    ├── commands/                       ← /pegasus:sites, :audit, :connecter, :critique
    ├── skills/orphic-web-design/       ← constitution design de l'agence (SKILL.md + références + scripts)
    ├── agents/                         ← orphic-critique, orphic-optimizer
    └── wordpress-plugin/pegasus.zip    ← plugin WP à installer sur les sites clients
```

- **Serveur MCP** (`server.mjs`) : lit le registre Supabase avec la clé service, déchiffre les mots de passe avec la clé privée (toutes deux dans la clé d'équipe), et signe les appels à l'API Pegasus de chaque site. Claude ne voit jamais les mots de passe.
- **Plugin WordPress** (`wordpress-plugin/`) : expose l'API REST `pegasus/v1` sur le site du client + un back-office (statut, bouton de connexion). Installé une fois par site.
- **Supabase** : registre central des sites (table `sites`, chiffrée).

## 🛠️ Outils disponibles

`list_clients`, `health`, `inspect`, `diagnostic`, `list_themes`, `install_theme`, `activate_theme`, `install_plugin`, `activate_plugin`, `seo_audit`, `seo_set`, `seo_site`, `upload_media`, `list_content`, `get_content`, `update_content`.

## 🎨 Design — skill `orphic-web-design`, bibliothèque vivante + agents

Depuis la v0.4.0, le plugin embarque la **constitution design web d'Orphic** :

- **`skills/orphic-web-design/`** — la doctrine : règle-mère, 4 interdits,
  offre à 4 niveaux (Premium → Ultra luxe, frontière « Blender ou pas Blender »),
  signature = une méthode (aucun registre par défaut — 4 registres à égalité),
  références = des ingrédients à recombiner, cadrage en 2 étapes (le QUOI puis
  le COMMENT, croisement business × niveau × registre), zones protégées, boucle
  de critique. Références (`aesthetic`, `sites`, `secteurs` Monaco/Riviera,
  `stack`, `3d-pipeline`, `critique`) + 5 scripts de mesure (contraste WCAG,
  audit de page, audit groupé de refs, budgets perf PageSpeed, budgets .glb).
  Le skill se déclenche automatiquement dès qu'une conversation touche au
  design web.
- **Agent `orphic-critique`** — boucle de critique obligatoire avant chaque
  livraison : scripts d'abord (faits), puis les 4 grilles (jugement). Il
  critique, il ne corrige jamais. Entrée directe : `/pegasus:critique <cible>`.
- **Agent `orphic-optimizer`** — phase d'optimisation uniquement (vitesse +
  SEO) sur une DA déjà validée, sous **zones protégées** : il optimise autour
  de la DA, jamais dedans.

Gouvernance : **Sacha juge le goût, la machine mesure le mesurable.**
L'agent optimise sous contrainte ; il ne crée jamais de design en autonomie
(l'autonomie est l'ennemie de la singularité).

### Méthode stable / données vivantes — la bibliothèque Orphic

Le skill (fichiers, versionné git, distribué par la marketplace) porte la
**méthode** — elle bouge rarement. Les **données** — références de sites,
animations validées, fiches secteurs, issues de la veille quotidienne des
devs — vivent dans **Supabase** via 3 outils MCP :

- `pegasus_get_references` — chercher (kind, niveau, registre, business,
  intention, texte libre ; validées par défaut)
- `pegasus_add_reference` — proposer un **candidat**
- `pegasus_validate_reference` — valider/rejeter (décision humaine uniquement)

Flux : **proposer (candidat) → valider (humain) → vivant pour toute l'agence.**

> **Installation (une fois, admin)** : coller `supabase/references-library.sql`
> dans Supabase → SQL Editor (projet Pegasus). Tant que la table n'existe pas,
> les 3 outils renvoient une erreur explicite ; le skill retombe sur ses .md.

### Feuille de route skills & agents

**Fait (v0.5.0)** :
- `orphic-build` (skill) — construire/mettre à jour un site LOCAL depuis un
  BRIEF.md de wireframe généré par Olympus (fixture du contrat de format dans
  `skills/orphic-build/references/exemple-BRIEF.md`).
- `orphic-monitoring` (agent) + `/pegasus:monitoring` — état du parc, lecture
  seule, un rapport (tableau + 🔴 à traiter + recommandations).
- `orphic-reporting` (agent) + `/pegasus:rapport` — rapport client vulgarisé,
  prêt à envoyer, zéro donnée inventée, recommandations d'évolution N1-N4.

Skills à dériver après le projet pilote : `orphic-motion` (lié à la veille),
`orphic-3d-webgl`, `orphic-perf-seo`, `orphic-monitoring-seo` (surveillance
SEO continue — distincte de l'agent monitoring, qui fait l'état des lieux).
Méthode convenue : un projet client **pilote** avec le skill racine, puis
dérivation depuis les apprentissages.
