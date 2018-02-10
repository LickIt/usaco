"""
ID: giliev91
LANG: PYTHON3
TASK: barn1
"""
with open("barn1.in", "r") as f:
    M, S, C = map(int, f.readline().strip().split())
    stalls = list(map(int, f.readlines()))
    stalls.sort()

# make intervals
intervals = []
start = stalls[0]
for i in range(1, C):
    if stalls[i] != stalls[i-1] + 1:
        intervals.append((start, stalls[i-1]))
        start = stalls[i]
intervals.append((start, stalls[i]))
#print(intervals)

if len(intervals) <= M:
    res = C
else:
    # calculate gaps and bridge the smallest ones
    gaps = [intervals[i+1][0] - intervals[i][1] - 1 for i in range(0, len(intervals) - 1)]
    add = sum(sorted(gaps)[:len(intervals)-M])
    res = C + add

with open("barn1.out", "w") as f:
    f.write(str(res) + "\n")