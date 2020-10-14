"""
ID: giliev91
LANG: PYTHON3
TASK: kimbits
"""
from math import factorial


def input():
    with open("kimbits.in", "r") as f:
        N, L, I = tuple(map(int, f.readline().strip().split()))
        return N, L, I


def solve(N, L, I):
    x = [0] * N
    ones = 0
    total = 0

    for i in range(N):
        c = count(N-i-1, L-ones)

        # if we can include all of them in the total we put a 1
        if total + c < I:
            x[i] = 1
            total += c
            ones += 1

    return "".join(map(str, x))


# return count of numbers with n digits and at most l ones
def count(n, l):
    c = 0
    for i in range(l+1):
        if i <= n:
            c += comb(n, i)

    return c


# combinations (n, r)
def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)


def output(res):
    with open("kimbits.out", "w") as f:
        f.write("%s\n" % res)


output(solve(*input()))
