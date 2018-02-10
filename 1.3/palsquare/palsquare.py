"""
ID: giliev91
LANG: PYTHON3
TASK: palsquare
"""
N = 301
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("palsquare.in", "r") as f:
    B = int(f.readline().strip())


def toBase(x, b):
    rem = []
    while x != 0:
        rem.append(x % b)
        x //= b

    return "".join(map(lambda r: alphabet[r], reversed(rem)))

res = []
for i in range(1, N):
    x = toBase(i, B)
    sq = toBase(i**2, B)

    if list(sq) == list(reversed(sq)):
        res.append((x, sq))

with open("palsquare.out", "w") as f:
    for p in res:
        f.write("%s %s\n" % p)
