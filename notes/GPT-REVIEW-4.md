# GPT-REVIEW-4 — turn 6 reply: proposal withdrawn, final plan (2026-11-22 07:43 JST)

## Turn 6 verdict (received 07:43 JST, ~2m44s thinking)
GPT WITHDREW its turn-5 proposal. SPD-QS is unnecessary — SPD already has the
stand-pat fix; building it would just re-verify the same code.

New ranking:
1. (b) Submit SPD once as integration test (1 slot) — verify unverified server-side gates.
2. (c) Freeze at 1099 as provisional final candidate (below the 1154 floor, stated plainly).
3. (a) Further strength work — NOT recommended. No revert-test.

- Revert-test declined: known major search bug deliberately revived; 6 games cannot
  separate one lucky draw from real difference; tune-a vs SPD differ in more than qs,
  so the 2.0/6 tie proves nothing about causality. (Also corrected: practice trial-0
  does not consume submission quota — already in OPS-PLAN-2 — so slot saving was never
  the reason; it is time + information value.)
- Remaining 8 items, all declined: TT depth/bound (biggest theoretical upside, but
  needs a coherent design: EXACT/LOWER/UPPER, depth comparison, TT-key completeness,
  cross-game residue, mate-score handling); stalemate (easy fix, unlikely to show in
  6 games); castling rights; PST symmetry; phase cap; rook open-file; PV ordering;
  repetition.
- After the SPD submission, verify: receipt, thinking_priced, thinking_wellformed,
  entry_size, other server checks, final submission status. Do NOT confuse a local
  FAIL with a server FAIL.

## Final decision (GPT turn 6)
- No more strength lanes.
- 1. Submit SPD once (2,650 B official compress). 2. Freeze SPD (1099 Elo, below 1154).
  3. No new fixes (TT, stalemate, eval, move ordering included). 4. Code freeze
  2026-11-24 14:00 JST — only final-package consistency checks after that.
- Rationale: internally strong candidates repeatedly regressed in trial-0; stacking
  more weakly-evidenced improvements is not rational. Verify the submission path,
  then end at 1099 if clean.

## Status (main side, 07:43 JST)
- Release lane running: VM opencode session ses_dffbaaf1fffep3axiCC0F4MaTw (repo cwd),
  keeper attached (lane-keeper-release.sh). Prep only: init -> source write -> official
  compress -> commit -> bundle -> local check -> REPORT-RELEASE-SPD.txt, then STOP.
  NO submit yet — submit happens on main-side go-ahead after the local check is in.
  (Duplicate-driver fix: the keeper relaunched with --session because the first launch
  lacked --session in its cmdline; the original driver PID 3740 was killed, the
  keeper-visible driver PID 4319 remains.)
