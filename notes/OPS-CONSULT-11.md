# OPS-CONSULT-11 — GPT turn 11 (2026-11-22 20:11-20:15 JST)

Topic: tiny-stack-vm-01 submission timing (separate competition from chess).
Consulted premise-free before any user decision.

Facts given: entry complete, unsubmitted; practice 40/40, kit checker 40,000/40,000, local grade 1,000,000/1,000,000; repo 6,929B (cap 8,192); determinism 2 runs match; 14 hard edge cases pass; deadline 2026-11-25T04:00Z; escrowed $100, top-10 x $10; quota separate from chess; chess HYBRID + TT2 running in parallel, freeze 11/24 14:00.

GPT verdict: submit EARLY, after pre-submission gate checks. No reason to wait for chess.
- Ties are broken by smaller size_bytes, then earlier receipt. Other entrants already have 1,000,000 practice scores — a perfect score does not guarantee top 10. Secure a valid perfect submission first; safe size reduction is a separate later candidate.
- Pre-submit checks (in order of importance): (1) repo created AFTER competition start 2026-11-22 04:00 UTC; (2) transcript session times inside the competition window (thinking_in_window); (3) authorship gate — page says 80%, machine-readable min_authored is 0.3, aim for 80% and verify with the latest kit; (4) complete transcript set (parent + subagent sessions, system prompt, instruction files, user prompt, run record) via the official bundle. Commands: grade-local --driver docker, bundle --dry-run, bundle, check.
- Fuzzing (500-2,000 differential programs vs reference vm.mjs) is worthwhile but runs IN PARALLEL with submission; fix only if a bug is found. Finals: 40 questions in 60 seconds TOTAL, 1 CPU/512MB — verify Docker grading time.
- Size reduction is worthwhile (ties broken by size; size_bytes includes path lengths), but only safe reductions (comments/whitespace/dupes, unneeded files); never cut boundary conditions; no full rewrite. Keep practice 1,000,000 + hard 14 + determinism + gates as the promotion condition.
- Parallelism: stack-vm submit lane fully independent on the PC; do NOT run heavy fuzzing/Docker on the VM during chess trials (CPU contention affects time-loss verdicts).
- Quota for this competition: 10/day, 20 total, independent of chess.

Actions: submit-prep lane launched on PC executor #2 (job vm1-submit-1122) — gate checks only, NO submit. Submission itself goes to the user with a one-tap choice after the checks pass.
