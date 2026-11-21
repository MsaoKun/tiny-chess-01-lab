# GPT review round 1 — 2026-11-21

ChatGPT read notes/STATUS.md and engines/tune-a_inner.py and returned a
general consultation plus a code-level review. The main agent then verified
every code claim against the source before acting. Summary of the outcome:

## Verified TRUE in the code (main checked line by line)

1. qs() drops the stand-pat score: quiet leaves return -40000 instead of the
   static eval; checkmate inside qs also returns -40000, never -29000,
   because the `z<-X` test can never fire. (Worst defect.)
2. TT reuses scores with no stored depth and no bound type; the table is
   also never cleared between games.
3. Stalemate is scored as checkmate (`if not ms:return-Y+q` with no check
   test).
4. Castling rights from the FEN are never read; castling is generated from
   piece placement only.
5. PST file bonus (3-abs(i%8-3)) is asymmetric: [0,1,2,3,2,1,0,-1].
6. Phase can exceed 24 after promotions, giving the endgame term a
   negative weight.
7. Rook open-file bonus ignores own blocking pawns.
8. PV move ordering bonus (999) is smaller than a pawn capture (1000).
9. Repetition handling is approximate: the history is a set (first
   repetition already scores as a draw inside search) and search-path
   positions are not tracked.

## Advice adopted

- Fix search correctness BEFORE more eval work: new lane tune-g applies the
  fixes one at a time (qs -> TT-off A/B -> stalemate+castling -> PST/rook/
  phase -> ordering), each validated by a >=100-game equal-node match and
  regression FEN tests.
- Self-play tuning (tune-f) promotion rule tightened: 30-40 games is
  screening only; champion status needs a >=100-game confirmation at the
  final 50k node cap. (At 30 games / 57%, a truly-equal candidate promotes
  ~18% of the time by chance.)
- "All losses by checkmate" is NOT by itself evidence that the eval is the
  bottleneck — the search defects are a better explanation for the plateau.

## Not yet proven

All Elo impact is unproven until the A/B matches run. The review was static
analysis; the fixes may gain a lot or a little. Measurements will be added
here after tune-g reports.
