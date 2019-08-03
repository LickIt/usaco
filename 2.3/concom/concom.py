"""
ID: giliev91
LANG: PYTHON3
TASK: concom
"""
from collections import deque
MAXC = 101

with open("concom.in", "r") as f:
    N = int(f.readline().strip())
    G = [[] for _ in range(MAXC)]
    for line in f.readlines():
        i, j, p = map(int, line.strip().split())
        G[i].append((j, p))


def get_owned(n):
    visited = set()
    queue = deque([n])
    owns = [0] * MAXC
    owns[n] = 100

    while queue:
        i = queue.popleft()
        visited.add(i)

        for j, p in G[i]:
            owns[j] += p

            if j not in visited and owns[j] > 50:
                queue.append(j)

    return [idx for idx, p in enumerate(owns) if p > 50 and idx != n]


res = [[]] * MAXC
for i in range(1, MAXC):
    res[i] = get_owned(i)

with open("concom.out", "w") as f:
    for i in range(1, MAXC):
        for j in res[i]:
            f.write("%d %d\n" % (i, j))
