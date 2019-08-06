"""
ID: giliev91
LANG: PYTHON2
TASK: cowtour
"""
from math import sqrt
INF = 1e12


def weight(x, y):
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


with open("cowtour.in", "r") as f:
    N = int(f.readline().strip())
    V = []
    for i in range(N):
        V.append(tuple(map(int, f.readline().strip().split())))

    M = [None for _ in range(N)]
    for i in range(N):
        M[i] = [bool(int(x)) for x in f.readline().strip()]


# floyd-warshall
dist = [[INF]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if M[i][j]:
            dist[i][j] = weight(V[i], V[j])

for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


# find max distances from each vertex
max_dist = [0]*N
for i in range(N):
    max_dist[i] = max([x for x in dist[i] if x < INF])


# find connected components
fields = []
visited = set()
for i in range(N):
    if i not in visited:
        field = set()

        for j in range(N):
            if dist[i][j] < INF:
                field.add(j)
                visited.add(j)

        fields.append(field)


# find diameter of each component
diameters = [0]*len(fields)
for f in range(len(fields)):
    diam = 0

    for i in fields[f]:
        for j in fields[f]:
            if dist[i][j] > diam:
                diam = dist[i][j]

    diameters[f] = diam


# find min diamter when adding a new
res = []
for a in range(len(fields)):
    for b in range(a+1, len(fields)):
        min_diameter = INF
        for i in fields[a]:
            for j in fields[b]:
                # new diameter either contains the edge (i, j) or it doesn't
                diameter = max(
                    max_dist[i] + max_dist[j] + weight(V[i], V[j]),
                    diameters[a],
                    diameters[b]
                )

                if min_diameter > diameter:
                    min_diameter = diameter

        res.append(min_diameter)


with open("cowtour.out", "w") as f:
    f.write("%.6f\n" % min(res))
