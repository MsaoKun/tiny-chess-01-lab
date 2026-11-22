# OPS-CONSULT-16 — GPT turn 16 (2026-11-23 00:47-00:51 JST)

Topic: which lanes to build now, after the rescue test (G4 rescuable from 2 plies earlier only; G5/G6 not rescuable from any tested point). Consulted premise-free.

GPT verdict:
- Priorities changed. Top: Berlin's "king to f8 two plies early" as a BOOK candidate (Lane A), NOT an eval change — the evidence shows one specific move wins, not that king safety in general is lacking. Target 3.0/6 -> 4.0/6. Launch to trial-0 without waiting for B/C.
- Slav (Lane B) and Philidor (Lane C): no basis yet for an eval fix. Investigate further back first: Slav to -16 plies (test -4/-6/-8/-12/-16, teacher's top ~3, prefer course-changing moves; look for the structural cause, not the attack itself); Philidor: first find the exact ply the dangerous passer was created, then analyse 4-8 plies before that. Stop conditions: no improvement by -16, one-game-only fix with regressions elsewhere, time cap. Candidate-ize only if a rescue is verified.
- Book implementation notes (Lane A): save the rescue FEN + UCI + history; verify the candidate REACHES the rescue FEN from the game start (a mid-game rescue does not guarantee that); key on side/castling/en-passant (+ halfmove/history where needed); fall through to search on mismatch; replay from the opening to reproduce the win vs 100k.
- Gates differ by lane type: A = rescue confirmed + from-opening reproduction + perft/determinism + 4KB + worst 3.5s + light screen regression only; B/C (if they change eval) = full screen + unknown-opening comparison. Trial-0 remains the authority for promotion.
- Schedule to the freeze (11/24 14:00): 0-3h A; 3-10h B (+ Philidor analysis in parallel); 10-17h C; 17-25h trial/integrate only proven changes; 25-32h 40-opening comparison + long-game safety; 32-37h packaging/freeze prep. Cut order: Philidor eval change, then Slav if no branch by -16, Berlin last (it has a verified flip). If Berlin's from-opening reproduction fails, shift the target point earlier, max ~2h extra, then protect BOOK.
- Keep BOOK pinned; overwrite only after a new candidate is accepted and its improvement is measured.

Actions: Lane A (berlin-1123) on PC executor #1, Lane B (slav-1123) on executor #2, Lane C (philidor-1123) queued behind A on executor #1.
