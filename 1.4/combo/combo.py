"""
ID: giliev91
LANG: PYTHON3
TASK: combo
"""
import itertools

with open("combo.in", "r") as f:
    N = int(f.readline().strip())
    john = tuple(map(int, f.readline().strip().split()))
    master = tuple(map(int, f.readline().strip().split()))

x = set(itertools.product(*[[((x-1) % N) + 1 for x in range(e - 2, e + 3)] for e in john]))
y = set(itertools.product(*[[((x-1) % N) + 1 for x in range(e - 2, e + 3)] for e in master]))

# print(x, y)
# print(len(x), len(y))
# print(len(x | y))

with open("combo.out", "w") as f:
    f.write(str(len(x | y)) + "\n")