#!/usr/bin/env python3

import operator

# *   8   -   1 < goal: 30
# 4   *   11  *
# +   4   -   18
# 22  -   9   *
# ^ start

OPS = {
    (1, 0): operator.sub,
    (3, 0): operator.mul,
    (0, 1): operator.add,
    (2, 1): operator.sub,
    (1, 2): operator.mul,
    (3, 2): operator.mul,
    (0, 3): operator.mul,
    (2, 3): operator.sub,
}

VALUE = {
    (0, 0): 22,
    (2, 0): 9,
    (1, 1): 4,
    (3, 1): 18,
    (0, 2): 4,
    (2, 2): 11,
    (1, 3): 8,
    (3, 3): 1,
}

pos = {(0, 0, 22)}
seen = set(pos)
fro = {}

while True:
    new = set()
    for x, y, value in pos:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                op = OPS[(nx, ny)]
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nnx, nny = nx + dx, ny + dy
                    if 0 <= nnx < 4 and 0 <= nny < 4 and (nnx, nny) != (0, 0):
                        v = op(value, VALUE[(nnx, nny)])
                        n = (nnx, nny, v)
                        if n == (3, 3, 30):
                            print(x, y, nx, ny)
                            while (x, y, value) in fro:
                                print(fro[x, y, value])
                                x, y, *_, value = fro[x, y, value]
                            exit()
                        elif nnx == 3 and nny == 3:
                            continue
                        if n not in seen:
                            new.add(n)
                            seen.add(n)
                            fro[n] = (x, y, nx, ny, value)
    pos = new
