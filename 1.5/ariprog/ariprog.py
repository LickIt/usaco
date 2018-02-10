"""
ID: giliev91
LANG: PYTHON3
TASK: ariprog
"""

with open("ariprog.in", "r") as f:
    N = int(f.readline().strip())
    M = int(f.readline().strip())

bisq = set()
for i in range(M + 1):
    for j in range(i, M + 1):
        bisq.add(i**2 + j**2)


seq = []
for b in range(1, (2 * M**2) // (N - 1) + 2):
    for a in bisq:
        x = a
        for i in range(N):
            if x not in bisq:
                break
            x += b
        else:
            seq.append((a, b))


with open("ariprog.out", "w") as f:
    if seq:
        for s in seq:
            f.write("%d %d\n" % s)
    else:
        f.write("NONE\n")
