#!/usr/bin/env python3
"""Audit groupé d'URLs de référence (constitution d'un dossier de refs, veille).
Usage: python audit_refs.py URL1 URL2 ...
       python audit_refs.py --file liste.txt   (une URL par ligne, # = commentaire)
Lance audit_page.py sur chaque URL et agrège les faits pour COMPARER les refs :
libs détectées, familles de polices, retenue chromatique, reduced-motion, poids.
Sortie JSON: un audit par URL + une synthèse transversale. Faits bruts —
l'extraction d'ingrédients (registre, matière, intention) reste humain/LLM."""
import sys, os, json, subprocess


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    if args[0] == "--file":
        if len(args) < 2:
            print(__doc__)
            sys.exit(1)
        with open(args[1]) as f:
            urls = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]
    else:
        urls = args

    audit = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audit_page.py")
    audits = []
    libs, fonts = {}, {}
    sans_rm, lourdes = [], []
    for url in urls:
        try:
            out = subprocess.run([sys.executable, audit, url],
                                 capture_output=True, text=True, timeout=120)
            data = json.loads(out.stdout)
        except Exception as e:
            data = {"faits": {"url": url}, "erreur": f"audit impossible: {e}"}
        audits.append(data)
        faits = data.get("faits", {})
        for lib in faits.get("libs_detectees", []):
            libs[lib] = libs.get(lib, 0) + 1
        for fam in faits.get("familles_de_polices", []):
            fonts[fam] = fonts.get(fam, 0) + 1
        if faits.get("prefers_reduced_motion") is False:
            sans_rm.append(url)
        if (faits.get("poids_html_ko") or 0) > 300:
            lourdes.append(url)

    synthese = {
        "nb_refs": len(urls),
        "libs_par_frequence": dict(sorted(libs.items(), key=lambda x: -x[1])),
        "polices_par_frequence": dict(sorted(fonts.items(), key=lambda x: -x[1])),
        "sans_reduced_motion": sans_rm,
        "html_lourd_300ko": lourdes,
        "note": ("Faits bruts pour comparaison. Une réf = des ingrédients à "
                 "recombiner, jamais un modèle (SKILL.md §6)."),
    }
    print(json.dumps({"synthese": synthese, "audits": audits},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
