"""
ID: giliev91
LANG: PYTHON3
TASK: numtri
"""
with open("numtri.in", "r") as f:
    N = int(f.readline().strip())
    rows = [tuple(map(int, x.strip().split())) for x in f.readlines()]

best = [0 for _ in range(N)]
for row in rows:
    for i in range(len(row) - 1, 0, -1):
        best[i] = max(best[i-1], best[i]) + row[i]
    best[0] = best[0] + row[0]
    # print(best[:len(row)])

with open("numtri.out", "w") as f:
    f.write(str(max(best)) + "\n")