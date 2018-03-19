"""
ID: giliev91
LANG: PYTHON2
TASK: nocows
"""
with open("nocows.in", "r") as f:
    N, K = map(int, f.readline().strip().split())

trees = [[0]*(N+1) for _ in range(K+1)]
trees[1][1] = 1

for k in range(2, K+1):
    for n in range(1, N+1):
        trees[k][n] = trees[k-1][n]
        # for i in range(1, n-1):
        #     trees[k][n] += trees[k-1][i] * trees[k-1][n-i-1]
        #     trees[k][n] -= trees[k-2][i] * trees[k-2][n-i-1]

        # python is slow so halve the loop .....
        for i in range(1, n//2):
            trees[k][n] += 2 * trees[k-1][i] * trees[k-1][n-i-1]
            trees[k][n] -= 2 * trees[k-2][i] * trees[k-2][n-i-1]

        if n % 2 == 1:
            i = n // 2
            trees[k][n] += trees[k-1][i] * trees[k-1][n-i-1]
            trees[k][n] -= trees[k-2][i] * trees[k-2][n-i-1]

        trees[k][n] %= 9901

with open("nocows.out", "w") as f:
    f.write(str((trees[K][N] - trees[K-1][N]) % 9901) + "\n")
