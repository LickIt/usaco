"""
ID: giliev91
LANG: PYTHON3
TASK: lamps
"""
from itertools import combinations

with open("lamps.in", "r") as f:
    N = int(f.readline().strip())
    C = int(f.readline().strip())
    ON = list(map(int, f.readline().strip().split()))[:-1]
    OFF = list(map(int, f.readline().strip().split()))[:-1]


def apply(but, lamps):
    if but == 1:
        return [not x for x in lamps]
    if but == 2:
        return [not x if (idx+1) % 2 == 1 else x for idx, x in enumerate(lamps)]
    if but == 3:
        return [not x if (idx+1) % 2 == 0 else x for idx, x in enumerate(lamps)]
    if but == 4:
        return [not x if (idx+1) % 3 == 1 else x for idx, x in enumerate(lamps)]


# find all possible presses of nCr switches
possible = [[] for _ in range(5)]
for r in range(5):
    for c in combinations(range(1, 5), r):
        lamps = [True] * N
        for but in c:
            lamps = apply(but, lamps)
        possible[r].append(lamps)


# valid solutions are with length `r`
# where `r` must satisfy `r + 2*k = C`
solutions = []
for r in range(5):
    if r <= C and (C - r) % 2 == 0:
        for lamps in possible[r]:
            valid = True
            for j in ON:
                if not lamps[j-1]:
                    valid = False
                    break

            for j in OFF:
                if lamps[j-1]:
                    valid = False
                    break

            if valid:
                solutions.append(lamps)

res = set(["".join(["1" if x else "0" for x in s]) for s in solutions])
with open("lamps.out", "w") as f:
    if not res:
        f.write("IMPOSSIBLE\n")
    else:
        for s in sorted(res):
            f.write(s + "\n")
