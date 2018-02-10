"""
ID: giliev91
LANG: PYTHON3
TASK: sprime
"""
import math

with open("sprime.in", "r") as f:
    N = int(f.readline().strip())

f = open("sprime.out", "w")


def is_prime(x):
    if x % 2 == 0:
        return x == 2

    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False

    return True


def gen(prime, depth):
    if depth == N:
        # print(prime)
        f.write(str(prime) + "\n")
        return

    for i in range(1, 10, 2):
        p = prime * 10 + i
        if is_prime(p):
            gen(p, depth+1)


for x in [2, 3, 5, 7]:
    gen(x, 1)

f.close()
