# OPS-CONSULT-10 — GPT turn 10 (2026-11-22 19:47-19:51 JST)

Consulted BEFORE asking the user (user correction 19:46: consult GPT first; no leading premise — facts and options only).

Facts given: teacher1 rejected (screen 0.438); teacher2 (null-move pruning) all gates pass, screen 0.516, trial-0 3.0/6=1279 same seed/pattern as BOOK, no book; BOOK 1279 includes the d1h5 book firing in game 3; TT2 gates pass, screen 0.500, no trial; BOOK pinned (submission 2, prize_eligible true); finals = 6 instances x 8 games, openings redrawn; freeze 11/24 14:00, deadline 11/25 02:00.

GPT verdict:
1. Keep the BOOK pin for now. If forced to pick one today, GPT would pick teacher2 on finals expectation — but do not rush; test the HYBRID first. teacher2's solo submission decision waits for the HYBRID result.
2. HYBRID (SPD base + null-move + book lookup) = top-priority experiment, max 4h. FIRST compare game 3 of BOOK vs teacher2 (where they diverge; does teacher2 reach the book FEN; what does it play there). Do not force d1h5 blindly. HYBRID outcomes: 3.5/6+ top final candidate; 3.0/6 compare vs teacher2 on unknown openings/long games; 2.5/6 keep BOOK pin; <=2.0/6 reject HYBRID, back to teacher2. Null-move endgame (KP zugzwang) risk noted; prefer correct integration over new search changes.
3. TT2 trial: YES, run it (after HYBRID, or first if HYBRID not ready). Screen-even does not imply trial-even; TT2 is the first fairly-testable TT (capped, stable in long games). 2.5/6+ -> protect, consider teacher2+TT2 integration; <=2.0/6 -> do not add TT2 to HYBRID (exception: clear search-efficiency gains).
4. Extra: unknown-opening comparisons on PC (teacher2 vs BOOK ~80 games both colours from the 40 openings; also vs depth-4 / nodes-100k; 150-200 ply timing/RSS; book-position-excluded pure-search comparison). Analyse WHY teacher2 beat depth-4 (search logs: real depth gain vs one lucky move).
5. Schedule: now+4h HYBRID; next 6-10h unknown-opening comparisons; 11/23 tuning one change at a time; 11/24 morning final gates; freeze 14:00; submit by 22:00.

Mochi's game-3 verification (from both trials' state exports, done before launching the lane): identical through ply 20; BOOK plays h2h4 (ply 21) and the book fires at ply 35 (d1h5), 145-ply win. teacher2 plays b1c3 at ply 21, NEVER reaches the book FEN, wins in 69 plies by a different route. In the hybrid the book would not have fired in game 3 either; it is fallback insurance only.

Actions taken 2026-11-22 19:52 JST: HYBRID lane launched on PC executor #1 (job hybrid-1122, claimed; folder F:\muse\tiny-chess-hybrid, brief includes the divergence file). TT2 trial-0 launched on the VM (tmux trial-tt2, port 18117, main_tt2.py 3,026B official compress). Pin unchanged (BOOK).
