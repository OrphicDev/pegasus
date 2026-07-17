-- ════════════════════════════════════════════════════════════════
-- PEGASUS — registre des sites (VERSION FINALE — à coller dans Supabase → SQL Editor)
-- ════════════════════════════════════════════════════════════════
-- Modèle « append-only », le plus sûr :
--   • Le plugin (clé publique) peut UNIQUEMENT AJOUTER une ligne.
--     Il ne peut ni lire, ni modifier, ni supprimer quoi que ce soit.
--   • Chaque (re)connexion d'un site ajoute une ligne ; ton Mac lit la plus récente.
--   • Les mots de passe arrivent déjà chiffrés (RSA). Seule la clé "secret" (ton Mac) lit.

drop table if exists public.sites;

create table public.sites (
  id               bigint generated always as identity primary key,
  site_url         text not null,
  username         text not null,
  app_password_enc text not null,   -- chiffré RSA (base64)
  label            text,
  created_at       timestamptz default now()
);
create index sites_site_url_idx on public.sites (site_url);

alter table public.sites enable row level security;

-- Public : AJOUT uniquement.
drop policy if exists pegasus_insert on public.sites;
create policy pegasus_insert on public.sites
  for insert to public with check (true);

-- Droits : le public ne reçoit QUE le droit d'insérer (aucune lecture possible).
revoke all on public.sites from anon, authenticated;
grant insert on public.sites to anon, authenticated;
grant all on public.sites to service_role;
