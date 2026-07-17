#!/usr/bin/env node
/**
 * Génère la « clé d'équipe » Pegasus à partager avec les devs (via 1Password/WhatsApp).
 * = base64( JSON { supabase_url, supabase_service_key, supabase_anon_key, private_key } )
 *
 * Lit les secrets LOCAUX (jamais versionnés) : ../mcp-server/pegasus.config.json + ../mcp-server/pegasus-private.pem
 * Réservé à l'administrateur Pegasus (Sacha), qui détient ces fichiers.
 *
 * Usage : node scripts/make-team-key.mjs
 */
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const dir = dirname(fileURLToPath(import.meta.url));
const src = join(dir, "..", "mcp-server");

try {
  const cfg = JSON.parse(readFileSync(join(src, "pegasus.config.json"), "utf8"));
  const priv = readFileSync(join(src, "pegasus-private.pem"), "utf8");
  const bundle = {
    supabase_url: cfg.supabase_url,
    supabase_service_key: cfg.supabase_service_key,
    supabase_anon_key: cfg.supabase_anon_key,
    private_key: priv,
  };
  const key = Buffer.from(JSON.stringify(bundle)).toString("base64");
  console.log("\n===== CLÉ D'ÉQUIPE PEGASUS (à coller à l'installation du plugin) =====\n");
  console.log(key);
  console.log(`\n(${key.length} caractères — partager via 1Password, JAMAIS dans un dépôt ou un chat)\n`);
} catch (e) {
  console.error("Erreur : impossible de lire les secrets locaux (" + e.message + ").");
  console.error("Ce script doit tourner sur le Mac de l'admin, avec mcp-server/pegasus.config.json + pegasus-private.pem en place.");
  process.exit(1);
}
