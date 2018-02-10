"""
ID: giliev91
LANG: PYTHON3
TASK: skidesign
"""
MAX_HEIGHT = 100
MAX_DIFF = 17

with open("skidesign.in", "r") as f:
    N = int(f.readline().strip())
    hills = [int(x.strip()) for x in f.readlines()]


def calc(min_, max_, hills):
    total = 0
    for hill in hills:
        if hill < min_:
            total += (min_ - hill) ** 2
        elif hill > max_:
            total += (hill - max_) ** 2

    return total

min_cost = 1000 * MAX_HEIGHT ** 2
for i in range(MAX_HEIGHT):
    cost = calc(i, i + MAX_DIFF, hills)
    min_cost = min(min_cost, cost)

with open("skidesign.out", "w") as f:
    f.write(str(min_cost) + "\n")