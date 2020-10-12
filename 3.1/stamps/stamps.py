"""
ID: giliev91
LANG: PYTHON3
TASK: stamps
"""
from itertools import count


def input():
    with open("stamps.in", "r") as f:
        K, _N = tuple(map(int, f.readline().strip().split()))
        stamps = list(map(int, f.read().replace('\n', '').split()))
        return K, stamps


def solve(K, stamps):
    # s[m] is the minimum number of stamps needed to construct sum m
    # s[m] = min(s[m-n])+1 for each stamp n <= m

    s = [0]
    for m in count(1, 1):
        s.append(0)
        s[m] = 1 + min([s[m-n] for n in stamps if m >= n])

        if s[m] > K:
            return m-1


def output(res):
    with open("stamps.out", "w") as f:
        f.write("%d\n" % res)


K, stamps = input()
res = solve(K, stamps)
output(res)
