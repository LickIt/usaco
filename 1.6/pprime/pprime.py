"""
ID: giliev91
LANG: PYTHON3
TASK: pprime
"""
import math
with open("pprime.in", "r") as f:
    A, B = map(int, f.readline().strip().split())


def prime(x):
    if x % 2 == 0:
        return x == 2

    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False

    return True


logA = int(math.floor(math.log10(A)))
logB = int(math.ceil(math.log10(B)))

f = open("pprime.out", "w")
for exp in range(logA, logB):
    for x in range(10**(int(exp / 2)), 10**(int(exp / 2) + 1)):
        pal = str(x)
        if exp % 2:
            pal += pal[::-1]
        else:
            pal += pal[:-1][::-1]

        num = int(pal)
        if num >= A and num <= B and prime(num):
            f.write(pal + "\n")

f.close()
