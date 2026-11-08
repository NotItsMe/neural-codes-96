# Proofs for the six new non-convex codes

Notation. A code C on neurons 1–6 is *open convex* in R^d if there are open convex sets U_1, …, U_6 ⊆ R^d with
C = { {i : x ∈ U_i} : x ∈ R^d }. "Codeword ⊇ S" means some codeword of C contains the set S.
Every codeword condition below can be read straight off the code's list of codewords, and
`python3 checker/nonconvex.py` re-checks all of them.

Two facts get used repeatedly:
- **(R)** If two open convex sets overlap, the closure of their intersection is the intersection of their closures
  (Rockafellar, *Convex Analysis*, Thm 6.5). So if U_k ∩ U_l ≠ ∅, U_m is open, and no codeword contains {k, l, m},
  then cl U_k ∩ cl U_l ∩ U_m = ∅.
- **(G)** For an open convex set U and a point z ∈ U, the gauge γ(x) = inf{t > 0 : z + (x − z)/t ∈ U} is continuous,
  and x ∈ U exactly when γ(x) < 1.

---

## 1. The Rim rule (not convex in any dimension)

**Rule.** Let i ≠ j and k ≠ l be neurons, and m another neuron. Suppose
1. every codeword with i but not j contains k, and every codeword with j but not i contains l;
2. some codeword contains {k, l}, and none contains {k, l, m};
3. there are codewords A ∋ i, m with j ∉ A; B ∋ j, m with i ∉ B; and Z ⊇ {i, j, m};
4. no codeword contains (A ∩ B) ∪ {i, j}.

Then C is not open convex in any dimension.

**Proof.** Suppose U_1, …, U_6 realize C. By (1), U_i∖U_j ⊆ U_k and U_j∖U_i ⊆ U_l. By (2) and (R),
cl U_k ∩ cl U_l ∩ U_m = ∅. Pick points a, b, z with codewords exactly A, B, Z. They aren't collinear (otherwise a would
lie in U_j or b in U_i), and the triangle abz lies in U_m. The segment [a, b] lies in every U_t with t ∈ A ∩ B, so by (4)
it misses U_i ∩ U_j.

Let γ_i, γ_j be the gauges of U_i, U_j centered at z. Then γ_i(a) < 1 ≤ γ_j(a) and γ_j(b) < 1 ≤ γ_i(b).
Let S = {q ∈ [a,b] : γ_i(q) < γ_j(q)} and T = {q : γ_j(q) < γ_i(q)}; both are open in [a,b], with a ∈ S and b ∈ T.

*The set E = {γ_i = γ_j} has empty interior in [a,b].* Otherwise, in the plane P of the triangle, U_i ∩ P and U_j ∩ P coincide
inside an open angular sector at z. Take q in that interval, g = γ_i(q) = γ_j(q) ≥ 1 (since q ∉ U_i ∩ U_j), and
r = z + (q − z)/g, a common boundary point. A supporting line L of U_i ∩ P at r also supports U_j ∩ P (a point of U_j on
the wrong side of L, joined to r, would put points of U_i near r on the wrong side). Then a and b lie strictly on z's side
of L, so q does too, so r (a convex combination of z and q) does too, which contradicts r ∈ L.

Let p = inf T. Points of S accumulate at p from the left and points of T from the right, and γ_i(p) = γ_j(p) = t ≥ 1.
Put r = z + (p − z)/t, a point of [z, p] ⊂ U_m. For q ∈ S near p, choose s in (γ_i(q), γ_j(q)]; the point
z + (q − z)/s lies in U_i∖U_j ⊆ U_k, and these points tend to r. So r ∈ cl U_k, and the same argument with T gives
r ∈ cl U_l. Then r ∈ cl U_k ∩ cl U_l ∩ U_m = ∅, a contradiction. ∎

**C5-033** (1345 1346 2345 2356 134 235 345 12 36 1 2 3 ∅): take i, j, k, l, m = 4, 5, 1, 2, 3 and A, B, Z = 1346, 2356, 345.
Codewords with 4 but not 5 are 1346 and 134 (both contain 1); with 5 but not 4, 2356 and 235 (both contain 2); 12 is a
codeword and nothing contains 123; A ∩ B = {3, 6} and nothing contains 3456.

**C5-095** (1234 1236 1256 1345 2346 123 126 134 234 236 15 23 1 ∅): take i, j, k, l, m = 2, 3, 6, 4, 1 and
A, B, Z = 1256, 1345, 123. Codewords with 2 but not 3 are 1256 and 126 (both contain 6); with 3 but not 2, 1345 and 134
(both contain 4); 2346 contains 46 and nothing contains 146; A ∩ B = {1, 5} and nothing contains 1235.

**C5-085** (1245 1246 1345 3456 123 124 145 345 12 13 46 1 4 ∅). From any realization U of C5-085, the six open convex sets
V = (U_2, U_3, U_4, U_5, U_6, U_1 ∩ U_4) realize the code
1346 1356 2346 2345 12 136 346 234 1 2 35 3 ∅
(each codeword w of C5-085 becomes {t : the t-th set contains the points of w}). The Rim rule fires on that code with
i, j, k, l, m = 4, 6, 2, 1, 3 and A, B, Z = 2345, 1356, 346, so C5-085 is not convex either. (This is a special case of
Jeffs' morphism theorem, arXiv:1806.02014, Prop. 2.11 and Thm 1.3, but the direct construction is all that's needed.)

