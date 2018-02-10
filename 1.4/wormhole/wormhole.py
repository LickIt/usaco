"""
ID: giliev91
LANG: PYTHON3
TASK: wormhole
"""

with open("wormhole.in", "r") as f:
    N = int(f.readline().strip())
    holes = [tuple(map(int, x.strip().split())) for x in f.readlines()]


# build natural edges along +x
walkable = [None for _ in range(N)]
holes_by_y = sorted([(y, x, i) for i, (x, y) in enumerate(holes)])
for i in range(len(holes_by_y) - 1):
    if holes_by_y[i][0] == holes_by_y[i + 1][0]:
        walkable[holes_by_y[i][2]] = holes_by_y[i + 1][2]


# build all hole combinations
def gen(i, h):
    global N

    if i == N - 1:
        if find_cycle(h):
            # yield h
            yield 1
        return

    if h[i] is not None:
        yield from gen(i + 1, h)
        return

    for j in range(i + 1, N):
        if h[j] is not None:
            continue

        hh = list(h)
        hh[i] = j
        hh[j] = i
        yield from gen(i + 1, hh)


# check for cycles
def find_cycle(h):
    global walkable

    for start in range(len(h)):
        v = h[start]
        while True:
            d = walkable[v]
            if d is None:
                break

            if d == start:
                return True

            v = h[d]

    return False

combinations = list(gen(0, [None for _ in range(N)]))

with open("wormhole.out", "w") as f:
    f.write(str(sum(combinations)) + "\n")
