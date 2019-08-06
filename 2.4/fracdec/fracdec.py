"""
ID: giliev91
LANG: PYTHON3
TASK: fracdec
"""


def input():
    with open("fracdec.in", "r") as f:
        return tuple(map(int, f.readline().strip().split()))


def divide(n, d):
    return (n // d, n % d)


def decimal(n, d):
    whole, n = divide(n, d)
    decimals = []
    used = set()

    q, r = divide(n * 10, d)
    while (q, r) not in used:
        # no repeating
        if (q, r) == (0, 0):
            break

        used.add((q, r))
        decimals.append((q, r))
        q, r = divide(r * 10, d)

    repeat_idx = decimals.index((q, r)) if (q, r) != (0, 0) else len(decimals)

    return (
        whole,
        [d[0] for d in decimals[:repeat_idx]],
        [d[0] for d in decimals[repeat_idx:]]
    )


def output(whole, non_repeating, repeating):
    res = str(whole) + "."
    if non_repeating or repeating:
        res += "".join(map(str, non_repeating))
        if repeating:
            res += "(%s)" % "".join(map(str, repeating))
    else:
        res += "0"

    with open("fracdec.out", "w") as f:
        for line in [res[i:i+76] for i in range(0, len(res), 76)]:
            f.write(line + "\n")


N, D = input()
res = decimal(N, D)
output(*res)
