# OPS-CONSULT-9 — after the turn-8 lanes (2026-11-22)

Posted to the ChatGPT thread "チェスエンジン改良優先順位" as turn 9 on
2026-11-22 ~17:15 JST.

## Results since turn 8
- BOOK: trial-0 3.0/6 = 1279, the only qualifier. Book move d1h5 fired
  at ply 35 of game 3 vs depth-4 and flipped it. The edge is that one move.
- TEX-A: rejected. Texel loss improved on 2,880 positions from 240
  self-play games (cap 10k/13k/16k), but match screens vs base were
  36.0% (train openings) / 25.5% (holdout) — learning did not transfer
  to playing strength.
- PVS alone: screen 15.0/32 = 0.469, rejected.
- LMR alone (conservative): screen 16.5/32 = 0.516 (weak positive),
  trial-0 1.0/6 = 876, rejected. Real depth gains (one extra ply at
  the same node count on some FENs) did not convert to score.
- FIX: screen 14.0/32, trial-0 1.0/6 = 876, rejected.

## House analysis (REPORT-HOUSE.txt, PC lane, complete)
- calibration.json has NO move lists: result + opening id + terminal
  reason + ply count + a hash of the move list. Not usable as training
  data.
- House eval is minimal: piece values + formula PSTs + bishop pair +30,
  king tapered only. Absent: king safety, passed pawns, pawn structure,
  mobility, rook open files, tempo, SEE, check extensions.
- depth-3 vs depth-4 divergence over the 40 openings: 15/40 change move,
  but verified gains are <=12 cp in 13 cases. Two big ones: Italian
  Game +52 cp (our book move) and Ruy Lopez Berlin +32 cp.
- Report's ranked improvements: #1 > #3 > #2 > #5 > #4 > #6 > #7.
  #6 = contempt + endgame/adjudication plan; #7 = null-move/LMR depth
  parity.

## State at posting
- Best: BOOK 1279. Submitted: SPD 1099 (1/10). Decision pending:
  submit BOOK now or wait for a general-strength candidate. Finals
  openings are redrawn, so the book may not fire (then the entry plays
  like SPD, 1099). 9 submission slots remain.
- Freeze 11/24 14:00 JST, deadline 11/25 02:00 JST. ~45 h left.
- trial-0 is VM-only; analysis/learning/screens run on the PC.

## Questions asked
1. Next-lane priorities (report's ranked items, null-move, capped-TT
   retry, adaptive node budgets, teacher-based error mining, contempt).
2. Was the Texel failure a design problem (game count, caps, features,
   split) or is weight learning hopeless at this scale? Is TEX-B/C
   worth it?
3. BOOK submission timing: now or wait for a general candidate?
4. Realistic endgame for the remaining ~45 h, finals strength included.

## Reply received (2026-11-22 17:21 JST)
Four decisions:
1. **Submit BOOK now** — do not wait for a general-strength candidate.
   Pin the finished BOOK submission as the final entry with
   `makefun final tiny-chess-01 <submission_id>` (verified in kit CLI
   v0.1.0: rule Force_Last; a pinned final survives later entries).
   Change the pin only when a general candidate is proven better.
2. **Lane A (priority 1): teacher-based error mining** (6–8 h) — 40
   openings, both colours, 100–200 positions, teacher = house
   nodes-500k (1M+ for key positions); deliver 20–30 classified
   blunders; fix at most 2 if one cause dominates.
3. **Lane B (priority 2): capped TT retry** (4–6 h) — 4,096/8,192
   slots, depth-preferred replacement, repetition on the search path,
   150–200 ply stress test (RSS + worst-move time at plies
   10/50/100/150).
4. **TEX-B/C: do NOT run as designed.** Only a 1–2 h cause audit:
   check the learner's features reproduce the engine's eval exactly
   on 100 positions (sign, PST mirroring, phase, units, endgame);
   if consistent, a small 3–5 parameter retrain with limited range;
   otherwise end the Texel line. (GPT's #1 suspect: the 10k/13k/16k
   training distribution vs 50k play.)
- Finals math: ~4.0/8 needed for the ~1365 prize line; realistic
  mid-goals: beat depth-4 reliably, draw+ vs nodes-100k.
- Trial-queue handling after BOOK is pinned: 3.5/6+ protect, 3.0/6 tie
  (compare on unknown openings/safety), 2.5/6 keep if generally
  stronger, <=2.0/6 keep BOOK.
- Note: GPT could not see REPORT-HOUSE.txt's numbered definitions
  (public notes only carry the ranking); it ranked independently.
  The definitions live in REPORT-HOUSE.txt §5 on disk.

## Adoption (Mochi, 2026-11-22 17:21)
- BOOK submission: awaiting the user's tap (options widget sent
  17:21). Submission will follow BRIEF2.md step 5 + the extra
  redaction, then `makefun final` pinning.
- Lane A (teacher mining) and Lane B (capped TT) launched on the PC
  in parallel (executor #1 job teacher-1122, executor #2 job
  tt2-1122). Briefs: BRIEF-TEACHER.md / BRIEF-TT2.md.
- Texel cause audit: not launched yet (decide after lanes A/B land;
  1–2 h, PC).
