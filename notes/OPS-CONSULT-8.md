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

Reply: pending (to be appended when received).
