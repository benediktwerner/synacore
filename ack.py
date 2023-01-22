#!/usr/bin/env python3

MOD = 32768
MOD1 = MOD - 1


def f(a, b, h):
    if a == 0:
        return b + 1
    if b == 0:
        return f(a - 1, h, h)
    return f(a - 1, f(a, b - 1, h), h)


def f2(a, b, h):
    # f(0, i) = i + 1
    if a == 0:
        return b + 1

    # f(1, 0) = f(0, h) = h + 1
    # f(1, 1) = f(0, f(1, 0)) = f(0, h + 1) = h + 2
    # f(1, 2) = f(0, f(1, 1)) = f(0, h + 2) = h + 3
    # f(1, i) = h + i + 1
    if a == 1:
        return h + b + 1

    # f(2, 0) = f(1, h) = h + h + 1 = 2h + 1
    # f(2, 1) = f(1, f(2, 0)) = f(1, 2h + 1) = h + h + h + 2 = 3h + 2
    # f(2, 2) = f(1, f(2, 1)) = f(1, 3 + 2) = 4h + 3
    # f(2, i) = (i + 2) * h + i + 1
    # proof: f(2, i) = f(1, f(2, i - 1)) = f(1, (i + 1) * h + i) = h + (i + 1) * h + i + 1 = (i + 2) * h + i + 1
    if a == 2:
        return (b + 2) * h + b + 1

    # f(3, 0) = f(2, h) = (h + 2) * h + h + 1 = h² + 3h + 1
    # f(3, 1) = f(2, f(3, 0)) = f(2, h² + 3h + 1) = (h² + 3h + 3) * h + h² + 3h + 2 = h³ + 4h² + 6h + 2
    # f(3, 2) = f(2, f(3, 1)) = f(2, h³ + 4h² + 6h + 2) = (h³ + 4h² + 6h + 4) * h + h³ + 4h² + 6h + 3 = h⁴ + 5h³ + 10h² + 10h + 3

    # f(4, 0) = f(3, h)
    # f(4, 1) = f(3, f(4, 0)) = f(3, f(3, h))
    return None


def f3(b, h):
    curr = h
    for _ in range(b + 1):
        curr = ((((curr + 2) * h) & MOD1) + curr + 1) & MOD1
    return curr


for h in range(1, MOD):
    if f3(f3(h, h), h) == 6:
        print(h)