The rule is silent on every one of the 80 codes in this repo that have a drawing.

---

## 2. The Six-Role Wall (no convex drawing in the plane)

**Rule.** Roles o, i, j, p, q, b (neurons) with
- W1: no codeword ⊇ {o, i, j}; some codeword ⊇ {o, i} and some ⊇ {o, j};
- W2: every codeword with i but not j contains p;  W3: every codeword with j but not i contains q;
- W4: every codeword with p but not i contains o;  W5: every codeword with q and i contains p;
- W6: some codeword ⊇ {o, p, b}, none ⊇ {o, p, b, i};
- W7: some codeword ⊇ {b, i, j} that doesn't contain p;
- W8: every codeword with b and (i or j) contains both i and j;
- W9: no codeword ⊇ {b, p, i, j}.

Then C has no open convex realization in R².

**Proof.** Let D = U_i ∩ U_j, nonempty by W7. By W1, U_o and D are disjoint open convex sets, so a line m has U_o strictly
above it and D strictly below. U_i has points above m (a codeword ⊇ {o, i}) and below (D), so I_i = U_i ∩ m is a nonempty
open interval; likewise I_j. They're disjoint, since D lies below m. W6 gives a point a ∈ U_o ∩ U_p ∩ U_b; that open set
misses U_i, so a ∉ cl U_i. W7 gives r ∈ U_b ∩ D with r ∉ U_p, below m. So J_b = U_b ∩ m contains c = [a, r] ∩ m, and by W8
it misses I_i and I_j. Two facts used below: for an open convex U meeting m, cl U ∩ m = cl(U ∩ m); and for rays from a
point outside cl U that enter U, the first point of cl U on the ray moves continuously with the ray.

*Ray Lemma.* Take a ray from a whose first point g of cl U_i lies strictly below m, and which then enters U_i.
(1) Points just past g are in U_i∖U_p ⊆ U_j (by W2): if such a point y were in U_p, then [a, y] ⊆ U_p, and points just
before g would be in U_p∖U_i below m, but U_p∖U_i ⊆ U_o lies above m (W4). (2) g ∉ U_j: otherwise g ∈ U_j∖U_i ⊆ U_q (W3),
so points just past g lie in U_q ∩ U_i ⊆ U_p (W5), contradicting (1).

Reflect if needed so that I_i is left of I_j. There are three orders.
- **I_i, J_b, I_j.** Take s ∈ I_i, t ∈ I_j. The segment [s, r] ⊂ U_i runs from U_p∖U_j to U_j∖U_p, so it meets
  U_i ∩ U_j ∩ U_p at a point z_1 ≠ r. The segment [t, r] ⊂ U_j runs from U_q∖U_i into U_i, so it meets U_i ∩ U_j ∩ U_q
  ⊆ U_p at a point z_2 ≠ r. The segment [z_1, z_2] ⊂ U_i ∩ U_j ∩ U_p crosses the cevian [c, r] ⊂ U_b of triangle s t r,
  which W9 forbids.
- **I_i, I_j, J_b.** The ray from a through c first meets cl U_i strictly below m ([a, c] misses cl U_i by W8). Sweep the
  crossing point x along m from c toward I_i. Every such ray meets U_i (the line ax separates s from r, so it crosses
  [s, r]), and its first-touch point can reach m only at a point of cl I_i, so it stays below m for every x ∈ I_j. That
  ray is in U_j at x, out of U_j at g (Ray Lemma 2), and back in U_j just past g (Ray Lemma 1): impossible for a convex set.
- **J_b, I_i, I_j.** Sweep x from c toward e, the left end of I_i. The first-touch points g(x) are in cl U_j
  (Ray Lemma 1) and lie between x and the ray's meeting point with [e, r], so g(x) → e. Then e ∈ cl U_j ∩ m = cl I_j,
  but I_j lies to the right of I_i. ∎

It fires on C5-053 (roles 1, 3, 5, 2, 6, 4), C5-072 (2, 5, 1, 6, 3, 4) and C5-076 (3, 4, 1, 6, 2, 5), and on none of the 63
codes drawn in the plane.

---

## 3. Forced-Facet Descent (a dimension bound)

**Claim.** Let C be a minimal code (its facets, its mandatory codewords and ∅). Pick k codewords as a base, and repeatedly
add every codeword that is a cut vertex separating two already-added codewords ω, ω′ in the graph of codewords containing
ω ∩ ω′ (edges join comparable codewords). If this reaches every facet, then C convex ⇒ C convex in R^(k−1).

**Proof.** Take a realization, cut down to a ball holding a witness of every codeword (this keeps the code). Walking along a
segment from a point of ω to a point of ω′, every codeword met contains ω ∩ ω′, and neighboring pieces have comparable
codewords, so the walk is a path in that graph and passes through every cut vertex. So all added codewords occur in the flat
F through the k base witnesses. The sets U_t ∩ F realize a convex code C′ ⊆ C that contains every facet, so it has the same
simplicial complex. Convex codes contain all their mandatory codewords (Curto et al.), so C′ ⊇ C, hence C′ = C, realized in
F, which has dimension at most k − 1. ∎

For C5-053, C5-072 and C5-076 three base codewords reach all five facets (bases 124/345/156, 246/123/145 and
2356/123/145), so each would be convex in the plane if convex at all, and Section 2 rules the plane out.
`checker/ffd.py` checks minimality before it runs.
