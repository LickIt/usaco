"""
ID: giliev91
LANG: PYTHON3
TASK: agrinet
"""
inf = 1e10


def input():
    with open("agrinet.in", "r") as f:
        N = int(f.readline().strip())
        G = [[] for _ in range(N)]
        for x in range(N):
            while len(G[x]) < N:
                G[x] += [int(d) for d in f.readline().strip().split()]

    return G


def min_tree(G, start=0):
    N = len(G)
    tree = set([start])
    dist = G[start]
    dist[start] = inf
    edges = []

    while len(tree) < N:
        edge, v = min([(dist, idx) for idx, dist in enumerate(dist)])
        edges.append(edge)
        tree.add(v)
        dist[v] = inf

        for x in range(N):
            if x not in tree and x != v:
                dist[x] = min(dist[x], G[v][x])

    return edges


def output(edges):
    with open("agrinet.out", "w") as f:
        f.write("%d\n" % sum(edges))


G = input()
edges = min_tree(G)
output(edges)
