# The 96 Open Codes of Remark 2.33

**Interactive viewer:** https://notitsme.github.io/neural-codes-96/ (click through all 96 codes; the 3D codes will spin)

When a rat, or another animal, walks into a room, some neurons fire when it is in a single specific spot. These are known as place cells. Each cell has its own location and that cell will fire when an animal is in its place field. You can then build a code by looking at which neurons are active together. If the code can come from one region per neuron with no dents or holes, then it is considered to be convex. We can thus ask the question: can this code be made into convex sets? In this case, for some of the smaller codes, nobody knew.

In 2025, Ahmed, Crepeau, Flores, Isekenegbe, Perez and Shiu pointed to 96 small codes (6 neurons, 5 maximal codewords each) whose convexity was previously unknown (Remark 2.33 of [arXiv:2510.20323](https://arxiv.org/abs/2510.20323), from Table 1 of the wheels paper by Ruys de Perez, Matusevich and Shiu, [arXiv:2108.04995](https://arxiv.org/abs/2108.04995)). This repo settles all 96 of those codes.

![Status of the 96 codes](docs/status.png)

## What's here

| Result | Codes | Visual |
|---|---|---|
| Convex, drawn flat in the plane | 63 | explicit polygons (rectangles, octagons, or 16-sided polygons) |
| Convex, needs exactly 3D | 19 | not drawable in the plane (proof below) + explicit 3D polytopes |
| Convex in 3D, plane still open | 2 (C5-011, C5-067) | explicit 3D polytopes |
| Convex in 4D (3D open) | 1 | C5-086, explicit 4D polytopes |
| Not convex | 11 | C5-044, 047, 050: first shown by P. Prabhakar (2026), reproduced here. C5-013, 033, 053, 072, 076, 085, 087, 095 are new findings, with proofs in [docs/proofs.md](docs/proofs.md) |

All 10 codes printed in Appendix A.1 of the wheels paper have been settled (9 convex in the plane or in 3D, plus C5-011).

### Convex codes

Each drawing is a certificate, and every region is written as a list of inequalities `lo < a·p < hi` with whole-number limits. The checker below uses those to reconstruct the code and verify that it is exact.

### Codes needing 3D

There are 19 codes with 3 regions which only overlap inside a shared codeword region, known as sunflowers. All the other parts of the code force the triangle to avoid that shared part. By the sunflower theorem ([arXiv:1810.03741](https://arxiv.org/abs/1810.03741), Cor. 2.1), this can't occur in the plane because a triangle with one corner in each of the three such regions in the plane must contain a point of the shared part. All 19 of these codes have a 3D drawing, which makes 3 its exact minimum dimension, the same behavior Jeffs found for his code T3.

### Non-convex

C5-044, C5-047 and C5-050 were first proven non-convex by Prayagh Prabhakar (S.-T. Yau High School Science Award, 2026) with his absorption criterion. We reimplemented that criterion independently, with a second proof.

The other eight (November 2026) are new results: written out in [docs/proofs.md](docs/proofs.md).

- **Rim rule** (works in any dimension): C5-033, 095, and 085 rise from that rule (033 and 095 directly; 085 from a simplified version of the code). The code makes the boundary of two regions cross within a third region, at a point where two regions are also touching but cannot meet.

- **Six-Role Wall** (the plane) + **Forced-Facet Descent**: C5-053, C5-072 and C5-076 can't be drawn in a plane, and three of their points force a drawing onto a flat plane, meaning they cannot be drawn in any dimension.

- **Two-shadow** and **twin-exit** arguments: C5-087 and C5-013. Both of these consider the crossing of two region boundaries, and they demonstrate that the code is required to have some codeword that it doesn't have.

These rules do not fire on any of the 85 convex codes, which shows it doesn't wrongly flag convex codes.


## Verify it yourself

```
pip install z3-solver
python3 checker/verify.py            # checks all 85 drawings (might take a few minutes)
python3 checker/verify.py C5-068     # checks one code
python3 checker/nonconvex.py         # re-checks the eight new non-convex proofs
```

The checker goes through every set of neurons with exact rational arithmetic and asks whether some point lies inside those exact regions. It will only accept a diagram if it generates the correct codewords, so if you alter any of the regions it will fail (which is how I tested the checker itself).


## Files

- `data/codes.json`: the 96 codes and their status
- `data/certificates/`: one drawing per convex code (`C5-xxx.json` octagons or rectangles in the plane, `_D8` 16-sided polygons, `_3D` polytopes, `_4D` polytopes)
- `checker/verify.py`: exact checker 
- `checker/nonconvex.py` (with `rim.py`, `sixrole.py`, `ffd.py`, `notch.py`): all the non-convexity rules
- `docs/proofs.md`: has the full proofs of the new results
- `docs/`: the interactive viewer

## What's left

All 96 codes have been finalised; 85 are convex and 11 are non-convex. What's left is the question of whether C5-011 and C5-067 can be drawn in the plane (2D) and whether C5-086 can be drawn in 3D or whether its minimal dimension is 4D.

Nov 7, 2026 results fingerprint (78 convex, 3 non-convex): `sha256 3bce792c2f3a20317ebd07bfb4aa7b0a29128851686689bd8930d6ba9c699c5f`
Nov 8, 2026 results fingerprint (85 convex, 11 non-convex): `sha256 a1004364ca0a9b755fa4359a7d16fa020d05e72fbe18ded909fc5750c6dbc1e2`
** files are in the Releases tab

AI tools (mostly Anthropic's Claude, bit of Google's Gemini) helped me set up this repo as well as ran the searches that found the drawings. It helped with coming up with proofs for proving the 11 codes non-convex. I decided what results got tested and when a result was fully done, as well as checked every proof myself. I also designed the look of the 3D viewer and wrote all of the published text in this repo.

Zaid Mohammed
