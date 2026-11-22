# OPS-CONSULT-13 — GPT turn 13 (2026-11-22 22:53-22:56 JST)

Topic (user's question): the three node-anchor losses. User: if we lose all of them, drop our assumptions and rethink; aren't there entrants who win everything? Consulted premise-free with facts (cap experiments, house eval gaps from REPORT-HOUSE).

GPT verdict:
- The "node wall" is NOT structural. GPT claimed the public leaderboard already shows multiple practice 6.0/6 = Elo 2112 entries (Kestrel 4K Chess v10, TinyChess 4KB v12, Kestrel 4KB Fast-Mate; PeSTO/PVS/MTD-bi/book/prepared defenses at the top). **VERIFIED BY MOCHI against the live API (submissions list, 2026-11-22 ~22:57): TRUE and stronger than claimed — 22 entries at 2112 in the top 100 alone; 15,764 ranked submissions. Winning titles show the methods: practice books, per-scenario variant tables ("all 640 gauntlet scenarios won offline"), PeSTO + PVS/TT/NMP/LMR at LIM 160k, 0x88 engines, 150k-node budgets, passed-pawn eval.**
- Confound warning: the 3 losses differ in opening AND colour, not just opponent strength. Controlled experiment required: same start + colour vs depth-4 to separate the causes.
- Draw-seeking is the most underrated lever: one draw vs 100k -> 3.5/6 = ~1364. Verify draw lines by playing them out (perpetual, threefold, 50-move, exchange-down, blockade; mind the 200-ply material adjudication).
- Anti-house steering is valid: the house lacks king-safety/passed-pawn/structure/mobility terms; steer into positions it misevaluates, and consider a short response-tree book over the 40 openings built from our own analysis.
- Same 50k can search better: move ordering / SEE / PV ordering; fix the actual tactical errors in the 3 losses rather than adding pruning methods.
- Adaptive budget (deterministic, position-based) instead of a flat cap raise.
- CORRECTION to turn 9: finals ~4.0/8 average is a house-benchmark comparison, NOT a top-20 prediction; with 22+ practice-perfect entries the prize cutoff may be higher. Practice-perfect and finals-general strength are separate goals.
- Priorities: (1) per-position analysis of the 3 losses (collapse ply, best move, draw possibility) — start with the loss closest to a draw; (2) house-weakness exploitation + draw routes; (3) teacher2+TT2 [already tried: REJECTED on screen 0.266/0.297]; (4) controlled comparison across house strengths; (5) search efficiency at 50k; (6) adaptive cap; (7) trial; (8) packaging.

Actions: loss-analysis lane (BRIEF-LOSSES) queued on PC executor #2 behind vm1-fix; 40-opening comparison lane already running on executor #1.
