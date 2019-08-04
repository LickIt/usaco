"""
ID: giliev91
LANG: PYTHON2
TASK: maze1
"""
from collections import deque


def vertex(i, j):
    return i * W + j


with open("maze1.in", "r") as f:
    W, H = map(int, f.readline().strip().split())
    M = [None for _ in range(2*H+1)]

    for i in range(2*H+1):
        M[i] = list(f.readline().strip('\n'))

# build the graph
G = [[] for _ in range(W*H)]
for i in range(H):
    # top connections
    row = M[2*i][1::2]
    if i != 0:
        for j in range(W):
            if row[j] == ' ':
                G[vertex(i-1, j)].append(vertex(i, j))
                G[vertex(i, j)].append(vertex(i-1, j))

    # side connections
    row = M[2*i+1][:-1:2]
    for j in range(1, W):
        if row[j] == ' ':
            G[vertex(i, j-1)].append(vertex(i, j))
            G[vertex(i, j)].append(vertex(i, j-1))


# find exit points
exits = []
for i in [0, 2*H]:
    for j in range(W):
        if M[i][j*2+1] == ' ':
            exits.append(vertex(0 if i == 0 else H-1, j))

for j in [0, 2*W]:
    for i in range(H):
        if M[i*2+1][j] == ' ':
            exits.append(vertex(i, 0 if j == 0 else W-1))


# find longest path with BFS
def longest_path(exits):
    visited = set(exits)
    queue = deque([(e, 1) for e in exits])

    while queue:
        v, dist = queue.popleft()

        for child in G[v]:
            if child not in visited:
                queue.append((child, dist+1))
                visited.add(child)

    return dist


# find longest paths from all exits
res = longest_path(exits)

with open("maze1.out", "w") as f:
    f.write("%d\n" % res)
