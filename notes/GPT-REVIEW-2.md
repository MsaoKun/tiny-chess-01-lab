# Ops consultation turn 2 — outcomes (2026-11-21 22:02 JST)

Second round with ChatGPT on the same thread, after reporting what we had
implemented. Verified against primary sources where it mattered.

## VERIFIED FROM PRIMARY SOURCE (kit RULES.txt) — packaging is blocking
- RULES.txt, check `thinking_reproduces`: transcripts must account for >= 30%
  of counted lines, and main.py must have >= 1 authored line. A packed
  entrypoint counts as its source ONLY when the kit's own `makefun compress`
  produced it byte-for-byte AND the sessions show the agent writing the
  source and then running makefun compress on it afterwards.
- Our tune-a main.py (3,250 B) is a CUSTOM wrapper:
  `import base64,zlib` + `exec(zlib.decompress(base64.b64decode(...)))`.
  It was NOT produced by the official compressor, so its lines likely do
  not count as authored -> thinking_reproduces failure risk at submission.
- Consequence: EVERY candidate's final main.py must be produced by running
  the official compressor on the readable source, inside a recorded agent
  session (write source -> run compress). The custom zlib packing step in
  our current pipeline must be replaced by `node cli/makefun.mjs compress`.
- A full dry run (compress -> bundle --dry-run -> bundle -> check) with
  tune-a is now a BLOCKING task for tonight, ahead of further tuning.
- Related gates confirmed in RULES.txt: thinking_revised (>= 2 write/edit
  messages give a file its final content), thinking_turns (>= 5 assistant
  turns with text/thinking), transcripts_run_record (required since
  2026-11-17), thinking_own_work (since 2026-11-20).

## Adopted from turn 2
1. Trial queue with supersession: a candidate superseded before its trial
   starts is dropped (unless needed for A/B); parameter-only tweaks need a
   positive quick strength screen first; identical candidate hash is never
   re-trialed without a reason. Target: one completed trial-0 per 60-120
   min during active development; 3 hours without a trial result while
   candidates wait = feedback-system failure.
2. Sequencing: trial B (T7 fixed, safe cap) and C (R_mob on tune-a)
   SEPARATELY first. Integration D (T7 + R_mob) only after both results.
   (This replaces the earlier "integrate as soon as T7 validates" rule.)
3. Rehearsal relabeled: local worst move <= 7s = SMOKE PASS only, not
   trial-safe. taskset+ulimit does not reproduce the official sandbox.
   Trial-0 remains the runtime authority. Matched-position calibration
   (same positions replayed locally, ratio of judge/local times) to be
   collected from future trial-0 runs before trusting any local threshold.
4. Speed optimization: deferred and contingent. Only if the cap-cut T7
   trials weaker than tune-a; then time-boxed 3-4 h, profile first, keep
   only changes with >= ~20% CPython throughput gain and no correctness
   regression. Cap cut 50k -> 22k estimated at 0.6-1.2 ply lost.
5. Keeper run-ID fix: accepted in principle (completion must match run ID
   + candidate hash, never a bare report file), budgeted 1-2 h, AFTER the
   packaging dry run. No new supervisor platform.
6. GPT accepted our correction: trial-0 does not consume submission quota.

## Priority order now
Packaging validity (dry run tonight) -> T7 runtime at safe cap -> B and C
separate trials -> integration D if justified -> strength optimization.
