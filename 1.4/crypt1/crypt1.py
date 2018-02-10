"""
ID: giliev91
LANG: PYTHON3
TASK: crypt1
"""
import itertools

with open("crypt1.in", "r") as f:
    N = int(f.readline().strip())
    nums = set([int(x) for x in f.readline().strip().split()])


def list_to_int(x):
    return int("".join(map(str, x)))


def int_to_list(x):
    return [int(d) for d in str(x)]

first = list(map(list_to_int, itertools.product(nums, repeat=3)))
second = list(map(list_to_int, itertools.product(nums, repeat=2)))

total = 0
for x in first:
    for y in second:
        p1 = int_to_list(x * (y % 10))
        p2 = int_to_list(x * (y // 10))
        res = int_to_list(x * y)

        if len(p1) == 3 and len(p2) == 3 and len(res) == 4 \
                and set(p1).issubset(nums) and set(p2).issubset(nums) and set(res).issubset(nums):
            total += 1
            # print(x, y, p1, p2, res)

with open("crypt1.out", "w") as f:
    f.write(str(total) + "\n")