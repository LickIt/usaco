"""
ID: giliev91
LANG: PYTHON3
TASK: humble
"""
from heapq import heapify, heapreplace


def input():
    with open("humble.in", "r") as f:
        _K, N = tuple(map(int, f.readline().strip().split()))
        factors = [int(x) for x in f.readline().strip().split()]

        return N, factors


def solve(N, factors):
    humble = [factors[0]]
    heap = [(factor, factor, -1) for factor in factors]
    heapify(heap)

    while len(humble) < N:
        value, factor, idx = heap[0]
        if value > humble[-1]:
            humble.append(value)  # no duplicates

        heapreplace(heap, (factor * humble[idx+1], factor, idx+1))

    return humble[-1]


def output(result):
    with open("humble.out", "w") as f:
        f.write("%d\n" % result)


N, factors = input()
num = solve(N, factors)
output(num)
