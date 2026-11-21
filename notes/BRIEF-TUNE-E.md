# Tuning task: strengthen the tiny chess engine in this folder (main.py) — eval angle

You are improving an existing engine. `main.py` in this folder (3250 bytes) is the
strongest entry so far for the make.fun tiny-chess-01 bounty: **practice Elo 1099**
(2.0 points in 6 games against fixed anchor engines; it beats depth-2 and draws
depth-3). The entry floor is **1154** and the house baseline is **~1365**.
Anchors: depth-2=855, depth-3=1073, depth-4=1199, nodes-100k=1392,
nodes-250k=1497, nodes-500k=1596 Elo. It searches a fixed cap of 50,000 nodes
per move, worst move 2.335 s.

## Why this angle

Two speed-only tunes plateaued at practice Elo 876 despite large NPS gains
(tune-b: 6.6x NPS, 100k cap, still 876; candidate C: 1.83x faster, still 876).
Speed is NOT the bottleneck. The engine loses to depth-3 and above by checkmate,
i.e. it misevaluates positions and walks into tactics. Your angle is
**evaluation quality and search quality**, not speed.

## What to do

1. `main.py` is a packed blob (2-line zlib+base64 exec wrapper). Decode it to the
   inner source first, work on the inner source, and repack with the same kind
   of wrapper at the end. Final file must be a single self-contained file.
2. Read the current eval carefully. Then try, one at a time, the highest-value
   eval improvements that fit the byte budget: tapered middlegame/endgame
   piece-square tables, mobility, king safety (pawn shelter / attacks on the
   king zone), passed-pawn bonuses, bishop pair, rook on open/semi-open file.
   Pick the subset that fits and helps; do not add everything.
3. Consider small search-quality additions only if bytes allow and self-play
   proves them: check extensions, better capture ordering is already there.
4. **Validate every change with equal-node self-play against the tune-a base**
   (the original main.py — keep a copy as `base.py` before editing). Use a
   fixed-node match harness (e.g. 20-50 games at cap 50000, alternating colours,
   a few different openings). Keep a change only if it wins the match;
   revert losers. Record the score of each tested change in the report.
5. Measure NPS and worst-case move time after your changes. If eval got slower,
   lower the node cap only as far as needed to keep the worst-case move at or
   below ~3 s on this machine (hard env limit is 10 s per move; leave margin).
   The cap must remain a fixed node count: determinism is mandatory, no
   wall-clock decisions, no randomness.

## Hard requirements (unchanged)

- main.py ≤ 4096 bytes total when you finish. Python 3.13, standard library
  only, reads/imports no other file.
- Perft must stay exact. The checker is at `../perft_check.py` (run it against
  your main.py's move generator the same way it does; if its interface does
  not fit, write your own perft test with the same 6 positions at depths 1-3
  and the same expected counts). A single mismatch = failure; fix before
  anything else.
- Never crash, never resign; keep the fallback to the env's first legal move
  on unexpected errors.

## Deliverables in this folder

- The improved `main.py`.
- `REPORT-TUNE-E.txt`: for each eval change tried, the self-play score vs the
  tune-a base (games, wins/draws/losses); final byte count; node cap and its
  measured worst-case move time; perft result; a short list of what changed.

Do NOT run the full practice trial yourself; that is measured centrally.
Finish with the report as your final message.
