#!/usr/bin/env python3
"""Valide un fichier .glb contre les budgets 3D Orphic (3d-pipeline.md, interdit #4).
Usage: python check_glb.py scene.glb [--hero]
--hero = objet heros seul (budget 150k triangles) sinon scene (500k).
Pur Python, sans dependance. Sortie JSON: taille, triangles, verdicts."""
import sys, json, struct

BUDGET_MB = 8
BUDGET_TRIS = {"hero": 150_000, "scene": 500_000}


def read_glb_json(path):
    with open(path, "rb") as f:
        magic, version, _len = struct.unpack("<4sII", f.read(12))
        if magic != b"glTF":
            raise ValueError("Pas un GLB (magic invalide)")
        clen, ctype = struct.unpack("<II", f.read(8))
        if ctype != 0x4E4F534A:  # 'JSON'
            raise ValueError("Premier chunk non-JSON")
        return json.loads(f.read(clen).decode("utf-8"))


def count_triangles(g):
    acc = g.get("accessors", [])
    total = 0
    per_mesh = []
    for mesh in g.get("meshes", []):
        t = 0
        for prim in mesh.get("primitives", []):
            mode = prim.get("mode", 4)
            if mode != 4:  # seuls les TRIANGLES comptent
                continue
            if "indices" in prim:
                t += acc[prim["indices"]].get("count", 0) // 3
            elif "POSITION" in prim.get("attributes", {}):
                t += acc[prim["attributes"]["POSITION"]].get("count", 0) // 3
        per_mesh.append({"mesh": mesh.get("name", "?"), "triangles": t})
        total += t
    return total, sorted(per_mesh, key=lambda m: -m["triangles"])[:10]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    mode = "hero" if "--hero" in sys.argv else "scene"
    if len(args) != 1:
        print(__doc__); sys.exit(1)
    path = args[0]
    try:
        g = read_glb_json(path)
    except Exception as e:
        print(json.dumps({"erreur": str(e)}, ensure_ascii=False)); sys.exit(1)

    import os
    size_mb = os.path.getsize(path) / 1_048_576
    tris, top = count_triangles(g)
    budget = BUDGET_TRIS[mode]
    res = {
        "fichier": path, "mode": mode,
        "taille_mo": round(size_mb, 2),
        "triangles": tris,
        "meshes_les_plus_lourds": top,
        "materiaux": len(g.get("materials", [])),
        "textures": len(g.get("textures", [])),
        "images_embarquees": len(g.get("images", [])),
        "extensions": g.get("extensionsUsed", []),
        "verdicts": {
            "taille": "PASS" if size_mb <= BUDGET_MB else f"FAIL (> {BUDGET_MB} Mo — Draco/KTX2/streaming requis)",
            "triangles": "PASS" if tris <= budget else f"FAIL (> {budget:,} — decimate/retopo requis)",
            "draco": "OK" if "KHR_draco_mesh_compression" in g.get("extensionsUsed", []) else "ABSENT — compresser (gltf-transform)",
        }
    }
    fails = [k for k, v in res["verdicts"].items() if str(v).startswith("FAIL")]
    res["verdict_global"] = ("FAIL — " + ", ".join(fails)) if fails else "PASS"
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
