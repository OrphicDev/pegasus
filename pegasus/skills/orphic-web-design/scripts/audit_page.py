#!/usr/bin/env python3
"""Audit statique d'une page contre les regles Orphic mesurables.
Usage: python audit_page.py https://exemple.com
Verifie (faits, pas de jugement): SEO de base, nb de familles de polices,
couleurs distinctes en CSS, presence de prefers-reduced-motion, images sans
alt et formats, librairies detectees, poids HTML. Sortie JSON faits+alertes."""
import sys, re, json, urllib.request, urllib.parse
from html.parser import HTMLParser

UA = {"User-Agent": "Mozilla/5.0 (Macintosh) orphic-skill/1.0"}
GENERIC_FONTS = {"sans-serif", "serif", "monospace", "system-ui", "cursive",
                 "fantasy", "inherit", "initial", "unset", "ui-sans-serif",
                 "ui-serif", "ui-monospace", "var", "-apple-system"}
LIBS = ["three", "gsap", "scrolltrigger", "lenis", "barba", "pixi", "curtains",
        "shery", "lottie", "rive", "matter", "anime", "split-type", "splittype",
        "atropos", "theatre"]


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = None; self._in_title = False; self._in_style = False
        self.meta = {}; self.lang = None; self.h1 = 0
        self.imgs = []; self.css_links = []; self.scripts = []
        self.inline_css = []; self.inline_js = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "style":
            self._in_style = True
        elif tag == "h1":
            self.h1 += 1
        elif tag == "meta" and a.get("name"):
            self.meta[a["name"].lower()] = a.get("content", "")
        elif tag == "link" and "stylesheet" in (a.get("rel") or ""):
            if a.get("href"):
                self.css_links.append(a["href"])
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "script" and a.get("src"):
            self.scripts.append(a["src"])

    def handle_endtag(self, tag):
        if tag == "title": self._in_title = False
        if tag == "style": self._in_style = False

    def handle_data(self, d):
        if self._in_title:
            self.title = (self.title or "") + d.strip()
        if self._in_style:
            self.inline_css.append(d)


def get(url, limit=1_500_000):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read(limit).decode("utf-8", "replace")


def main():
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(1)
    url = sys.argv[1]
    try:
        html = get(url)
    except Exception as e:
        print(json.dumps({"erreur": f"fetch: {e}"}, ensure_ascii=False)); sys.exit(1)

    p = P(); p.feed(html)
    css = "\n".join(p.inline_css)
    host = urllib.parse.urlparse(url).netloc
    for href in p.css_links[:4]:
        full = urllib.parse.urljoin(url, href)
        if urllib.parse.urlparse(full).netloc in (host, "fonts.googleapis.com"):
            try:
                css += "\n" + get(full, 400_000)
            except Exception:
                pass

    fams = set()
    for m in re.finditer(r'font-family\s*:\s*([^;}]+)', css, re.I):
        f = m.group(1).split(",")[0].strip().strip("'\"").lower()
        if f and f not in GENERIC_FONTS and not f.startswith("var("):
            fams.add(f)
    for l in p.css_links:
        for m in re.finditer(r'family=([^&:@]+)', l):
            fams.add(urllib.parse.unquote(m.group(1)).replace("+", " ").lower())

    colors = set()
    for m in re.finditer(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', css):
        c = m.group(1).lower()
        colors.add(c if len(c) == 6 else "".join(x * 2 for x in c))

    blob = (html + " ".join(p.scripts)).lower()
    libs = sorted({l for l in LIBS if l in blob})
    no_alt = sum(1 for i in p.imgs if not (i.get("alt") or "").strip())
    formats = {}
    for i in p.imgs:
        ext = (i.get("src") or "").split("?")[0].rsplit(".", 1)[-1].lower()[:5]
        formats[ext] = formats.get(ext, 0) + 1
    rm = "prefers-reduced-motion" in css or "prefers-reduced-motion" in html
    desc = p.meta.get("description", "")

    faits = {
        "url": url, "poids_html_ko": round(len(html) / 1024),
        "titre": p.title, "meta_description_longueur": len(desc),
        "viewport": "viewport" in p.meta, "lang": p.lang, "h1": p.h1,
        "familles_de_polices": sorted(fams), "nb_polices": len(fams),
        "couleurs_distinctes_css": len(colors),
        "couleurs_extrait": sorted(colors)[:20],
        "prefers_reduced_motion": rm,
        "images": {"total": len(p.imgs), "sans_alt": no_alt, "formats": formats},
        "libs_detectees": libs,
    }
    alertes = []
    if not p.title: alertes.append("SEO: <title> manquant")
    if not desc: alertes.append("SEO: meta description manquante")
    elif not 50 <= len(desc) <= 160: alertes.append("SEO: meta description hors 50-160 car.")
    if p.h1 != 1: alertes.append(f"SEO: {p.h1} balise(s) h1 (attendu: 1)")
    if not p.meta.get("viewport") and "viewport" not in p.meta: alertes.append("mobile: meta viewport manquante")
    if not p.lang: alertes.append("a11y: attribut lang manquant")
    if len(fams) > 2: alertes.append(f"signature: {len(fams)} familles de polices (max 2)")
    if not rm: alertes.append("interdit #3: prefers-reduced-motion absent")
    if no_alt: alertes.append(f"a11y: {no_alt} image(s) sans alt")
    if len(colors) > 12: alertes.append(f"palette: {len(colors)} couleurs CSS — verifier la retenue (nuances comprises, a interpreter)")
    if len(html) > 300_000: alertes.append("perf: HTML > 300 Ko")

    print(json.dumps({"faits": faits, "alertes": alertes,
                      "note": "Faits bruts. Le jugement (singularite, intention, matiere) reste humain/LLM."},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
