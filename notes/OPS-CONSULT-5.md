# OPS-CONSULT-5 — endgame decision (2026-11-22 07:20 JST)

State: every lane is done. No successor candidate exists. Freeze 2026-11-24 14:00 JST,
deadline 2026-11-25 02:00 JST (~55 h left). Submissions 0/10.

## trial-0 results (all candidates, practice trial-0, 6 games)
| candidate | origin | score | Elo | note |
|---|---|---|---|---|
| tune-a | Hy4 base | 2.0/6 | 1099 | strongest, tied |
| SPD | speed lane, official compress | 2.0/6 | 1099 | tied, faster |
| cap65 | Lane A, CP=65000 | 2.0/6 | 1099 | tied |
| cap75 | Lane A, CP=75000 | — | — | VM rehearsal HARD FAIL (wall 10.26s, CPU 3.38s, contention); not trialed |
| cap100 | Lane A, CP=100000 | 0.0/6 | 0 | all 6 games lost on time |
| T7-B | search fixes, CP=20000 | 1.5/6 | 997 | below tune-a |
| T5-C | R_mob eval, cap 42000 | 0.5/6 | 708 | far below tune-a |
| cand_rmob | Lane B, R_mob + queen-mobility fix, CP=50000 | 1.0/6 | 876 | A/B vs SPD was +60.9% (19.5/32), direct queen-fix A/B 57.4% — but trial-0 is 223 Elo BELOW tune-a |

Pattern: every eval/search change tried so far made trial-0 worse or neutral.
Only speed and cap changes tied tune-a. The 8 verified tune-a defects from
GPT-REVIEW-1 (qs drops stand-pat; TT no depth/bound, never cleared; stalemate
scored as checkmate; castling rights never read from FEN; PST file bonus
asymmetric; phase can exceed 24; rook open-file ignores own pawns; PV ordering
bonus 999 < pawn-capture 1000) are mostly still unfixed in shipped candidates —
but T7's search fixes, which addressed some of them, went backwards in trial-0.

## Packaging state
- thinking_priced PASS. thinking_wellformed still FAILs locally (kit design false
  positive: one long tool execution makes seq timestamps step back 79 s; feedback
  sent to make.fun, no reply channel). entry_size resolves at commit time.
- Every final main.py must be official `makefun compress` output. SPD's official
  compress (2,650 B) is ready; tune-a's is ready too (2,460 B, dry-run artifact).

## Question (turn 5)
Rank these endgame options with reasoning, not a hedge:
(a) One more strength lane — which SINGLE change has the best expected value
    given that every eval/search change so far went backwards in trial-0?
(b) Submit SPD now as a submission-path integration test (1099, below the 1154
    floor, no finals value; tests the unverified server-side gates, incl. the
    wellformed check). Worth one of the 10 submissions?
(c) Stop spending: accept 1099 as the final candidate and only prepare the
    submission package (freeze-ready, no more lanes).
