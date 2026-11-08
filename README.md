# The 96 Open Codes of Remark 2.33

**Interactive viewer:** https://notitsme.github.io/neural-codes-96/ (click through all 96 codes; the 3D ones spin)

Every time an animal walks through a room, a small group of neurons called place cells fires in a pattern, and each one fires only when the animal is inside its own patch of space, its place field. If you write down which neurons fire together, you get a neural code. The code is called convex when it can come from place fields that are convex (open regions with no dents or holes, like a disk or a polygon). The question is whether a given list of codewords can be drawn with convex regions at all, and for some small codes nobody knows the answer.

In 2025, Ahmed, Crepeau, Flores, Isekenegbe, Perez and Shiu pointed to 96 small codes (6 neurons, 5 maximal codewords each) whose convexity nobody knew (Remark 2.33 of [arXiv:2510.20323](https://arxiv.org/abs/2510.20323), from Table 1 of the wheels paper by Ruys de Perez, Matusevich and Shiu, [arXiv:2108.04995](https://arxiv.org/abs/2108.04995)). This repo settles 94 of them.

![Status of the 96 codes](docs/status.png)

## What's here

| Result | Codes | How it's shown |
|---|---|---|
| Convex, drawn in the plane | 63 | explicit polygons (rectangles, octagons, or 16-sided polygons) |
| Convex, needs exactly 3D | 19 | not drawable in the plane (proof below) + explicit 3D polytopes |
| Convex in 3D, plane still open | 2 (C5-011, C5-067) | explicit 3D polytopes |
| Not convex | 9 | C5-044, 047, 050: first shown by P. Prabhakar (2026), reproduced here. C5-033, 053, 072, 076, 085, 095: new, proofs in [docs/proofs.md](docs/proofs.md) |
| Convex in 4D (3D open) | 1 | C5-086, explicit 4D polytopes |
| Open | 2 | C5-013, C5-087 |

All 10 codes printed in Appendix A.1 of the wheels paper are among the solved ones (9 convex in the plane or in 3D, plus C5-011).

### Convex codes

Each drawing is a certificate: every region is written as a list of inequalities `lo < a·p < hi` with whole-number limits, so nothing depends on rounding. The checker below rebuilds the exact code each drawing makes and compares it with the target.

### Codes that need exactly 3D

For 19 codes, three of the regions only ever overlap inside one shared codeword (a "sunflower"), and the rest of the code forces any triangle connecting them to stay inside regions that never touch that shared part. Jeffs' sunflower theorem ([arXiv:1810.03741](https://arxiv.org/abs/1810.03741), Cor. 2.1) says a triangle with one corner in each of three such regions in the plane must contain a point of the shared part—so no flat drawing exists. Each of these 19 still has a 3D drawing, which makes 3 its exact minimum dimension, the same behavior Jeffs found for his code T3.

### Not convex

C5-044, C5-047 and C5-050 were first proven non-convex by Prayagh Prabhakar (S.-T. Yau High School Science Award, 2026) with his absorption criterion. We reimplemented that criterion independently, and his split-cover pinch argument gives a second, separate proof for all three.

Six more are new (November 2026), from two new arguments written out in [docs/proofs.md](docs/proofs.md):

- **Rim rule** (any dimension): C5-033 and C5-095 directly, and C5-085 through a smaller code that any drawing of it would also draw. If the code forces region i minus region j inside k and j minus i inside l, but k and l never overlap inside region m, the boundaries of i and j end up crossing at a point inside m that touches both k and l, which can't happen.
- **Six-Role Wall** (the plane) plus **Forced-Facet Descent**: C5-053, C5-072 and C5-076 can't be drawn in the plane, and three of their points already force the whole code onto one plane, so they can't be drawn in any dimension.

Neither rule fires on any of the 85 codes that have drawings.

## Verify it yourself

```
pip install z3-solver
python3 checker/verify.py            # checks all 78 drawings (a few minutes)
python3 checker/verify.py C5-068     # one code
python3 checker/nonconvex.py         # re-checks the six new non-convexity proofs and their controls
```

For every set of neurons, the checker asks Z3 (exact rational arithmetic) whether some point lies inside exactly those regions. A drawing passes only if the codewords it produces match the target code exactly, with nothing missing and nothing extra. Editing a single region in a certificate makes it fail, which is how we tested the checker itself.

## Files

- `data/codes.json`: the 96 codes and their status
- `data/certificates/`: one file per convex code (`C5-xxx.json` octagons or rectangles in the plane, `_D8` 16-sided polygons, `_3D` polytopes)
- `checker/verify.py`: the exact checker
- `checker/nonconvex.py` (with `rim.py`, `sixrole.py`, `ffd.py`): the non-convexity rules
- `docs/proofs.md`: full proofs of the new results
- `docs/`: the interactive viewer (served by GitHub Pages)

## Still open

Two codes are still open: C5-013 and C5-087. Both look non-convex, and there are draft proofs for both that are being checked now. The newest drawings (038, 059, 060, 067, 069, 094 in 3D and 086 in 4D) were all built by hand, and several have a codeword that only lives on a flat plane or in a very thin slab, which is why the earlier computer searches missed them.

Results fingerprint (Nov 7, 2026 bundle): `sha256 3bce792c2f3a20317ebd07bfb4aa7b0a29128851686689bd8930d6ba9c699c5f`

Claude (Anthropic's AI) helped me set up this repo and with some of the analysis. I checked every result myself, and every drawing passes the exact checker above.

Zaid Mohammed
