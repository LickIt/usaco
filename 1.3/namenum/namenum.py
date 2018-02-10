"""
ID: giliev91
LANG: PYTHON3
TASK: namenum
"""
with open("namenum.in", "r") as f:
    N = f.readline().strip()

with open("dict.txt", "r") as f:
    names = [x.strip() for x in f.readlines()]

alphabet = {"A": 2, "B": 2, "C": 2,
            "D": 3, "E": 3, "F": 3,
            "G": 4, "H": 4, "I": 4,
            "J": 5, "K": 5, "L": 5,
            "M": 6, "N": 6, "O": 6,
            "P": 7, "R": 7, "S": 7,
            "T": 8, "U": 8, "V": 8,
            "W": 9, "X": 9, "Y": 9,
            "Q": -1, "Z": -1}

valid = []
for name in names:
    if len(name) != len(N):
        continue

    for c, num in zip(list(name), list(N)):
        if str(alphabet[c]) != num:
            break
    else:
        valid.append(name)

with open("namenum.out", "w") as f:
    if len(valid) > 0:
        for name in valid:
            f.write(name + "\n")
    else:
        f.write("NONE\n")
