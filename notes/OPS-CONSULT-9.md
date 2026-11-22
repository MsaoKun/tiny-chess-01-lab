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

Reply: pending (to be appended when received).
