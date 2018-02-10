"""
ID: giliev91
LANG: PYTHON3
TASK: hamming
"""
with open("hamming.in", "r") as f:
    N, B, D = map(int, f.readline().strip().split())


def gen(s, seq, depth):
    if depth == N:
        return seq

    for i in range(s, 2 << B):
        for j in seq:
            bits = bin(i ^ j).count("1")
            if bits < D:
                break
        else:
            res = gen(i+1, seq + [i], depth + 1)
            if res:
                return res

    return None


res = gen(1, [0], 1)

with open("hamming.out", "w") as f:
    for c in [res[i:i + 10] for i in range(0, len(res), 10)]:
        f.write(str(c[0]))
        for i in range(1, len(c)):
            f.write(" " + str(c[i]))
        f.write("\n")
