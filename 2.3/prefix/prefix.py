"""
ID: giliev91
LANG: PYTHON3
TASK: prefix
"""
prefixes = []
sequence = ""

with open("prefix.in", "r") as f:
    while True:
        line = f.readline().strip()
        if line == ".":
            break
        prefixes += [x.strip() for x in line.split()]

    sequence = "".join([x.strip() for x in f.readlines()])


subseq = [False]*(len(sequence)+1)
subseq[0] = True
for i in range(1, len(sequence)+1):
    for prefix in prefixes:
        if len(prefix) <= i:
            if sequence[i-len(prefix):i] == prefix and subseq[i-len(prefix)]:
                subseq[i] = True
                break


for idx, value in enumerate(reversed(subseq)):
    if value:
        break

with open("prefix.out", "w") as f:
    f.write(str(len(subseq) - 1 - idx) + "\n")
