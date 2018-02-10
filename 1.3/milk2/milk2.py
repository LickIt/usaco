"""
ID: giliev91
LANG: PYTHON3
TASK: milk2
"""
intervals = []
with open("milk2.in", "r") as f:
    N = int(f.readline().strip())
    for i in range(N):
        intervals.append(tuple(map(int, f.readline().strip().split())))

intervals.sort()

merged = []
it = intervals[0]
for i in range(1, N):
    # merge if there is overlap
    if it[1] >= intervals[i][0]:
        it = (it[0], max(it[1], intervals[i][1]))
    else:
        merged.append(it)
        it = intervals[i]
merged.append(it)

#print(intervals)
#print(merged)

max_milk = max([b - a for a, b in merged])
max_nomilk = max([merged[i + 1][0] - merged[i][1]
                  for i in range(0, len(merged) - 1)] or [0])

with open("milk2.out", "w") as f:
    f.write("%d %d\n" % (max_milk, max_nomilk))
