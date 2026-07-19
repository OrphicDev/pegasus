#!/usr/bin/env python3
"""Budgets perf Orphic (interdit #4) via l'API PageSpeed Insights (gratuite, sans cle).
Usage: python check_perf_budget.py https://exemple.com [mobile|desktop]
Budgets: LCP < 2500 ms, INP < 200 ms (terrain), CLS < 0.1.
Attention: l'appel prend 20-60 s. Sortie JSON avec verdicts PASS/FAIL."""
import sys, json, urllib.request, urllib.parse

BUDGETS = {"LCP_ms": 2500, "INP_ms": 200, "CLS": 0.1}
PSI = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={u}&strategy={s}&category=performance"


def fetch(url, strategy):
    api = PSI.format(u=urllib.parse.quote(url, safe=''), s=strategy)
    req = urllib.request.Request(api, headers={"User-Agent": "orphic-skill/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    url = sys.argv[1]
    strategy = sys.argv[2] if len(sys.argv) > 2 else "mobile"
    try:
        data = fetch(url, strategy)
    except Exception as e:
        print(json.dumps({"erreur": f"PSI inaccessible: {e}"}, ensure_ascii=False))
        sys.exit(1)

    audits = data.get("lighthouseResult", {}).get("audits", {})
    lcp = audits.get("largest-contentful-paint", {}).get("numericValue")
    cls = audits.get("cumulative-layout-shift", {}).get("numericValue")
    tbt = audits.get("total-blocking-time", {}).get("numericValue")
    score = data.get("lighthouseResult", {}).get("categories", {}) \
                .get("performance", {}).get("score")
    # INP = donnee terrain (CrUX) si disponible
    inp = data.get("loadingExperience", {}).get("metrics", {}) \
              .get("INTERACTION_TO_NEXT_PAINT", {}).get("percentile")

    res = {
        "url": url, "strategie": strategy,
        "score_performance": round(score * 100) if score is not None else None,
        "LCP_ms": round(lcp) if lcp is not None else None,
        "CLS": round(cls, 3) if cls is not None else None,
        "INP_ms_terrain": inp,
        "TBT_ms_labo": round(tbt) if tbt is not None else None,
        "verdicts": {}
    }
    if lcp is not None:
        res["verdicts"]["LCP"] = "PASS" if lcp < BUDGETS["LCP_ms"] else "FAIL"
    if cls is not None:
        res["verdicts"]["CLS"] = "PASS" if cls < BUDGETS["CLS"] else "FAIL"
    if inp is not None:
        res["verdicts"]["INP"] = "PASS" if inp < BUDGETS["INP_ms"] else "FAIL"
    else:
        res["verdicts"]["INP"] = "INCONNU (pas de donnees terrain; surveiller TBT)"

    fails = [k for k, v in res["verdicts"].items() if v == "FAIL"]
    res["verdict_global"] = ("FAIL — interdit #4: " + ", ".join(fails)) if fails else "PASS"
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
