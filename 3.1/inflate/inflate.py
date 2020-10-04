"""
ID: giliev91
LANG: PYTHON3
TASK: inflate
"""


def input():
    with open("inflate.in", "r") as f:
        M, _N = tuple(map(int, f.readline().strip().split()))
        categories = [tuple(map(int, line.strip().split()))
                      for line in f.readlines()]

        return M, categories


def solve(M, categories):
    best = [0] * (M+1)
    for i in range(M+1):
        for points, time in categories:
            if i >= time:
                best[i] = max(best[i], best[i-time] + points)

    return best


def output(result):
    with open("inflate.out", "w") as f:
        f.write("%d\n" % result)


M, categories = input()
best = solve(M, categories)
output(best[M])
