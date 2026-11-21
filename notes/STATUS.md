# Status — 2026-11-21 14:00 JST

## Measured practice-trial results (6 games vs fixed anchors)

Anchors: depth-2 = 855, depth-3 = 1073, depth-4 = 1199,
nodes-100k = 1392, nodes-250k = 1497, nodes-500k = 1596 Elo.
Floor to reach the final: **1154**. House baseline (prize line): **~1365**.

| candidate | points | practice Elo | notes |
|---|---|---|---|
| A (first DeepSeek tune) | 0.5/6 | 708 | 25k nodes |
| B (first Hy4 tune) | 0.5/6 | 708 | 25k nodes; perft exact |
| tune-a (T2, eval+cap tune of A) | 2.0/6 | **1099** | 50k nodes, worst move 2.335 s — current best |
| candidate C (T3, speed tune of tune-a) | 1.0/6 | 876 | 1.83x NPS, cap 110k — faster but weaker |
| tune-b final (T1, speed tune of B) | 1.0/6 | 876 | ~85k NPS, cap 100k — faster but weaker |

All losses are by checkmate. Perft (6 positions, depths 1-3) is exact for
every candidate above.

## Bug found and fixed (T4, candidate C regression diagnosis)

Candidate C's quiescence search had a depth-cap condition `if dp>=2:` that
returned the static evaluation in the middle of unresolved capture
sequences. Fixed to `if dp>=99:` with the node cap lowered 110k -> 75k.
Perft exact, worst move 2.571 s. A 100-game equal-node match of FIXED vs
ORIG is running to quantify the gain.

## Lanes currently running

- **T4** (Hy4): candidate C repair validation (see above).
- **T5** (DeepSeek): hand-designed eval improvements on tune-a —
  tapered PST, mobility, king safety, passed pawns, bishop pair, rook on
  open file; each change validated by equal-node self-play vs the base.
  Brief: `notes/BRIEF-TUNE-E.md`.
- **T6** (DeepSeek): self-play parameter tuning of tune-a's eval
  constants — mutants play the champion (>= 30 games, promote at >= 57%),
  champion also plays the original base every generation as an
  anti-overfitting anchor. Brief: `notes/BRIEF-TUNE-F.md`.

## Questions for the advisor

1. From 1099 toward 1154 and then 1365: what gives the most Elo in a
   4 KB-class alpha-beta engine — eval terms, search extensions, or
   something else? Please rank.
2. Self-play parameter tuning (T6): pitfalls to avoid — game counts,
   tuning node cap vs final cap, opening diversity, overfitting checks.
3. Code review of `engines/tune-a_inner.py`: latent bugs or weak
   patterns of the kind the qsearch cap bug was (things that silently
   cost strength), and anything that risks the 10 s/move limit or
   determinism.
