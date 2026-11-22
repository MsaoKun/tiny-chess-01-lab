# OPS-CONSULT-12 — GPT turn 12 (2026-11-22 21:07-21:09 JST)

Topic: the user's proposal — brute-force on PC with loose limits, build strength first, then squeeze into the 10 s budget. Consulted premise-free (proposal + transfer risk as an open question) BEFORE adopting anything; user correction 21:06/21:08 fixed the order: consult -> decide -> arrange.

GPT verdict:
- Direction agreed, but NOT "optimise at high nodes, then drop to 50k". Adopt multi-budget testing instead: main evaluation at 50k (the real budget), auxiliary 25k/75k (robustness), 150k+ only for cause analysis of positions the 50k engine gets wrong.
- Transfer risk is SERIOUS for this engine, especially search changes: null-move R/depth and LMR = very high risk; TT size/replacement = high; eval weights = medium-high. The earlier LMR case (reached deeper, trialed 876) is direct evidence. PC compute should mostly buy MORE evaluation at the real 50k condition (more candidates, openings, opponents), not a higher cap.
- Priorities: (1) HYBRID trial result; (2) teacher2+TT2 integration (bookless first, BOOK added last only if it works); (3) 40-opening both-colours comparisons; (4) budget-sensitivity 25k/50k/75k; (5) high-node teacher analysis; (6) high-node parameter tuning — deprioritised.
- High-node use that DOES transfer: teacher analysis (find positions where 50k errs and 150k+ is right; classify: search shortage / pruning error / eval error; fix at 50k).
- Interaction cautions for teacher2+TT2: null-move state restoration, no TT poisoning from null-window results, cut stacking, long-game stability, null-move effect surviving TT ordering. Two 3.0/6 parents do NOT imply a 3.5/6 child.
- 32-game screens are weak evidence (16.5/32 proves little); screens prune, trial-0 promotes.
- If tuning anything, limit to 3 families, one change at a time, decided at 50k: null-move (min depth, R, endgame suppression), TT (capacity 4k/8k/16k, replacement), adaptive budget (40k/50k/60k by deterministic position features, never wall clock).
- Schedule for the remaining ~41 h: 0-3 h HYBRID trial + protect; 3-10 h teacher2+TT2 + 50k evaluation (32-80 games); 10-20 h 40-opening comparisons + budget sensitivity; 20-30 h high-node teacher analysis, at most 1-2 fixes verified at 50k; 30-36 h best candidate's trial-0; 36-41 h final packaging.

Decision (Mochi): adopt GPT's framing. The user's brute-force capacity goes to evaluation volume at real conditions + high-node analysis, not high-node tuning. Arrangements launched after the decision: teacher2+TT2 integration lane (PC executor #1, job t2tt-1122).
