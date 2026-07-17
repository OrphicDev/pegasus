"use strict";
const $ = (id) => document.getElementById(id);
const codeEl = $("code"), goEl = $("go"), msgEl = $("msg");

// Si la clé est déjà là, on va direct à l'écran de succès.
window.pegasus.status().then((s) => {
  if (s && s.installed) showDone();
});

// Formatage auto : groupes de 4 séparés par des tirets, majuscules.
codeEl.addEventListener("input", () => {
  const raw = codeEl.value.toUpperCase().replace(/[^A-Z0-9]/g, "").slice(0, 16);
  codeEl.value = raw.match(/.{1,4}/g)?.join("-") || raw;
});

codeEl.addEventListener("keydown", (e) => { if (e.key === "Enter") connect(); });
goEl.addEventListener("click", connect);

async function connect() {
  const code = codeEl.value.trim();
  if (code.replace(/[^A-Z0-9]/g, "").length < 8) {
    return setMsg("Entre ton code d'accès complet.", "err");
  }
  goEl.disabled = true;
  goEl.innerHTML = '<span class="spin"></span>Connexion…';
  setMsg("", "");

  const r = await window.pegasus.connect(code);

  if (r.ok) {
    showDone();
  } else {
    setMsg(r.error || "Échec de la connexion.", "err");
    goEl.disabled = false;
    goEl.textContent = "Connecter";
  }
}

function setMsg(t, cls) {
  msgEl.textContent = t;
  msgEl.className = "msg" + (cls ? " " + cls : "");
}

function showDone() {
  $("loginCard").classList.add("hidden");
  $("doneCard").classList.remove("hidden");
}
