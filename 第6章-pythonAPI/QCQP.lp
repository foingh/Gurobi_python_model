\ Model QCQP
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - 2 x - 6 y + [ x ^2 - 2 x * y + 2 y ^2 ] / 2 
Subject To
 c0: - x + 2 y <= 2
 c1: 2 x + y <= 3
 c2: 0.5 y + [ x ^2 ] <= 2
Bounds
End
