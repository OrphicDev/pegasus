#!/usr/bin/env python3
"""Contraste WCAG entre deux couleurs (interdit #3).
Usage: python check_contrast.py '#ffffff' '#0a0a0c' [--large]
--large = texte >= 18.66px bold ou >= 24px normal.
Sortie JSON: ratio, AA, AAA, verdict."""
import sys, re, json


def parse(c):
    c = c.strip().lstrip('#')
    if len(c) == 3:
        c = ''.join(x * 2 for x in c)
    if not re.fullmatch(r'[0-9a-fA-F]{6}', c):
        raise ValueError(f"Couleur invalide: {c}")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def lum(rgb):
    def f(v):
        v /= 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(c1, c2):
    l1, l2 = sorted((lum(parse(c1)), lum(parse(c2))), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    large = '--large' in sys.argv
    if len(args) != 2:
        print(__doc__)
        sys.exit(1)
    try:
        r = ratio(args[0], args[1])
    except ValueError as e:
        print(json.dumps({"erreur": str(e)}, ensure_ascii=False))
        sys.exit(1)
    aa = r >= (3.0 if large else 4.5)
    aaa = r >= (4.5 if large else 7.0)
    print(json.dumps({
        "couleurs": args, "texte": "large" if large else "normal",
        "ratio": round(r, 2), "AA": aa, "AAA": aaa,
        "verdict": "PASS" if aa else "FAIL — interdit #3, corriger avant livraison"
    }, ensure_ascii=False))
