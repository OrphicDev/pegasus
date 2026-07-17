---
description: Configurer Pegasus avec la clé d'équipe (à faire une seule fois, après l'installation)
---

Tu vas enregistrer la **clé d'équipe Pegasus** sur cette machine pour que Pegasus puisse se connecter.

Clé fournie par l'utilisateur : $ARGUMENTS

Procédure :

1. **Récupérer la clé.** Si "$ARGUMENTS" contient déjà un long code (une chaîne base64 de plusieurs milliers de caractères, sans espaces), utilise-le. Sinon, demande à l'utilisateur : « Colle ta clé d'équipe Pegasus (le long code fourni par l'administrateur Orphic) » et attends sa réponse.

2. **Enregistrer la clé** dans le fichier `~/.pegasus/team-key`, en la nettoyant de tout espace/retour à la ligne parasite. Utilise le Bash tool :
   - `mkdir -p ~/.pegasus && chmod 700 ~/.pegasus`
   - écris la clé, telle quelle, dans `~/.pegasus/team-key` (une seule ligne, sans rien ajouter), puis `chmod 600 ~/.pegasus/team-key`
   - vérifie la taille : `wc -c ~/.pegasus/team-key` (doit faire ~2000–3000 caractères)

3. **Ne réaffiche JAMAIS la clé** dans ta réponse. Confirme seulement : « ✅ Clé enregistrée. »

4. **Dis à l'utilisateur** de **fermer complètement Claude Code puis de le rouvrir**. Ensuite, `/sites` (ou « montre mes sites Pegasus ») fonctionnera.

Si aucune clé n'est disponible : explique que l'administrateur Pegasus la génère avec `node scripts/make-team-key.mjs` (dans le dépôt Pegasus) et la partage via 1Password. Sans elle, impossible de continuer.
