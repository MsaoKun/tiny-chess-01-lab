# OPS-CONSULT-18 (2026-11-23, GPT turn 18)

State given: BERLIN submitted + pinned (1451). Remaining losses: G5 Slav (White, vs 250k), G6 Philidor (Black, vs 500k). Slav: 12 rescue alternatives all lost; remaining idea = avoid the line by book. Philidor: Qf7 rescue verified with teacher2 (null-move) but the SPD-based book candidate diverged at ply 12 and never reached it. Freeze 11/24 14:00 JST, ~35 h left. Competitor asked for a multi-angle plan.

## GPT ranking (subjective planning estimates; success = keep the 4 wins + gain points in trial-0)
1. Philidor: null-move base + rescue book — 30-50%, +1.0, cap 6 h.
2. Slav: choose a different line early — 20-40%, +0.5-1.0, cap 8 h.
3. Philidor: small guide book from ply 12 — 15-30%, +1.0, cap 4 h (alternative to 1; do not add the scores).
4. General eval (king safety / passed pawns) — 10-20%.
5. Draw-seeking redesign — 5-10%.
6. New search / higher node cap — 5-10%.

## Lane A (Philidor): switch the engine base, not the book line
- Fix teacher2's full winning Philidor game record first; reproduce it under identical conditions.
- Do not force teacher2's line into the SPD engine. Instead: common search code with null-move toggled by position (Philidor-type start -> teacher2 conditions; everything else -> BERLIN behaviour). Deterministic from the provided start FEN / game moves only; no opponent id or game number.
- Replay game 6 from the opening: does it reach the ply-35 position? If yes, Qf7 fires by exact position.
- Verify games 1-4 stay wins (books fire), then trial-0. 5.0/6 -> protect as new main candidate.
- Cut: if the from-opening win is not reproduced within 6 h including the toggle implementation, stop and shift time to Slav.

## Lane B (Slav): avoid, don't rescue
- Get the practice Slav start FEN and BERLIN's first self-chosen moves. At the first branch points, take the teacher's top 3-5 alternatives, play each out to the end vs nodes-250k with BERLIN playing on.
- First target is a draw (4.5/6), then a win. Book-ify only branches that reach draw-or-better, minimally.
- Cut: 8 h without one from-opening draw-or-better -> close the lane. If a found branch breaks the existing 4 wins when book-ified, do not adopt it.

## Lane C (parallel verification): 40 openings x both colours book fire rate; move diff vs BERLIN; null-move-on win rate outside the target opening; 150-200 ply long games and worst think time; memory / 4 KB / determinism / perft; the 4 wins reproduce.

## Schedule (35 h): 0-4 h reproduce + implement / Slav candidate generation; 4-8 h from-opening verification; 8-13 h trial for whichever succeeded; 13-20 h guide book only if needed; 20-27 h integrate proven changes only + integrated trial; 27-32 h 40-opening + long tests + formal submission; 32-35 h freeze.
## Promotion: trial 4.5/6+ = protect as improved candidate; 5.0/6+ = new main candidate, submit with priority. A 5.0/6 practice candidate with a big unknown-opening regression still gets compared against BERLIN before adoption.
## Cut order: long guide books that cannot reproduce points; new general eval/search changes; keep branches with measured point gains.
