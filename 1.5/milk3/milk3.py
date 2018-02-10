"""
ID: giliev91
LANG: PYTHON3
TASK: milk3
"""

with open("milk3.in", "r") as f:
    buckets = tuple(map(int, f.readline().strip().split()))

used = set()
queue = [(0, 0, buckets[2])]
solutions = set([buckets[2]])
while queue:
    b = queue.pop()
    used.add(b)
    for i in range(3):
        for j in range(3):
            if i != j:
                new_b = list(b)
                amount = min(buckets[j] - b[j], b[i])
                new_b[j] += amount
                new_b[i] -= amount
                new_b = tuple(new_b)

                if new_b not in used:
                    queue.append(new_b)
                    if new_b[0] == 0:
                        solutions.add(new_b[2])

_sorted = list(sorted(solutions))
with open("milk3.out", "w") as f:
    f.write(str(_sorted[0]))
    for i in range(1, len(_sorted)):
        f.write(" " + str(_sorted[i]))
    f.write("\n")