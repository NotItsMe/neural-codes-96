# Proofs for the eight new non-convex codes

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


---

## 4. Tools for the last two codes

### Outside results used

1. **Separation.** Two disjoint nonempty convex sets in R^d are separated by a hyperplane (Rockafellar, *Convex Analysis*, Thm 11.3). An open set lying in a closed half-space lies in the open half-space.
2. **Line-segment principle** (Rockafellar Thm 6.1). If x ∈ ri C and y ∈ cl C, then [x, y) ⊂ ri C.
   **Thm 6.5.** If ∩ ri C_i ≠ ∅, then cl ∩C_i = ∩ cl C_i.
   **Cor 6.5.1.** If an affine set M meets ri C, then cl(M∩C) = M ∩ cl C.
   **Corner-segment rule (consequence).** Let U, V be open convex with U∩V ≠ ∅ and x ∈ cl U ∩ cl V. Then x ∈ cl(U∩V), and (x, p] ⊂ U∩V for every p ∈ U∩V.
3. **Tietze–Nakajima (1928).** A closed, connected, locally convex subset of R^n is convex.
4. **Zajíček (1979)**, Czech. Math. J. 29, 340–348. For a convex φ on R^d, the set J_k(φ) = {dim ∂φ(x) ≥ d−k} can be covered by countably many DC_k sets ("c-c hypersurfaces of dimension k"). (See also Alberti 1994.)
   **Used with d = 2, k = 1.** The non-smooth points of the boundary of a convex body in R³ lie on countably many Lipschitz curves.

### Lemma 0.1
Let U, V be open convex with U∩V ≠ ∅. Then U∪V = int cl(U∪V).

*Proof.* Suppose z ∈ int(cl U ∪ cl V) but z ∉ U∪V.
- If z ∈ cl U ∩ cl V: both sets omit z, so cl U ⊂ z + cl T_U and cl V ⊂ z + cl T_V, and each closed cone lies in a closed half-space. These two cones cover a ball around z, hence all of R^d. Two closed convex cones, each in a closed half-space, cover R^d only if they are opposite closed half-spaces. Then U and V lie in opposite open half-spaces, so they don't meet. Contradiction.
- If z lies in only one closure: near z, cl U ∪ cl V equals that closure, and int cl U = U.

∎

### Lemma 0.2 (crease existence)
Let U, V be open convex, overlapping, with U∪V not convex. Then Z := cl(U∖V) ∩ cl(V∖U) ≠ ∅.

*Proof.* Suppose Z = ∅. Take x ∉ cl(U∖V) and an open ball N around x missing U∖V. Then N ∩ cl U ⊂ cl(N∩U) ⊂ cl V. So K = cl U ∪ cl V is locally convex everywhere. K is closed and connected, so it is convex by Tietze–Nakajima. Then int K = U∪V (Lemma 0.1) is convex. ∎

The same holds inside any 2-plane Π, applied to U∩Π and V∩Π. A crease point found inside Π lies in Z, because Π-closures are contained in ambient closures.

### Lemma 0.3 (generic 3-flat restriction)
Let {U_i} be an open convex realization of a code C in R^d with d ≥ 3, and let F be the affine 3-flat through chosen points q_1, …, q_4 (enlarge or perturb if they are dependent). Then {U_i ∩ F} realizes, in F ≅ R³, a subcode C' ⊆ C that contains the codewords of the q_j.

Every step below uses only:
- facts of the form "no codeword ⊇ S" or "every codeword ⊇ S contains T", which pass to subcodes; and
- nonemptiness of named cells, which the q_j supply.

So it is enough to argue in R³. (A planar drawing becomes a 3-D one by taking U_i × R.)

### Lemma 0.4 (shift invariance)
If an open convex cone K contains a nonempty open set O invariant under translation by l, then K + l = K.

*Proof.* Take k ∈ K and o ∈ O. For small λ, k'' = (k − λo)/(1−λ) ∈ K. Then k + tl = (1−λ)k'' + λ(o + (t/λ)l) ∈ K. ∎

Notation: for x ∈ cl U, the cone T_U(x) = {v : x + εv ∈ U for some ε > 0} is an open convex cone. If v ∉ T_U(x), then x + εv ∉ U for every ε > 0 ("a ray that leaves never comes back").

---

