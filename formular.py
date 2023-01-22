#!/usr/bin/env python3

from z3 import *
import itertools

s = Solver()
a, b, c, d, e = vars = Ints("a b c d e")
for x in vars:
    s.add(Or(x == 2, x == 9, x == 5, x == 7, x == 3))
for x, y in itertools.combinations(vars, 2):
    s.add(x != y)
s.add(a + b * c * c + d * d * d - e == 399)
s.check()
print(s.model())
