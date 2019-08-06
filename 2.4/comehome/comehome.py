"""
ID: giliev91
LANG: PYTHON3
TASK: comehome
"""
INF = 1e10


def input():
    with open("comehome.in", "r") as f:
        P = int(f.readline().strip())
        G = {}
        for i in range(P):
            i, j, d = f.readline().strip().split()

            if i not in G:
                G[i] = []
            if j not in G:
                G[j] = []

            G[i].append((j, int(d)))
            G[j].append((i, int(d)))

    return G


def dijkstra(G, source):
    dist = {v: INF for v in G}
    dist[source] = 0
    visited = set()

    while len(visited) < len(G):
        i, _ = min([(v, d) for v, d in dist.items() if v not in visited],
                   key=lambda x: x[1])

        visited.add(i)

        for j, d in G[i]:
            if dist[j] > dist[i] + d:
                dist[j] = dist[i] + d

    return dist


def closest_cow(dist):
    cows = set([chr(c) for c in range(ord("A"), ord("Z"))])
    cow = (None, INF)
    for c, d in dist.items():
        if c in cows and cow[1] > d:
            cow = (c, d)

    return cow


def output(res):
    with open("comehome.out", "w") as f:
        f.write("%s %d\n" % res)


G = input()
dist = dijkstra(G, 'Z')
res = closest_cow(dist)
output(res)
