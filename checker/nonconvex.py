#!/usr/bin/env python3
"""
nonconvex.py - re-run every non-convexity argument in this repo, with controls.

    python3 checker/nonconvex.py

Three rules, each proved in docs/proofs.md (pure Python, no solver needed):
  Rim rule (rim.py)           - not convex in any dimension.
  Six-Role Wall (sixrole.py)  - no convex drawing in the plane.
  Forced-Facet Descent (ffd.py) - for a minimal code: convex => convex in R^bound.
Results checked here:
  C5-033, C5-095: Rim fires on the code itself.
  C5-085: Rim fires on the code of (U2, U3, U4, U5, U6, U1∩U4), which any drawing of C5-085 would draw.
  C5-053, C5-072, C5-076: Six-Role Wall fires and FFD bound is 2, so they are not convex in any dimension.
Controls: none of the rules may fire on any code with a drawing in data/certificates
(the Six-Role Wall is also checked against every code drawn in the plane).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rim import rim
from sixrole import wall
from ffd import bound

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
codes = {c["id"]: [frozenset(w) for w in c["codewords"]] + [frozenset()]
         for c in json.load(open(os.path.join(DATA, "codes.json")))["codes"]}
certs = os.listdir(os.path.join(DATA, "certificates"))
drawn = {f.split("_")[0].replace(".json", "") for f in certs}
planar = {f.replace(".json", "").replace("_D8", "") for f in certs if "_3D" not in f}

def image_085():
    c = codes["C5-085"]
    T = lambda s: {w for w in c if s <= w}
    trunks = [T({2}), T({3}), T({4}), T({5}), T({6}), T({1, 4})]
    return {frozenset(t + 1 for t, Tr in enumerate(trunks) if w in Tr) for w in c}

ok = True
def report(name, cond):
    global ok
    ok &= cond
    print(("PASS  " if cond else "FAIL  ") + name)

for cid in ("C5-033", "C5-095"):
    h = rim(codes[cid]); report(f"{cid}: Rim rule fires {h[0] if h else ''}", bool(h))
h = rim(image_085()); report(f"C5-085: Rim rule fires on the image {h[0] if h else ''}", bool(h))
for cid in ("C5-053", "C5-072", "C5-076"):
    w = wall(codes[cid]); d, base = bound(codes[cid])
    report(f"{cid}: Six-Role Wall fires {w[0] if w else ''}; FFD bound {d} from base {base}", bool(w) and d == 2)
report(f"controls: Rim silent on all {len(drawn)} drawn codes", not any(rim(codes[c]) for c in drawn))
report(f"controls: Six-Role Wall silent on all {len(planar)} codes drawn in the plane", not any(wall(codes[c]) for c in planar))
print("\nall checks passed" if ok else "\nSOME CHECKS FAILED")
sys.exit(0 if ok else 1)
