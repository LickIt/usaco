"""
ID: giliev91
LANG: PYTHON3
TASK: gift1
"""
import math
from collections import OrderedDict

friends = OrderedDict()
with open("gift1.in", "r") as fin:
    NP = int(fin.readline().strip())
    for i in range(NP):
        name = fin.readline().strip()
        friends[name] = 0

    for i in range(NP):
        name = fin.readline().strip()
        money, people = map(lambda x: int(x), fin.readline().strip().split())
        friends[name] -= money

        for j in range(people):
            friend = fin.readline().strip()
            friends[friend] += money // people

        if money != 0:
            friends[name] += money % people

with open("gift1.out", "w") as fout:
    for item in friends.items():
        fout.write("%s %d\n" % item)
