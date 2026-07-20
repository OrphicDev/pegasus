-- Pegasus — rapports quotidiens (SEO / Performance / Sécurité / Audience)
-- Chaque site (plugin) pousse son rapport du jour à 18 h (Europe/Paris) avec la
-- clé publishable. Modèle append-only, comme la table `sites` : insertion seule
-- pour anon/authenticated, lecture réservée au service_role (Olympus).

create table if not exists public.reports (
  id         bigint generated always as identity primary key,
  site_url   text not null,
  day        date not null,
  seo        jsonb,
  perf       jsonb,
  secu       jsonb,
  audience   jsonb,
  created_at timestamptz not null default now()
);

alter table public.reports enable row level security;

revoke all on public.reports from anon, authenticated;
grant insert on public.reports to anon, authenticated;
grant all on public.reports to service_role;

drop policy if exists "insert reports" on public.reports;
create policy "insert reports" on public.reports
  for insert to anon, authenticated
  with check (true);

create index if not exists reports_site_day on public.reports (site_url, day desc);
