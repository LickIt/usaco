"""
ID: giliev91
LANG: PYTHON3
TASK: subset
"""
from math import ceil
with open("subset.in", "r") as f:
    N = int(f.readline().strip())

sums = [[0] * int(ceil(n * (n+1) / 2)) for n in range(N+1)]
sums[1][0] = 1
for n in range(2, N+1):
    # copy all previous sums (i.e. not add n)
    for i in range(len(sums[n-1])):
        sums[n][i] = sums[n-1][i]
    # add n to each sum to make a new one
    for i in range(len(sums[n]) - n):
        sums[n][i+n] += sums[n-1][i]

if (N * (N+1)) % 4 != 0:
    res = 0
else:
    res = sums[N][(N * (N+1)) // 4]

with open("subset.out", "w") as f:
    f.write(str(res) + "\n")
