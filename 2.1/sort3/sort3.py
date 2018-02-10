"""
ID: giliev91
LANG: PYTHON3
TASK: sort3
"""
with open("sort3.in", "r") as f:
    N = int(f.readline().strip())
    seq = list(map(int, f.readlines()))

target = list(sorted(seq))
wrong = [[0 for j in range(3)] for x in range(3)]
for i in range(N):
    if seq[i] != target[i]:
        wrong[target[i] - 1][seq[i] - 1] += 1

swaps = 0
for i in range(3):
    for j in range(3):
        if i == j:
            continue

        # optimal swaps (i, j) with length 1
        amount = min(wrong[i][j], wrong[j][i])
        wrong[i][j] -= amount
        wrong[j][i] -= amount
        swaps += amount

# non optimal swaps (i, j, k) with length 2
swaps += max(wrong[0]) * 2

with open("sort3.out", "w") as f:
    f.write(str(swaps) + "\n")
