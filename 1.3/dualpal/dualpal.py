"""
ID: giliev91
LANG: PYTHON3
TASK: dualpal
"""
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("dualpal.in", "r") as f:
    N, S = map(int, f.readline().strip().split())


def toBase(x, b):
    rem = []
    while x != 0:
        rem.append(x % b)
        x //= b

    return "".join(map(lambda r: alphabet[r], reversed(rem)))


def palindrome(x):
    return list(x) == list(reversed(x))

res = []
for i in range(N):
    while True:
        S += 1
        p = [palindrome(toBase(S, b)) for b in range(2, 11)]
        if p.count(True) > 1:
            res.append(S)
            break

with open("dualpal.out", "w") as f:
    for p in res:
        f.write(str(p) + "\n")
