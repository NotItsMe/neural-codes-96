#!/usr/bin/env python3
"""
verify.py - check every drawing in this repo with exact arithmetic.

    pip install z3-solver
    python3 checker/verify.py            # all codes with a drawing
    python3 checker/verify.py C5-068     # one code

A drawing gives each neuron i an open convex region  U_i = { p : lo < a.p < hi  for each direction a }.
For every set S of neurons, Z3 (exact rational arithmetic, no rounding) decides whether some point lies
in exactly the regions of S. The set of S that occur is the code the drawing makes. The check passes
only if it equals the target code exactly: no codeword missing, no extra codeword.
"""
import json, os, sys
from fractions import Fraction as F
from itertools import combinations
from z3 import Real, Solver, And, Not, Q, sat

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


def load(cid):
    for suffix in ("_3D", "_D8", ""):
        path = os.path.join(DATA, "certificates", f"{cid}{suffix}.json")
        if os.path.exists(path):
            d = json.load(open(path))
            if "boxes" in d:
                return [(1, 0), (0, 1)], {n: {"1,0": b[0], "0,1": b[1]} for n, b in d["boxes"].items()}
            if "regions" in d:
                names = {"x": "1,0", "y": "0,1", "x+y": "1,1", "x-y": "1,-1"}
                return [(1, 0), (0, 1), (1, 1), (1, -1)], {n: {names[f]: v for f, v in r.items()} for n, r in d["regions"].items()}
            return [tuple(x) for x in d["directions"]], d["drawing"]
    return None


def produced_code(dirs, cert):
    dim = len(dirs[0])
    p = [Real(f"p{i}") for i in range(dim)]
    neurons = sorted(int(n) for n in cert)

    def inside(n):
        r = cert[str(n)]
        terms = []
        for d in dirs:
            lo, hi = (F(x) for x in r[",".join(map(str, d))])
            v = sum(a * x for a, x in zip(d, p))
            terms += [Q(lo.numerator, lo.denominator) < v, v < Q(hi.numerator, hi.denominator)]
        return And(terms)

    found = set()
    for k in range(len(neurons) + 1):
        for S in combinations(neurons, k):
            s = Solver()
            s.add([inside(n) if n in S else Not(inside(n)) for n in neurons])
            if s.check() == sat:
                found.add(frozenset(S))
    return found


def main():
    codes = {c["id"]: c for c in json.load(open(os.path.join(DATA, "codes.json")))["codes"]}
    ids = sys.argv[1:] or sorted(codes)
    passed = failed = 0
    for cid in ids:
        got = load(cid)
        if got is None:
            if len(sys.argv) > 1:
                print(cid, "has no drawing (status:", codes[cid].get("status", "?") + ")")
            continue
        target = {frozenset(w) for w in codes[cid]["codewords"]} | {frozenset()}
        made = produced_code(*got)
        ok = made == target
        passed += ok
        failed += not ok
        extra, missing = made - target, target - made
        print(f"{cid}: {'PASS' if ok else 'FAIL'}  (dimension {len(got[0][0])})"
              + ("" if ok else f"  missing={sorted(map(sorted, missing))} extra={sorted(map(sorted, extra))}"), flush=True)
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
