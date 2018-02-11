"""
ID: giliev91
LANG: PYTHON3
TASK: runround
"""

with open("runround.in", "r") as f:
    M = int(f.readline().strip())
    M = list(map(int, format(M+1, "09d")))


def is_runround(num):
    for idx, val in enumerate(num):
        if val != 0:
            break

    num = num[idx:]

    # make sure there are no zeroes
    if not all(num):
        return False

    mod = len(num)
    used = [False] * mod

    x = 0
    for _ in range(mod):
        used[x] = True
        x = (x + num[x]) % mod

    return x == 0 and all(used)


# init flag is used to start the recursion
# from the input number rather than 0
def gen(num, depth, used, init):
    if depth == 9:
        if is_runround(num):
            return num
        return

    start = 1 if init else M[depth]
    for i in range(start, 10):
        if not used[i] or i == 0:
            used[i] = True
            num[depth] = i
            res = gen(num, depth + 1, used, init)
            init = True
            used[i] = False

            if res:
                return res


res = gen([0]*9, 0, [False]*10, False)
res = int("".join(map(str, res)))

with open("runround.out", "w") as f:
    f.write(str(res) + "\n")
