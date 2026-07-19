-- ════════════════════════════════════════════════════════════════
-- PEGASUS — Bibliothèque Orphic : références vivantes du design
-- (à coller dans Supabase → SQL Editor du projet Pegasus ; ré-exécutable)
-- ════════════════════════════════════════════════════════════════
-- Architecture « méthode stable / données vivantes » : le skill
-- orphic-web-design (fichiers, versionné git) porte la MÉTHODE ; cette
-- table porte les DONNÉES — références de sites, animations validées,
-- fiches secteurs — enrichies au quotidien par la veille de l'équipe.
-- Flux : proposer (candidat) → valider (humain) → vivant pour tous.
-- NB : nom "references_library" (REFERENCES est un mot réservé SQL).

create table if not exists public.references_library (
  id          bigint generated always as identity primary key,
  kind        text not null default 'site',    -- site | animation | matiere | secteur | autre
  titre       text not null,
  url         text,
  niveau      text,                            -- N1 | N2 | N3 | N4
  technique   text,                            -- libs / techniques (ex : "Curtains.js + GSAP")
  intention   text,                            -- vitrine | produit | univers
  registre    text,                            -- sombre-dramatique | clair-epure | chaleureux-ludique | clair-conversion
  business    text,                            -- secteur / type de client (ex : "yachting")
  ingredients text,                            -- ce qu'on en EXTRAIT et recombine (jamais un modèle)
  notes       text,
  statut      text not null default 'candidat',-- candidat | valide | rejete
  auteur      text,
  created_at  timestamptz not null default now()
);
create index if not exists references_library_statut_idx on public.references_library (statut);
create index if not exists references_library_kind_idx   on public.references_library (kind);

alter table public.references_library enable row level security;

-- Aucune policy publique : lecture ET écriture réservées à la clé service
-- (portée par la clé d'équipe, comme le registre des sites).
revoke all on public.references_library from anon, authenticated;
grant all on public.references_library to service_role;
