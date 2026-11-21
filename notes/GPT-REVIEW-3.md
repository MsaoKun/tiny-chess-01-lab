# GPT-REVIEW-3 — turn 5 reply + qs correction (2026-11-22 07:30 JST)

## GPT turn-5 verdict (received 07:30 JST, ~3.5 min thinking)
Ranked: (a) one last fix — qsearch stand-pat only, CP=50000, SPD base, max 6 h;
(b) submit SPD once as an integration test (worth 1 of 10 slots); (c) stop at 1099
— premature now, switch if the single fix fails. Plan: (a) + (b) in parallel,
then no more strength experiments. SPD-QS adoption: trial-0 >= 2.5/6 adopt;
2.0/6 reject (stop experiments); <= 1.5/6 discard; timeout/determinism/packaging
failure = reject regardless of score. No 100-game self-play check.
Full reply recorded by the main side (browser-task 950f9c41).

## CORRECTION (main-side verification, 07:31 JST) — the fix is already in SPD
GPT's turn-5 (a) was based on re-reading tune-a's ORIGINAL qs(). But the SPD
base (work/speed/inner_final.py, the Hy4 speed lane's rewrite) already
implements stand-pat correctly:

tune-a original (repo/source.py, buggy):
```
 k=A.index(6*s);c=at(k,-s)
 if not c:
  v=ev(s)
  if v>=b:return b
  if v>a:a=v
 ms=gen(s,not c);z=-X
 ...
 return-Y if z<-X and c else z     # z<-X is never true: mate return is dead code
```

SPD base (work/speed/inner_final.py, correct):
```
 k=A.index(6*s);c=at(k,-s);z=-X;l=0
 if not c:
  z=ev(s)
  if z>=b:return b
  if z>a:a=z
 for m in od(gen(s,not c),0):
  ...
  l=1
  v=-qs(-s,-b,-a);um(u)
  if v>z: z=v ...
 return-Y if c and not l else z    # checkmate returns -Y; stand-pat is the floor
```

So (a) as specified is a no-op on SPD. Further, SPD (qs fixed) still ties
tune-a at 1099 in trial-0 at CP=50000 — the fix as implemented produced no
trial-0 Elo gain. Turn 6 asks GPT to re-rank with this correction (revert-test
to isolate the fix? another single fix? or (b) then (c)?).
