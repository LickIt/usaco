"""
ID: giliev91
LANG: PYTHON3
TASK: ttwo
"""

SIZE = 10

with open("ttwo.in", "r") as f:
    G = [None for _ in range(SIZE)]
    for i in range(SIZE):
        G[i] = list(f.readline().strip())

# find farmer and cows
for i in range(SIZE):
    for j in range(SIZE):
        if G[i][j] == "F":
            F = (i, j, "N")
        if G[i][j] == "C":
            C = (i, j, "N")


def next_step(i, j, d):
    if d == "N":
        if i == 0 or G[i-1][j] == "*":
            return (i, j, "E")
        else:
            return (i-1, j, d)
    elif d == "E":
        if j == SIZE-1 or G[i][j+1] == "*":
            return (i, j, "S")
        else:
            return (i, j+1, d)
    elif d == "S":
        if i == SIZE-1 or G[i+1][j] == "*":
            return (i, j, "W")
        else:
            return (i+1, j, d)
    elif d == "W":
        if j == 0 or G[i][j-1] == "*":
            return (i, j, "N")
        else:
            return (i, j-1, d)
    else:
        raise Exception("invalid direction " + d)


visited = set()
steps = 0

# simulate steps
while F[:2] != C[:2] and (F, C) not in visited:
    visited.add((F, C))
    F = next_step(*F)
    C = next_step(*C)
    steps += 1

with open("ttwo.out", "w") as f:
    if F[:2] == C[:2]:
        f.write("%d\n" % steps)
    else:
        f.write("0\n")
