"""
ID: giliev91
LANG: PYTHON3
TASK: holstein
"""
with open("holstein.in", "r") as f:
    V = int(f.readline().strip())
    vitamins = [int(x) for x in f.readline().strip().split()]
    G = int(f.readline().strip())
    feeds = [[int(y) for y in x.strip().split()] for x in f.readlines()]


def is_enough(x):
    total = [0] * V
    for i in range(G):
        if x & (1 << i):
            for idx, val in enumerate(feeds[i]):
                total[idx] += val

    for i in range(V):
        if total[i] < vitamins[i]:
            return False

    return True


min_len = G
min_g = (2 << G) - 1
for g in range(1 << G):
    if is_enough(g):
        g_len = bin(g).count("1")
        if g_len < min_len:
            min_len = g_len
            min_g = g

with open("holstein.out", "w") as f:
    f.write(str(min_len))
    for i in range(G):
        if min_g & (1 << i):
            f.write(" " + str(i + 1))
    f.write("\n")
