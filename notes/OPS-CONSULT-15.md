# OPS-CONSULT-15 — GPT turn 15 (2026-11-23 00:18-00:22 JST)

Topic: next move after the compare (four-way tie) and losses (no draw routes; control experiment) results. Consulted premise-free.

GPT verdict:
- Stop search-volume work. The 3 losses are not a search shortage (4x budget still loses; depth-4 also wins those setups). Causes: eval / tactical-danger blindness / opening progression.
- **FIRST: a rescue test, before building anything.** Force the house-1M best move at each collapse point (and 2-4 plies before), let our engine play on vs the original anchor and vs depth-4, and see whether the RESULT changes. Branch on the outcome: 1-move rescue -> minimal book/move rule; earlier-point rescue -> prevention eval; no rescue -> look earlier still.
- Priorities after the test: (1) king-safety defensive fix (Berlin + Slav; first check whether the two games share a misjudged feature; prefer a small king-danger eval of 2-3 features, measure its CPU cost; quiescence check-extension only if the eval route does not fit), (2) passed-pawn urgency (Philidor; independent small candidate), (3) small book branch as a parallel low-cost lane (branch a few plies BEFORE the collapse, not at it). Max 3 new candidates.
- Gates relaxed for this phase: rescue test -> regression (perft/determinism) -> timing (worst <=3.5 s target) -> 32-game screen (15/32 is NOT a clear regression; <=10/32 investigate first; a clear rescue may go to trial despite a slightly worse screen) -> trial-0 is the authority -> 40-opening comparison for generality. Trial 3.5/6+ protects; 3.0/6 compares on unknown openings; <=2.5/6 keeps BOOK.
- Schedule to the freeze (11/24 14:00): 0-3h rescue test; 3-11h king-safety candidate; 11-17h passed-pawn candidate; 17-24h book branch; 24-31h integrate only proven changes + 40-opening comparison; 31-38h packaging/freeze prep. Cut order if behind: book branch, then passed-pawn, then king-safety analysis. If nothing improves, BOOK stays (already qualified).
- Target: keep 3.0/6 while taking >=0.5 points from the 100k+ anchors for the first time.

Actions: rescue-test lane (BRIEF-RESCUE) launched on PC executor #1.
