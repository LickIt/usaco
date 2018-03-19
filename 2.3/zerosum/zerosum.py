"""
ID: giliev91
LANG: PYTHON3
TASK: zerosum
"""
from itertools import chain, product

with open("zerosum.in", "r") as f:
    N = int(f.readline().strip())

result = []
for op in product(' +-', repeat=N-1):
    expr = zip(op, map(str, range(2, N+1)))
    expr = "".join(chain(*expr))
    expr = "1" + expr
    if eval(expr.replace(" ", "")) == 0:
        result += [expr]

with open("zerosum.out", "w") as f:
    for expr in result:
        f.write(expr + "\n")
