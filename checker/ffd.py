"""
ffd.py - Forced-Facet Descent: an upper bound on the dimension a MINIMAL open convex code needs.

Facts used (C open convex, realized by open convex U_i in R^d, bounded realization since empty word is in C):
  (1) Restriction: for any affine flat F, the sets U_i ∩ F realize a convex code C' ⊆ C (in F), with ∅ ∈ C'.
      If C' contains every facet of C, then Δ(C') = Δ(C), and C' (being convex, so no local obstruction)
      contains every mandatory codeword. For a MINIMAL code (C = facets + mandatory + ∅), C' = C.
  (2) Walk along a segment [a,b]: every point's codeword contains ω(a)∩ω(b) (each U_i is convex), and
      neighbouring pieces have comparable codewords (sets are open). So the codewords met form a path from
      ω(a) to ω(b) in the comparability graph on Tk(ω(a)∩ω(b)). If codeword φ is a cut vertex separating
      ω(a) from ω(b) there, every segment from a point of ω(a) to a point of ω(b) contains a point of φ.
Procedure: choose k base codewords (their witness points span a flat of dim <= k-1). Repeatedly add every
codeword forced on a segment between two points already in the flat. If every facet gets reached, then
C convex  =>  C convex in R^(k-1).    bound(C) = smallest such k-1 over all base sets.
"""
import json, sys
from itertools import combinations


def cut_forced(code, A, B):
    """codewords (other than A, B) that every comparability path from A to B in Tk(A&B) must visit."""
    base = A & B
    nodes = [w for w in code if base <= w]
    adj = {w: [v for v in nodes if v != w and (v <= w or w <= v)] for w in nodes}

    def reach(blocked):
        seen, stack = {A}, [A]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen and y != blocked:
                    seen.add(y)
                    stack.append(y)
        return B in seen

    if not reach(None):
        return None                     # no path at all: these two points can't be in one convex code
    return [w for w in nodes if w not in (A, B) and not reach(w)]


def closure(code, start):
    have = set(start)
    changed = True
    while changed:
        changed = False
        for A, B in combinations(list(have), 2):
            f = cut_forced(code, A, B)
            if f is None:
                return None
            for w in f:
                if w not in have:
                    have.add(w)
                    changed = True
    return have


def is_minimal(code, facets):
    """every nonempty non-facet codeword must be mandatory (link has nonzero reduced homology)."""
    from neuralcodes import minimal_code
    return set(code) == set(minimal_code(frozenset(facets)))


def bound(codewords, maxk=6):
    code = [frozenset(w) for w in {frozenset(c) for c in codewords} | {frozenset()}]
    facets = [w for w in code if w and not any(w < v for v in code)]
    if not is_minimal(code, facets):
        raise ValueError("FFD needs a minimal code (facets + mandatory codewords + empty)")
    nonempty = [w for w in code if w]
    for k in range(1, maxk + 1):
        for base in combinations(nonempty, k):
            got = closure(code, base)
            if got is not None and all(f in got for f in facets):
                return k - 1, ["".join(map(str, sorted(b))) for b in base]
    return None, None


if __name__ == "__main__":
    codes = {c["id"]: c for c in json.load(open("/home/claude/jeffs_96_codes.json"))["codes"]}
    for cid in sys.argv[1:] or sorted(codes):
        d, base = bound(codes[cid]["codewords"])
        print(cid, d, base, flush=True)
