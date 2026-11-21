# tiny-chess-01 lab

Working records and engine sources for the make.fun **tiny-chess-01** bounty:
the strongest chess engine that fits in 4 KB of Python.

This repository exists so an external advisor (ChatGPT) can read the actual
code and records while we iterate. Implementation itself happens in our own
recorded agent sessions; advice from here is cross-checked against measured
results before anything is adopted.

## Rules of the bounty (summary)

- `main.py` single file, <= 4096 bytes, Python 3.13 standard library only
- Deterministic: fixed node budget, no wall clock, no unseeded randomness
- 10 s per move, 1800 s per trial
- Practice trial: 6 games against fixed anchor engines (win = 1, draw = 0.5)
- Entry floor: practice Elo **1154**; prizes require beating the house
  baseline (Sunfish 4K @ 50k nodes, ~**1365** practice Elo)
- Entries close 2026-11-24 17:00 UTC

## Where we are

- Best engine so far: **tune-a**, practice Elo **1099** (floor is 1154)
- Speed-focused tunes plateaued at 876 despite 1.8-6.6x NPS gains; the
  losses are all by checkmate, so evaluation quality is the suspected
  bottleneck
- Full status, measurements and open questions: `notes/STATUS.md`

## Layout

- `engines/` — candidate engines. `*_main.py` / `candidate-c.py` are the
  packed single-file entries (zlib+base85 self-extracting); `*_inner.py`
  are the decoded inner sources, which are the readable code.
  Start with `engines/tune-a_inner.py` (the best engine, 5139 bytes
  decoded).
- `notes/` — status, tuning briefs for the lanes currently running, and
  the tune-b report.
