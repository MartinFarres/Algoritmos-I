from numpy import rec


def r(a):
    n = 0
    return rec(a, n)


def rec(a, n):
    if n == 0:
        return rec
