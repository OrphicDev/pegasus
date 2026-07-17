-- ════════════════════════════════════════════════════════════════
-- PEGASUS — Livraison de la clé d'équipe via code d'accès révocable
-- À coller UNE FOIS dans Supabase → SQL Editor (en plus de supabase-setup.sql).
-- ════════════════════════════════════════════════════════════════
-- Principe :
--   • La clé d'équipe (blob) vit dans une table ILLISIBLE côté client (aucune policy RLS).
--   • Chaque collègue a un CODE d'accès (on ne stocke que son hash SHA-256).
--   • L'app Pegasus appelle la fonction get_team_key(code) :
--       - code valide + non révoqué  → renvoie le blob (via TLS)
--       - sinon                      → erreur
--   • Révoquer un collègue = passer son code à revoked = true. Instantané.
-- La fonction est SECURITY DEFINER : elle seule peut lire les tables protégées.
-- (Hash via sha256() natif Postgres — aucune extension requise.)

-- ── Le blob de la clé d'équipe (service_role + clé privée). Jamais lisible côté client.
create table if not exists public.team_config (
  id         int primary key default 1,
  team_key   text not null,
  updated_at timestamptz default now()
);
alter table public.team_config enable row level security;
-- (aucune policy → anon/authenticated ne peuvent RIEN lire directement)
revoke all on public.team_config from anon, authenticated;

-- ── Codes d'accès des collègues (on stocke le hash, jamais le code en clair).
create table if not exists public.access_codes (
  code_hash    text primary key,
  label        text,
  revoked      boolean default false,
  created_at   timestamptz default now(),
  last_used_at timestamptz
);
alter table public.access_codes enable row level security;
revoke all on public.access_codes from anon, authenticated;

-- ── La seule porte d'entrée : valide le code, renvoie le blob.
create or replace function public.get_team_key(p_code text)
returns text
language plpgsql
security definer
set search_path = public
as $$
declare
  v_hash text := encode(sha256(convert_to(p_code, 'UTF8')), 'hex');
  v_key  text;
begin
  if not exists (
    select 1 from public.access_codes
    where code_hash = v_hash and not revoked
  ) then
    raise exception 'Code invalide ou révoqué.';
  end if;

  update public.access_codes set last_used_at = now() where code_hash = v_hash;

  select team_key into v_key from public.team_config where id = 1;
  if v_key is null then
    raise exception 'Clé d''équipe non encore configurée par l''admin.';
  end if;

  return v_key;
end;
$$;

-- Le public peut EXÉCUTER la fonction (mais pas lire les tables sous-jacentes).
revoke all on function public.get_team_key(text) from public;
grant execute on function public.get_team_key(text) to anon, authenticated;
