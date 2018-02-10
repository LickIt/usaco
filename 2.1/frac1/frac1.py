"""
ID: giliev91
LANG: PYTHON3
TASK: frac1
"""
import math

with open("frac1.in", "r") as f:
    N = int(f.readline().strip())

fracts = []
for i in range(N+1):
    for j in range(i, N+1):
        if math.gcd(i, j) == 1:
            fracts.append((i, j))

fracts.sort(key=lambda x: x[0] / x[1])

with open("frac1.out", "w") as f:
    for fract in fracts:
        f.write("%d/%d\n" % fract)
