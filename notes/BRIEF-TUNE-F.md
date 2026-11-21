# Tuning task: strengthen the tiny chess engine by SELF-PLAY PARAMETER TUNING

You are improving an existing engine with an automated learning loop, not by
hand-picking features (a sibling lane, tune-e, is doing hand-designed eval
work on the same base — do not duplicate that angle).

`main.py` in this folder (3250 bytes) is the strongest entry so far for the
make.fun tiny-chess-01 bounty: **practice Elo 1099**. The entry floor is
**1154** and the house baseline is **~1365**.
Anchors: depth-2=855, depth-3=1073, depth-4=1199, nodes-100k=1392,
nodes-250k=1497, nodes-500k=1596 Elo. The base searches a fixed cap of
50,000 nodes per move, worst move 2.335 s. `base.py` is a pristine copy of
the base engine — never modify it; it is your sparring reference.

## Your angle: learn the evaluation numbers from self-play

Two speed-only tunes plateaued at Elo 876; the bottleneck is evaluation
quality. Instead of hand-tuning, run an automated parameter search:

1. `main.py` is a packed blob (zlib+base64 exec wrapper). Decode it to the
   inner source. Identify every tunable numeric constant in the evaluation
   (piece values, piece-square table entries or their generators, phase
   weights, mobility coefficients, etc.). Refactor the inner source so the
   eval is driven by a single parameter vector (a params table the eval
   reads, or a template you regenerate). Keep a machine-readable copy of
   the current champion's parameters in this folder (e.g. `champion.json`)
   so a resumed session can continue.
2. Build a fast self-play arena in this folder (keep it here, /tmp is wiped
   on VM restart): two engine instances, FIXED node cap per move for tuning
   matches (use a lower cap, ~10-20k nodes, for volume), a fixed set of
   ~16-24 varied opening positions (FENs from common opening lines),
   colours alternated, games adjudicated by checkmate / resign threshold /
   move limit. Seeded randomness in the ARENA is fine; the ENGINE itself
   must stay deterministic (fixed node cap, no wall clock, no randomness).
3. Generations: champion + several mutants per generation (mutate 1-4
   parameters by roughly ±5-15%). Each mutant plays the champion at least
   30 games. Promote a mutant only if it scores >= 57%. Every generation,
   also play the champion against the ORIGINAL base (>= 30 games) and
   record it — this is your anti-overfitting anchor. If the champion's
   score vs base over the last 60+ games drops below 50%, revert to the
   last champion that beat base.
4. Checkpoint after every promotion: write the champion (repacked, single
   self-contained file, <= 4096 bytes) to `main.py`, and append one line
   per generation to `generations.log` (generation, mutation, scores vs
   champion and vs base). `main.py` must always hold the best-so-far
   champion, even if you are stopped mid-run.
5. Final validation of the champion at the REAL 50k cap: >= 40 games vs
   base, plus perft (move generation must stay exact — verify with the
   same 6-position perft the other lanes used; a mismatch disqualifies),
   plus NPS and worst-move time (keep worst move <= ~3 s; if the tuned
   eval is slower, trim the cap only as far as needed).

## Deliverables (in this folder)

- `main.py` — final champion, single self-contained file, <= 4096 bytes,
  perft-exact.
- `REPORT-TUNE-F.txt` — generations run, total games played, final
  champion-vs-base score at 50k cap, the parameter diff vs base, byte
  size, NPS and worst-move time.

Do NOT run the official practice trial yourself. Work steadily; volume of
games matters more than perfect bookkeeping, but keep `generations.log`
and the checkpoints current so the work survives a VM restart.