**Frontier point.** (Written for C5-087 with crossing sets U1, U4 and bridge U3; for C5-013 read U3, U4 and bridge U5.)
1. Take Π through a ∈ 123, b ∈ 3456 and c ∈ U1∩U4, not collinear. Let A' = U1∩Π, B' = U4∩Π, core' = A'∩B', and let T be the triangle abc.
2. a ∉ cl U4, because the open set U3∩U1 misses U4. Likewise b ∉ cl U1. [a,b] ⊂ U3, and U3 misses cl(core'). Set Q = cl(core') ∩ T.
3. [c,a] ⊂ A' and [c,a] ∩ Q = [c, p1] with p1 ∈ A' ∩ ∂B'. Likewise p2 ∈ B' ∩ ∂A'.
4. Let Γ be the arc of ∂Q from p1 to p2 avoiding c. Γ misses [a,b], so Γ∖{p1, p2} ⊂ int T and Γ ∩ core' = ∅.
5. Γ∩A' and Γ∩B' are disjoint and relatively open, and they contain p1 and p2 respectively. Γ is connected, so there is x ∈ Γ with x ∉ U1∪U4 and x ∈ cl U1 ∩ cl U4 ∩ cl(U1∩U4).
6. If U1∩Π and U4∩Π had a common supporting line through x, they would lie on the same open side, since they overlap. Then a, b, c would be on that side, so T ⊂ open side, yet x ∈ T. Contradiction.
7. Hence the slice cones are not nested and their union is not convex. Therefore **T1 ∪ T4 is not convex** in R³, and T1∩T4 ≠ ∅.

**Common invariant line.**
- **Polyhedral.** x lies in relint F1 ∩ relint F4 for faces F1, F4, and relint(F1∩F4) ∋ x (Thm 6.5). Only finitely many such intersections are points, and a generic Π in the open family 𝒫 misses them. So dim(F1∩F4) ≥ 1, and its direction lies in the lineality of both cones.
- **Curved.**
  - *Smooth at x on both boundaries:* T1 and T4 are open half-spaces. Equal normals would make T1 = T4; opposite normals would make them disjoint. So the boundary planes meet in a line l, and both cones are invariant along l.
  - *Ridge points:* let Y be the points of ∂U1∩∂U4 where at least one boundary is non-smooth. By Zajíček (1979), Y is covered by countably many Lipschitz curves γ_n. Parametrize each in a boundary chart as (s, g(s), f(s, g(s))), so γ_n' ≠ 0 wherever it exists.
  - Let B_n be the set of parameters in γ_n⁻¹(Y) that are not Lebesgue density points, or where γ_n is not differentiable. Then L¹(B_n) = 0, so E := ∪ γ_n(B_n) has H¹(E) = 0.
  - For every normal direction, the projection of E has length 0. Planes meeting E therefore form a null set, while 𝒫 is open and nonempty. So pick Π ∈ 𝒫 with Π∩E = ∅.
  - If x ∈ Y, then x is a good point of some γ_n. Points of Y ⊂ cl U1 ∩ cl U4 approach x from both sides along γ_n, so ±γ_n'(t) ∈ cl T1 ∩ cl T4. Then T_i = int cl T_i is invariant along l = γ_n'(t).
- In both cases T1 and T4 are l-invariant. By Lemma 0.4 so are T2 ⊇ T1∖cl T4, T5 and T6 (both ⊇ T4∖cl T1), because these differences are nonempty open l-invariant sets.

---

## 5. C5-087 is not convex (two-shadow argument)

**C5-087.** 1245 1246 1456 3456 123 124 145 146 456 12 14 3 ∅.

**Codeword facts** :
- (F1) No codeword contains {2,5,6}.
- (F2) Every codeword with 1 and not 4 contains 2 (123, 12).
- (F3) Every codeword with 4 and not 1 contains 5 and 6 (3456, 456).
- (F4) Every codeword with 5 or with 6 contains 4.
- (F5) No codeword contains {1,3,4}.

**Proof.** Work in R³ (Lemma 0.3 with points of 123, 3456, 1245 and 1246). Write V = U5∩U6.

1. By (F1), U2 ∩ V = ∅, so a plane H has U2 ⊂ H⁺ and V ⊂ H⁻ (open sides).
2. By (F2), U1∖U4 ⊂ U2 ⊂ H⁺. By (F3), U4∖U1 ⊂ V ⊂ H⁻. Hence U1∩H = U4∩H =: C, a relatively open convex set in H.
3. By (F4), U5 ⊂ U4 and U6 ⊂ U4. A 1245 point lies in H⁺ and a 3456 point lies in V ⊂ H⁻, both in U5, so T5 := U5∩H ≠ ∅. Likewise T6 ≠ ∅ (1246 and 3456). T5∩T6 ⊂ V∩H = ∅. And T5, T6 ⊂ U4∩H = C.
4. T5 and T6 are disjoint, relatively open and convex in H, so a line m ⊂ H has T5 and T6 on opposite open sides. For t5 ∈ T5 and t6 ∈ T6, the segment [t5, t6] ⊂ C crosses m. **So m meets C = ri C.**
5. Let a ∈ 123 and b ∈ 3456. The segment [a,b] ⊂ U3, and by (F5) U3∩U1∩U4 = ∅, so [a,b] leaves U1∪U4. U1∩U4 ≠ ∅ (1245). By Lemma 0.2, Z := cl(U1∖U4) ∩ cl(U4∖U1) ≠ ∅.
6. **Locating Z.**
   - By step 2, Z ⊂ cl H⁺ ∩ cl H⁻ = H.
   - Z misses U1 and U4, since each is open and disjoint from one of the two differences.
   - By Cor 6.5.1, H∩cl U1 = cl C. So Z ⊂ cl C ∖ C.
   - Let e ∈ Z. Take p5 in the 1245 cell (in U5∩H⁺) and v ∈ U4∖U1 ⊂ V ⊂ U5 with v → e. The segment [p5, v] ⊂ U5 crosses H at points of T5 that tend to e. So e ∈ cl T5, and similarly e ∈ cl T6. Hence e ∈ cl T5 ∩ cl T6 ⊂ m.
   - So Z ⊂ (cl C ∖ C) ∩ m.
