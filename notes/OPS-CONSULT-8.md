# OPS-CONSULT-8 — full method inventory after rule clarifications (2026-11-22)

Posted to the ChatGPT thread "チェスエンジン改良優先順位" as turn 8 on
2026-11-22 ~15:09 JST, at the user's instruction ("網羅的に試してるんだと
思った、ほかの手法も踏まえてgptと相談してきて").

## Rule clarifications verified in RULES.txt before posting
- Opponent (house engine) analysis is NOT prohibited. The house engine
  (Sunfish-derived) and the 2,720-game calibration set ship in the kit.
  Only exploiting env/scorer bugs is banned.
- Reinforcement learning / self-play tuning is NOT prohibited. Banned:
  (1) the entry program making model calls during a trial (DQ),
  (2) nondeterminism — every move must derive from the position, the
  game's moves and the trial seed only. Embedding constants learned
  offline in our own recorded sessions is allowed.
- Finals: 8 games (nodes-1M=1667, nodes-2M=1712 added), openings redrawn
  from the 40-opening book, 6 instances. General strength transfers;
  single-position books have no reproduction guarantee.

## State at posting
- Best 1099 (tune-a / SPD / cap65 tied), floor 1154, gap 0.5 pt.
- TT candidate trialed on the VM: 1.0/6 = 876 REJECTED. Early think_ms
  ~2 s growing to a max of 45,368 ms inside long games; 4 time losses.
  Suspected cause: unbounded TT growth (the lane's own report flagged
  it). Rehearsal (fresh state per FEN) does not expose this failure mode.
- Book candidate (verified d1h5, gauntlet replay 3.0/6) packaging on PC.
- Fixed candidate (rook open-file + PV ordering) screen 14.0/32; VM
  rehearsal PASS (worst 2.32 s); VM trial launched 15:10 JST.
- Tried: speed +27% (Elo unchanged), caps 65k/75k/100k (tie/876/0),
  R_mob + queen mobility (screen positive, trial 876), T7 bug fixes
  (997), T6 coarse variant screening (no significant gain, parked).

## Untried (the consultation's subject)
- Self-play weight learning (Texel / TD) — T6 was variant screening,
  not a weight-learning loop.
- House-engine implementation analysis.
- PVS, LMR, null-move pruning, check extensions, aspiration windows.
- PeSTO-style PST redesign, king-attack eval.
- Draw-route search (repetition / 50-move).
- Position-adaptive node budgets.

## Questions asked
1. Prioritize the untried methods by remaining time (~47 h to freeze)
   and expected value.
2. Design the self-play weight-learning loop (parameters, game count,
   engine usage, anti-overfit, validation).
3. Is house-engine analysis worth it; what to look at.
4. Next move if TT / book / fixed all fail.
5. Completeness checklist for methods legal within 4 KB, deterministic,
   stdlib-only.

## GPT reply (received 2026-11-22 15:13 JST) — summary

Verdict: run three lines in parallel — house-engine analysis, Texel-style
weight learning, and search improvements (PVS/LMR) — instead of repeating
generic tweaks. T6 was variant screening, not weight learning.

Priorities (47 h to freeze):
1. House-engine analysis + loss-cause identification (2–4 h). Audit
   calibration.json first: does it contain full games/FENs or only
   results? The house engines share one search/eval structure and differ
   mainly by depth/node budget; eval = material + PST + bishop pair,
   with qsearch, TT, capture/killer ordering, repetition/50-move.
   Start with a depth-3 vs depth-4 divergence study; use strong house
   engines (nodes-500k/1M) as teachers to classify SPD's errors.
2. Texel weight learning (6–10 h): keep SPD's eval structure, learn only
   its existing constants (~16–24 params: piece values, mid/end PST
   coefficients, bishop pair, passed pawn, rook files). 150–300 self-play
   games at 10–20k nodes from the 40 openings (both colours), 8–20
   positions per game → 2,000–5,000 positions; per-game weight
   normalisation; sigmoid loss with K calibrated once; L2 pull to the
   current values; coordinate descent ±2/±4/±8; split 70/15/15 by
   opening pair; never train on trial-0's 6 games. TEX-A first; TEX-B/C
   only if A disappoints. TD learning later, if at all, seeded from
   Texel weights.
3. PVS + conservative LMR (4–6 h): PVS alone, LMR alone, then combined.
   LMR spec: depth ≥ 3, quiet moves from the 3rd onward, never in check /
   captures / promotions, reduction 1 ply, re-search on alpha improvement.
4. Existing candidates continue: BOOK first in the trial queue (replay
   3.0/6 is the closest route to 1154), FIX behind it.
5. Null-move pruning after LMR; PeSTO PSTs folded into the Texel lane;
   adaptive node budgets as a small experiment; aspiration windows last.
   TD / small NNUE = research only.
- TT failure is an implementation failure, not a method failure: cap the
  table (4,096–16,384 entries), depth-preferred replacement, reset
  per game, long-game (150–200 ply) timing/memory tests. Cheap fix worth
  one retry; if still weak, drop it.
- If everything fails: teacher-based error mining (collect SPD's error
  positions, classify eval-vs-search with strong house engines, fix only
  the common failure classes).
- Combinations: BOOK + best general candidate for the finals; never bulk
  -merge untested changes; learned weights do not transfer across changed
  eval structures without re-learning.
- Schedule: 0–4 h book trial + house audit; 4–14 h Texel + PVS/LMR;
  14–26 h TEX-A trial + comparisons; 26–38 h integration + finals
  hardening; 38–47 h final verification; freeze 11/24 14:00; submit by
  22:00. PC split: 3 cores Texel games, 2 cores house analysis, 1 core
  orchestration. Keep the trial VM free of training load.
- Packaging gates stay a separate mandatory track; record every training
  stage inside genuine agent sessions for the authorship gate.

## Adoption (Mochi, 2026-11-22)
Adopted essentially as proposed. Actions taken the same hour:
- VM trial queue reordered: FIX (running) → BOOK (as soon as the PC
  packaging lane delivers) → TEX-A → PVS/LMR.
- PC lane HOUSE (executor #1, job house-analysis-1122): kit audit +
  house implementation report + depth-3/4 divergence + ranked weakness
  list. Analysis only, no code changes.
- PC lane TEXEL (executor #2, job texel-1122, queued behind book-pack):
  GPT's Texel v1 design as briefed (calibration audit first, self-play
  data, existing constants only, TEX-A + full verification).
- PC lane PVSLMR: briefed and staged (F:\muse\tiny-chess-pvslmr);
  job drops after the HOUSE lane finishes (executor #1 is serial).
- Capped-TT retry: noted, not launched (lane slots full); revisit if a
  slot frees or PVS/LMR finishes early.
One correction to GPT's framing: its claim that the submission gates are
still open is outdated — submission 1 already proved the packaging route
end-to-end (prize_eligible: true server-side). The gates remain a
checklist item for the final submission, not a blocker.
