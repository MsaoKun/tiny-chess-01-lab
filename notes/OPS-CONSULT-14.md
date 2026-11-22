# OPS-CONSULT-14 — GPT turn 14 (2026-11-22 23:16-23:20 JST)

Topic: tiny-stack-vm-01 submission decision after the fix lane (check 15/15 PASS, size 6,943 -> 5,570 B, grade-local 1,000,000).

GPT verdict:
- **Submit the current 5,570 B version NOW.** Do not gate the first submission on further size reduction; the remaining uncertainty is server-side acceptance, which only a real submission resolves.
- **KEY DIFFERENCE from chess: stack-vm has NO pin — the latest submission before the deadline is the final entry.** After submitting, never overwrite with an unverified version. Any resubmission must be smaller AND fully re-verified (40/40, hard-14, determinism, grade-local, full check).
- Further reduction is worth it (multiple perfect-score entries exist; 5,570 B may not be top-10 on size): targets 5,400 -> 5,200 -> 5,000-5,300 B in a separate worktree, AFTER the first submission, low priority vs chess until the chess freeze.
- Risks: finals problems differ (mitigated: reference-VM diffing + 152/152 fuzz), 60 s total in the 1-CPU/512 MB isolated env (practice 40 in ~5 s on the PC; Docker grade unavailable on the PC — accepted caveat), server gates, overwrite.
- After submitting: verify server-side score + authorship + size + acceptance, and record commit SHA / submission id / received time.

Decision flow: GPT consulted (this turn) -> user decides the submission via options widget.
