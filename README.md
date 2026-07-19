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

## 🎨 Design — skill `orphic-web-design` + agents

Depuis la v0.3.0, le plugin embarque la **constitution design web d'Orphic** :

- **`skills/orphic-web-design/`** — la doctrine complète : règle-mère, 4 interdits,
  offre à 4 niveaux (Premium → Ultra luxe, frontière « Blender ou pas Blender »),
  signature (2 couleurs, matière avant couleur, une idée singulière), workflow en
  6 phases, zones protégées, boucle de critique. Références (`aesthetic`, `sites`,
  `stack`, `3d-pipeline`, `critique`) + 4 scripts de mesure (contraste WCAG,
  audit de page, budgets perf PageSpeed, budgets .glb). Le skill se déclenche
  automatiquement dès qu'une conversation touche au design web.
- **Agent `orphic-critique`** — exécute la boucle de critique obligatoire avant
  chaque livraison : scripts d'abord (faits), puis les 4 grilles (jugement).
  Il critique, il ne corrige jamais. Entrée directe : `/pegasus:critique <cible>`.
- **Agent `orphic-optimizer`** — phase 6 uniquement (vitesse + SEO) sur une DA
  déjà validée, sous le régime des **zones protégées** : il optimise autour de
  la DA, jamais dedans.

Gouvernance : **Sacha juge le goût, la machine mesure le mesurable.**

### Protocole d'évolution du skill : fichiers d'abord

La doctrine évolue **par ce dépôt** (git) : on modifie les fichiers du skill,
on bump la version du plugin, chaque poste récupère la mise à jour via la
marketplace. Avantages : versionné, relisible en diff, distribué par le canal
déjà en place, zéro infra. Supabase/Pegasus reste le registre des **sites**,
pas de la doctrine ; si un jour on veut de la donnée vivante par client
(DA validées, historique de critiques, mesures perf), elle s'ajoutera en
table Supabase à côté — sans rien changer au skill fichiers.
