-- ════════════════════════════════════════════════════════════════
-- PEGASUS — Sauvegardes de sites (filet de sécurité / retour arrière)
-- (à coller dans Supabase → SQL Editor du projet Pegasus ; ré-exécutable)
-- ════════════════════════════════════════════════════════════════
-- Chaque déploiement (ou sauvegarde manuelle) enregistre un snapshot du site :
-- structure (thème, extensions, permaliens…), contenus (pages/articles) et la
-- page d'accueil rendue. Permet de REVENIR EN ARRIÈRE si un site casse.
-- NB : ce n'est pas un miroir fichiers complet (Pegasus n'a pas d'accès FTP),
-- mais assez pour restaurer contenu + thème via les outils Pegasus.

create table if not exists public.site_backups (
  id         bigint generated always as identity primary key,
  site_key   text not null,                    -- clé du site (ex : emotions-arts)
  label      text,
  kind       text not null default 'manual',   -- manual | pre-push | post-push
  structure  jsonb,                            -- health + inspect
  content    jsonb,                            -- contenus (pages/articles)
  home_html  text,                             -- page d'accueil rendue
  note       text,
  created_at timestamptz not null default now()
);
create index if not exists site_backups_key_idx on public.site_backups (site_key, created_at desc);

alter table public.site_backups enable row level security;

-- Lecture/écriture réservées à la clé service (portée par la clé d'équipe).
revoke all on public.site_backups from anon, authenticated;
grant all on public.site_backups to service_role;
