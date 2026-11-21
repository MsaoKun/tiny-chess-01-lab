# Ops plan v2 — adopted 2026-11-21 21:50 JST

External ops review (ChatGPT, thread "チェスエンジン改良優先順位") of
OPS-CONSULT-1.md, cross-checked against our records. Adopted items are marked
ADOPTED; corrections to the review are marked CORRECTED.

## Cross-check
- Elo scale confirmed against our known point: 2.0/6 = 1099 (tune-a).
  2.5/6 = 1191 clears the 1154 floor — the gap is one draw, not 55 abstract
  points. 3.5/6 ~ 1364 ~ house benchmark.
- CORRECTED: the review treats "official trials" as quota-limited. Our
  practice trial-0 does NOT consume submission quota (we have run it many
  times). The scarce resource is submissions: 0 of 10 used, 5/day cap.
  So trial-0 may run on every rehearsal-passing candidate; submissions are
  reserved for the endgame.
- Statistics critique accepted: 52% over 100 games is +/-5pt standard error —
  weak evidence. The 100-game confirmation model is retired.

## Adopted operating rules
1. Success = verified trial-valid score movement, not lane deliverables.
   No promotion on ladder score alone.
2. Gate order: static (bytes, perft) -> REHEARSAL (CPython, taskset 1 CPU,
   ulimit 512MB, 16-24 fixed FENs, real UCI flow, wall-clock per move;
   FAIL if worst move > 7s, hard fail > 10s; record mean) -> trial-0.
3. The "trial only on finished candidates" rule is abolished.
4. Watch the cumulative budget too: trial total 1,800s including the house
   engine's thinking; target mean move time ~<=1.5s on the benchmark mix.
5. Lanes reduced from 3 to 2: T6 (self-play parameter search) is PARKED —
   its 100-game confirmation at ~7 games/31min would take ~7.4h for a
   +/-5pt measurement, and its CPU contention contaminates wall-clock
   measurements. T6 state is preserved in a parking report for later resume.
   T7 = runtime/correctness/packaging; T5 = eval (R_mob won its head-to-heads).
6. Candidate registry (work/registry.md) maintained by the check chain:
   candidate, source lane, rehearsal worst/mean, trial-0 score, state.
7. Freeze: 2026-11-24 14:00 JST code freeze, final submission by ~22:00.
   Once a submission clears 1154, never replace it with an unqualified
   candidate (the last submission is the entry).
8. Fallback: if nothing clears 1154, tune-a (1099) remains the entry —
   a timing-out candidate has zero qualification chance regardless of
   ladder strength.

## Immediate actions taken (2026-11-21 21:53-21:58)
- T7 steered: build the rehearsal gate, sweep E candidate at node caps
  20000/22000/25000, produce the fixed main.py at the largest passing cap.
- T6 steered to park: stop conf-g04 and screening, write parking report.
- Check chain (next-27, fires 22:00) rewritten to this plan.
