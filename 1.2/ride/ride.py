"""
ID: giliev91
LANG: PYTHON3
TASK: ride
"""
fin = open("ride.in", "r")
fout = open("ride.out", "w")

def mult(_list):
    res = 1
    for x in _list:
        res *= x
        res %= 47
    return res


sums = [[ord(c) - 64 for c in line.strip()] for line in fin.readlines()]
sums = [mult(x) for x in sums]
fout.write ("GO\n" if sums[0] == sums[1] else "STAY\n")