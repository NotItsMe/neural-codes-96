"""Six-Role Wall (council 'Nonconvexity part 3', turns 5+7; checked by hand 2026-11-08).
PLANAR-ONLY test: if roles (o,i,j,p,q,b) satisfy W1..W9 the code has no convex drawing in R^2.
 W1 no codeword ⊇{o,i,j}; some ⊇{o,i}; some ⊇{o,j}
 W2 every codeword with i, not j, has p      W3 every codeword with j, not i, has q
 W4 every codeword with p, not i, has o      W5 every codeword with q and i has p
 W6 some codeword ⊇{o,p,b}; none ⊇{o,p,b,i}  W7 some codeword ⊇{b,i,j} without p
 W8 every codeword with b and (i or j) has both i and j
 W9 no codeword ⊇{b,p,i,j}"""
import os, json, sys
from itertools import permutations
def wall(code):
    code=[frozenset(w) for w in code]; N=sorted(set().union(*code)); hits=[]
    has=lambda S: any(S<=w for w in code)
    allw=lambda cond,need: all(need(w) for w in code if cond(w))
    for o,i,j,p,q,b in permutations(N,6) if len(N)>=6 else []:
        if has({o,i,j}) or not has({o,i}) or not has({o,j}): continue
        if not allw(lambda w:i in w and j not in w, lambda w:p in w): continue
        if not allw(lambda w:j in w and i not in w, lambda w:q in w): continue
        if not allw(lambda w:p in w and i not in w, lambda w:o in w): continue
        if not allw(lambda w:q in w and i in w, lambda w:p in w): continue
        if not has({o,p,b}) or has({o,p,b,i}): continue
        if not any({b,i,j}<=w and p not in w for w in code): continue
        if not allw(lambda w:b in w and (i in w or j in w), lambda w:i in w and j in w): continue
        if has({b,p,i,j}): continue
        hits.append((o,i,j,p,q,b))
    return hits
if __name__=="__main__":
    for c in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "codes.json")))["codes"]:
        h=wall(c["codewords"])
        if h: print(c["id"],len(h),h[0])
