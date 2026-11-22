# OPS-CONSULT-17 — GPT turn 17 (2026-11-23 02:22-02:27 JST)

Topic: BERLIN trial 4.0/6 = 1451; philidor-pack dead; what next. Consulted premise-free.

GPT verdict:
- **Submit BERLIN NOW**, then re-pin after verifying acceptance + 1451 server-side. Order: final checks -> bundle -> submit -> verify prize_eligible + 1451 + finished -> `makefun final` to the new id -> GET-verify the pick (the page still says "latest submission is final" in places, so verify explicitly). 3rd submission of 10.
- BERLIN is the baseline from here: do not overwrite its search/book order/eval constants with untested changes.
- Philidor: diagnosis only, 2-3h cap. First establish whether Qf7 actually scores vs 500k from the teacher2 side (the earlier rescue test never showed a score from Qf7 vs the anchor — it only showed a win from the SPD side's failure to reach it... correction: the philidor lane verified Qf7 wins 132 plies vs 500k with teacher2 playing on; GPT's point is to confirm that value, then find an SPD-side path). Stop if: Qf7 scores nothing on replay, reaching the rescue needs a long forced line, no from-opening improvement in 2-3h, or BERLIN's 4 wins break. teacher2-based candidate only as an independent candidate, never mixed into BERLIN untested.
- Slav: stop dedicated analysis (12 failures is weak evidence for more effort); revisit only if a general improvement incidentally helps it.
- General comparison: do NOT repeat the full 80-game set (BERLIN differs from BOOK by one book branch; non-firing games are identical). Instead: book fire count across the 40 openings, full move-diff BERLIN vs BOOK, 150-200 ply long-game timing safety (BOOK had one ~14 s move in the 80-game set; trial worst was 2.2 s but unknown openings are untested), representative comparisons vs teacher2/TT2.
- Schedule to the freeze (11/24 14:00): 0-2h submit+pin; 2-5h philidor diagnosis; 5-14h general comparison + long-game tests; 14-24h integrate at most ONE promising change + trial; 24-31h verify + submit best; 31-36h freeze prep. Max 2 new candidates (A: BERLIN+philidor rescue only if a real route is found; B: BERLIN+general search improvement only with new evidence). A new candidate below 4.0/6 does not displace the pin even with general gains; holding 4.0/6 + fewer timeouts on unknown openings qualifies.
- Key framing: qualifying is already secured (1451 vs floor 1154). The prize lever is now reducing loss/timeout rates on unknown openings, because the finals redraw openings and the book may not fire. Do not start a new large search algorithm now (node increase, LMR, coarse Texel all showed no sufficient gain).

Actions: submit decision presented to the user with an options widget (release session + bundle + check run after approval).
