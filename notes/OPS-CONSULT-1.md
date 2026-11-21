# Ops consultation — process and infrastructure (2026-11-21)

We are asking for a review of HOW we are running this project, not of the engine code.
Facts below are measured, not estimates.

## Competition frame
- Strongest chess engine in <= 4,096 bytes of Python (stdlib only). Engine must be
  deterministic: fixed node/depth budget, no wall clock, no unseeded randomness.
- Official harness: 10 s per move. Practice trial ("trial-0") = 6 games vs fixed
  anchors (Elo: depth-2 855, depth-3 1073, depth-4 1199, 100k nodes 1392,
  250k nodes 1497, 500k nodes 1596).
- Score floor that matters: 1154. House baseline (Sunfish 4K @ 50k nodes) ~ 1365.
- Entries close 2026-11-25 02:00 JST — about 76 hours from this writing.
- Best verified score so far: base engine "tune-a", trial-0 Elo 1099 (below floor).

## How the work is organized
- Three parallel worker lanes, all AI coding agents (DeepSeek) supervised by an
  orchestrator agent:
  - T5: evaluation improvements on tune-a (mobility / PST variants, head-to-heads).
  - T6: self-play parameter tuning (screening 32 games, promotion needs a
    100-game confirmation at 50k nodes scoring >= 52%).
  - T7: bug-fix lane applying a reviewed fix list (quiescence stand-pat, TT depth
    and bound handling, stalemate scoring, castling rights from FEN, PST symmetry,
    phase clamp, rook open-file condition, move-ordering bonus).
- Orchestrator rule we imposed: the official trial runs ONLY on "finished"
  candidates. Lanes report internal metrics (ladder win rates, per-move CPU-cost
  timings, perft).

## The failure that exposed the process
- T7's fixed candidate passed every internal gate (byte size, perft all 6,
  regression tests) and beat the previously accepted version 52.5% over a
  60-game ladder — then scored 0 in trial-0: all 6 games lost on time, worst
  move ~14.9 s against the 10 s limit.
- The ladder ran with a CPU-cost budget on a fast desktop (PyPy, 6 cores). No
  gate measured per-move WALL-CLOCK under the actual trial conditions.
- Since that 0, no new official score has been produced at all (hours of lane
  work, internal metrics only). Feedback starvation by our own gating rule.

## Infrastructure reality
- Lanes run on a VM that restarts roughly every 2 hours, killing all lane
  processes. Sessions are resumable; watchdog "keeper" scripts relaunch a dead
  session within ~1 minute when they work.
- One lane's keeper had a wrong completion condition (it treated an old phase's
  report file as "done"), so that lane ran UNGUARDED through its current phase.
  It died at least 4 times tonight; two deaths were only noticed at the
  30-minute human check cadence, costing ~30 minutes each. Lane processes also
  die without VM restarts; logs simply stop, cause unknown.
- Match throughput: a 60-game ladder at 50k nodes ~ 45 min on the desktop
  (PyPy). On the VM, python3 fallback is ~5x slower than PyPy; a 100-game
  confirmation is running at ~7 games / 31 min (ETA ~4 more hours).
- The orchestrator's own context is also finite; supervision is periodic
  (30-minute checks), not continuous.

## Questions
1. Trial cadence and gating: how do we avoid feedback starvation? Should the
   official trial (or a faithful local replica) run on intermediate candidates?
   What should the gate order be (cheap -> expensive), and what belongs in a
   fast "trial rehearsal" that catches timeout-class failures in minutes?
2. Predictive metrics: which measurements actually predict trial success
   (per-move wall-clock distribution on worst-case positions? node counts?
   ladder conditions?) and how should the internal ladder be run so its
   results transfer to the harness?
3. Running lanes on an unreliable host: work-unit sizing, checkpointing,
   watchdog patterns. How do we make a lane death cost minutes, not 30?
   Is 3 parallel lanes right, or fewer lanes with tighter loops?
4. Time allocation for the remaining ~76 hours: speed fix vs strength tuning
   vs freeze/submission prep. When do we stop tuning and lock the best
   verified candidate? Fallback if nothing clears 1154: submit tune-a (1099)
   anyway, or keep pushing? Expected-value reasoning welcome.
5. Blind spots: anything structurally wrong with this setup that we cannot
   see from inside?

We want a concrete revised operating plan, with numbers where possible.
