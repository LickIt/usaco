"""
ID: giliev91
LANG: PYTHON3
TASK: transform
"""
with open("transform.in", "r") as f:
    N = int(f.readline().strip())
    before = [list(x.strip()) for x in [f.readline() for _ in range(N)]]
    after = [list(x.strip()) for x in [f.readline() for _ in range(N)]]


def rotate(m):
    return [list(x) for x in zip(*reversed(m))]


def flip(m):
    return [list(reversed(x)) for x in m]

res = 7
if after == rotate(before):
    res = 1
elif after == rotate(rotate(before)):
    res = 2
elif after == rotate(rotate(rotate(before))):
    res = 3
elif after == flip(before):
    res = 4
elif after == rotate(flip(before)) or \
        after == rotate(rotate(flip(before))) or \
        after == rotate(rotate(rotate(flip(before)))):
    res = 5
elif after == before:
    res = 6

with open("transform.out", "w") as f:
    f.write(str(res) + "\n")
