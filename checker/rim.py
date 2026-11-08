"""Rim rule (council 'Remaining 15' turn 13, re-proved by hand 2026-11-08).
Neurons i,j,k,l,m (i!=j, k!=l). If
  (1) every codeword with i, without j, contains k;  every codeword with j, without i, contains l
  (2) some codeword contains {k,l};  no codeword contains {k,l,m}
  (3) codewords A (i,m in A, j not), B (j,m in B, i not), Z (i,j,m in Z)
  (4) no codeword contains (A&B) | {i,j}
then the code is NOT convex (any dimension)."""
import json, sys
from itertools import permutations
def rim(code):
    code=[frozenset(w) for w in code]
    N=sorted(set().union(*code)); hits=[]
    has=lambda S: any(S<=w for w in code)
    for i,j in permutations(N,2):
        for k in N:
            if not all(k in w for w in code if i in w and j not in w): continue
            for l in N:
                if l==k or not all(l in w for w in code if j in w and i not in w): continue
                if not has({k,l}): continue
                for m in N:
                    if has({k,l,m}): continue
                    Z=[w for w in code if {i,j,m}<=w]
                    if not Z: continue
                    for A in code:
                        if not({i,m}<=A and j not in A): continue
                        for B in code:
                            if {j,m}<=B and i not in B and not has((A&B)|{i,j}):
                                hits.append(dict(i=i,j=j,k=k,l=l,m=m,A=''.join(map(str,sorted(A))),B=''.join(map(str,sorted(B))),Z=''.join(map(str,sorted(Z[0])))))
    return hits
if __name__=="__main__":
    codes=json.load(open("jeffs_96_codes.json"))["codes"]
    for c in codes:
        h=rim([set(map(int,w)) if isinstance(w,str) else set(w) for w in c["codewords"]])
        if h: print(c["id"],len(h),h[0])
