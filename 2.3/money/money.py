"""
ID: giliev91
LANG: PYTHON2
TASK: money
"""

with open("money.in", "r") as f:
    V, N = map(int, f.readline().strip().split())
    coins = []
    for line in f.readlines():
        coins += list(map(int, line.strip().split()))

sums = [[0] * (N+1) for _ in range(V+1)]
sums[0][0] = 1

for v in range(1, V+1):
    coin = coins[v-1]

    # F(v, n) = F(v-1, n) + F(v, n - coin)
    for n in range(N+1):
        sums[v][n] += sums[v-1][n]
        if n >= coin:
            sums[v][n] += sums[v][n-coin]

with open("money.out", "w") as f:
    f.write(str(sums[V][N]) + "\n")
