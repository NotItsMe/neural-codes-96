"""Hypothesis-pattern scanner for the 087 / 013 non-convexity proofs (referee run).

Each rule is the exact list of combinatorial facts the corresponding proof uses.
Role sets (A, B, P, F, G, K, X, Y, Z) may be single neurons or intersections
(any nonempty neuron subset), since intersections of open convex sets are open convex.

Rules:
  R_TS  : l7_proof "two-shadow + finite crease" (087)
  R_NO  : l7_draw  "Notch" (087)  -- R_TS plus X subset A, Y,Z subset B (arc containment)
  R_TE  : l7_draw  "Twin-Exit Notch" (013)

A rule firing on a convex code means the proof is wrong.
"""
import json, itertools, sys

import os
CODES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'codes.json')))['codes']
EXTRA_CONVEX = {'C5-060', 'C5-067', 'C5-069', 'C5-086', 'C5-094'}  # exact drawings checked

N = range(1, 7)
SUBSETS = [frozenset(s) for r in range(1, 7) for s in itertools.combinations(N, r)]


def mk(code):
    return [frozenset(w) for w in code['codewords']]


def exists(C, S):            # some codeword contains S   (U_S nonempty)
    return any(S <= c for c in C)


def every(C, S, T):          # U_S subset U_T  (every codeword containing S contains T)
    return all(T <= c for c in C if S <= c)


def diff(C, A, B):           # codewords of points in U_A \ U_B
    return [c for c in C if A <= c and not B <= c]


def bridge_ok(C, A, B, K):
    return exists(C, K | A) and exists(C, K | B) and not exists(C, K | A | B)


def bridges(C, A, B):
    return [K for K in SUBSETS if bridge_ok(C, A, B, K)]


def rule_TS(C, A, B):
    """two-shadow (l7_proof): A∖B ⊂ U_P, B∖A ⊂ U_F∩U_G, U_P∩U_F∩U_G=∅,
    U_F,U_G ⊂ A∪B, U_P∩U_F, U_P∩U_G nonempty, bridge K."""
    if not exists(C, A | B):
        return []
    dA, dB = diff(C, A, B), diff(C, B, A)
    if not dA or not dB:
        return []
    capA = frozenset.intersection(*dA)
    capB = frozenset.intersection(*dB)
    Ks = bridges(C, A, B)
    if not Ks:
        return []
    hits = []
    Ps = [P for P in SUBSETS if P <= capA]
    FG = [F for F in SUBSETS if F <= capB]
    for P in Ps:
        for F, G in itertools.combinations(FG, 2):
            if F <= G or G <= F:
                continue
            if exists(C, P | F | G):
                continue
            if not (exists(C, P | F) and exists(C, P | G)):
                continue
            inAB = lambda S: all((A <= c) or (B <= c) for c in C if S <= c)
            if not (inAB(F) and inAB(G)):
                continue
            hits.append((P, F, G, Ks[0]))
    return hits


def rule_NO(C, A, B):
    """Notch (l7_draw): two-shadow pattern + X⊂A, Y,Z⊂B (arc containment)."""
    out = []
    for P, F, G, K in rule_TS(C, A, B):
        if every(C, P, A) and every(C, F, B) and every(C, G, B):
            out.append((P, F, G, K))
    return out


def rule_TE(C, A, B):
    """Twin-Exit (l7_draw, 013 with A=3,B=4,K=5,X=1,Y=6,Z=2):
    (a) A∖B ⊂ U_X   (b) B∖A ⊂ U_Y   (c) U_Z∩A ⊂ B and U_Z∩B ⊂ A
    (d) A∩U_Y ⊂ U_Z  (e) no codeword ⊇ X∪Z∪A  (f) U_X∩U_Z ≠ ∅, bridge K."""
    if not exists(C, A | B):
        return []
    dA, dB = diff(C, A, B), diff(C, B, A)
    if not dA or not dB:
        return []
    Ks = bridges(C, A, B)
    if not Ks:
        return []
    capA = frozenset.intersection(*dA)
    capB = frozenset.intersection(*dB)
    hits = []
    for X in SUBSETS:
        if not X <= capA:
            continue
        for Y in SUBSETS:
            if not Y <= capB:
                continue
            for Z in SUBSETS:
                if not (every(C, Z | A, B) and every(C, Z | B, A)):
                    continue
                if not every(C, A | Y, Z):
                    continue
                if exists(C, X | Z | A):
                    continue
                if not exists(C, X | Z):
                    continue
                hits.append((X, Y, Z, Ks[0]))
    return hits


def fmt(S):
    return ''.join(map(str, sorted(S)))


def scan(rule, roles=('single', 'pair')):
    AB = [S for S in SUBSETS if len(S) <= 2]
    res = {}
    for code in CODES:
        C = mk(code)
        found = []
        for A in AB:
            for B in AB:
                if A == B or A <= B or B <= A:
                    continue
                h = rule(C, A, B)
                if h:
                    found.append((A, B, h[0], len(h)))
        if found:
            res[code['id']] = (code['status'], found)
    return res


if __name__ == '__main__':
    for name, rule in [('TS (l7_proof 087)', rule_TS), ('NO (l7_draw 087)', rule_NO),
                       ('TE (l7_draw 013)', rule_TE)]:
        res = scan(rule)
        print('=== rule', name, '- fires on', len(res), 'codes')
        for cid, (st, found) in sorted(res.items()):
            conv = st.startswith('convex') or cid in EXTRA_CONVEX
            A, B, h, n = found[0]
            print(f"  {cid:7s} [{'CONVEX!!' if conv else st}] e.g. A={fmt(A)} B={fmt(B)} "
                  f"roles={[fmt(s) for s in h]} ({len(found)} (A,B) pairs)")
