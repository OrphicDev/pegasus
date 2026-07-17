# Pegasus 🦄 — outil interne Orphic Agency

Gérer les sites WordPress des clients d'Orphic **directement depuis Claude Code** — contenus, thèmes, plugins, SEO, médias, multilingue — **sans FTP ni accès hébergeur**.

Ce dépôt est une **marketplace de plugin Claude Code**. Pegasus s'installe en deux commandes dans l'app Claude Code, sans toucher au terminal.

---

## 🚀 Installer (Claude Code desktop — sans terminal)

Dans l'app Claude Code :

```
/plugin marketplace add OrphicDev/pegasus
/plugin install pegasus@orphic
```

À l'installation, Claude Code demande la **Clé d'équipe Pegasus** → collez celle fournie par l'admin (Sacha), puis **redémarrez Claude Code**.

C'est tout. Vous avez maintenant :
- les outils `pegasus_*` (Claude peut piloter les sites)
- les commandes `/pegasus:sites`, `/pegasus:audit`, `/pegasus:connecter`

> Prérequis : Node.js (déjà là si vous avez Claude Code). Le serveur MCP est **sans aucune dépendance** — rien à installer.

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
    ├── commands/                       ← /pegasus:sites, :audit, :connecter
    └── wordpress-plugin/pegasus.zip    ← plugin WP à installer sur les sites clients
```

- **Serveur MCP** (`server.mjs`) : lit le registre Supabase avec la clé service, déchiffre les mots de passe avec la clé privée (toutes deux dans la clé d'équipe), et signe les appels à l'API Pegasus de chaque site. Claude ne voit jamais les mots de passe.
- **Plugin WordPress** (`wordpress-plugin/`) : expose l'API REST `pegasus/v1` sur le site du client + un back-office (statut, bouton de connexion). Installé une fois par site.
- **Supabase** : registre central des sites (table `sites`, chiffrée).

## 🛠️ Outils disponibles

`list_clients`, `health`, `inspect`, `diagnostic`, `list_themes`, `install_theme`, `activate_theme`, `install_plugin`, `activate_plugin`, `seo_audit`, `seo_set`, `seo_site`, `upload_media`, `list_content`, `get_content`, `update_content`.
