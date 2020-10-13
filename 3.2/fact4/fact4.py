"""
ID: giliev91
LANG: PYTHON3
TASK: fact4
"""
from math import floor, log


def input():
    with open("fact4.in", "r") as f:
        N = int(f.readline().strip())
        return N


def solve(N):
    num_of_twos = 0
    res = 1
    for i in range(2, N+1):
        while i % 2 == 0:
            num_of_twos += 1
            i = i // 2

        while i % 5 == 0:
            num_of_twos -= 1
            i = i // 5

        res = (res * i) % 10

    return (res * pow(2, num_of_twos, 10)) % 10


def output(res):
    with open("fact4.out", "w") as f:
        f.write("%d\n" % res)


N = input()
res = solve(N)
output(res)
