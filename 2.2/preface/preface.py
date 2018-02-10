"""
ID: giliev91
LANG: PYTHON3
TASK: preface
"""
from collections import OrderedDict

numerals = OrderedDict([(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                        (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")])

with open("preface.in", "r") as f:
    N = int(f.readline().strip())


def to_roman(x):
    res = ""
    for val, c in numerals.items():
        while x >= val:
            res += c
            x -= val
    return res


letters = OrderedDict([("I", 0), ("V", 0), ("X", 0),
                       ("L", 0), ("C", 0), ("D", 0), ("M", 0)])
for i in range(1, N+1):
    for c in to_roman(i):
        letters[c] += 1

with open("preface.out", "w") as f:
    for item in letters.items():
        if item[1] == 0:
            break
        f.write("%s %d\n" % item)