7. Since m meets ri C, Cor 6.5.1 (inside H) gives m ∩ cl C = cl(m∩C). The set m∩C is an open interval, so **|Z| ≤ 2.**
8. Every plane Π through a ∈ 123, w ∈ U1∩U4 and b ∈ 3456 (not collinear) contains a point of Z: apply Lemma 0.2 inside Π, as in step 5. The triples (a, w, b) for which a given point z lies in aff{a, w, b} form the zero set of a nonzero polynomial on an open subset of R⁹. So some triple gives a plane missing both points of Z. Contradiction. ∎

---

## 6. C5-013 is not convex (twin-exit argument)

**C5-013.** 2346 134 135 456 12 13 34 46 1 2 5 ∅.

**Roles:** A = U3, B = U4, bridge U5, X = U1, Y = U6, Z = U2.

**Facts** :
- (a) U3∖U4 ⊂ U1 (135, 13).
- (b) U4∖U3 ⊂ U6 (456, 46).
- (c) U2∩U3 ⊂ U4 and U2∩U4 ⊂ U3 (2346 is the only codeword with 2 and 3, and the only one with 2 and 4).
- (d) U3∩U6 ⊂ U2.
- (e) No codeword contains 123.
- (f) 12 is a codeword.
- (g) No codeword contains 345.

**Proof.** Work in R³ (Lemma 0.3 with points of 135, 456, 2346 and 12).

1. **Frontier point.** The frontier-point construction below (with U3, U4 in the roles of U1, U4 there, and U5 as the bridge) uses only:
   - A, B open convex and overlapping (2346 ⊂ U3∩U4);
   - a ∈ U5∩U3 and b ∈ U5∩U4;
   - U5∩U3∩U4 = ∅, by (g).

   They give x0 ∈ ∂U3∩∂U4 ∩ cl(U3∩U4) and a line l with K3 and K4 l-invariant, K3∪K4 not convex, and K3∩K4 ≠ ∅.
2. **The other cones.**
   - K1 ⊇ K3∖K4, by (a).
   - K4 meets ∂K3. Take d ∈ ∂K3 ∩ K4. Then x0 + εd ∈ U4∖U3 ⊂ U6, so d ∈ K6. K6 is open and contains a boundary point of K3, so K3∩K6 ≠ ∅.
   - By (d), K3∩K6 ⊂ K2, so K2 ≠ ∅.
   - K6 ⊇ K4∖cl K3 and K1 ⊇ K3∖cl K4, both nonempty open l-invariant sets. So K6 and K1 are l-invariant (Lemma 0.4), and so is K2 ⊇ K3∩K6.
3. **Quotient.** K3 = (a3, b3) and K4 = (a4, b4) with a3 < a4 < b3 < b4.
   - x0 ∉ U2. Otherwise a ball around x0 lies in U2, and (c) forces U3 = U4 on that ball, so K3 = K4. Hence K2 is a proper open arc.
   - By (c), K2∩K3 ⊂ K4 and K2∩K4 ⊂ K3. So a4 ∉ K2 (it lies in K3∖K4) and b3 ∉ K2.
   - K2∩K3 ≠ ∅ and K2∩K3 ⊂ K3∩K4 = (a4, b3).
   - K2 is a connected subset of S¹∖{a4, b3} that meets (a4, b3), so **K2 ⊂ (a4, b3) ⊂ K3.** 
4. **Corner segment.**
   - x0 ∈ cl U1 (K1 ≠ ∅) and x0 ∈ cl U2.
   - Take p ∈ U1∩U2 (cell 12). By Thm 6.5, x0 ∈ cl(U1∩U2), and (x0, p] ⊂ U1∩U2.
   - Since K2 ⊂ K3 holds in R³ (both are l-invariant), p − x0 ∈ K3. So x0 + ε(p − x0) ∈ U1∩U2∩U3, contradicting (e). ∎

Both arguments were also turned into abstract rules (`checker/notch.py`) and run on all 96 codes under every choice of roles: they fire on these two codes and on codes already known to be non-convex, and never on any of the 85 codes with drawings.
