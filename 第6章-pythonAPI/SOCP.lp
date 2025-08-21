\ Model SOCP
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  x + y
Subject To
 c0: x + y + z <= 2
 c1: [ x ^2 + y ^2 - z ^2 ] <= 0
Bounds
End
