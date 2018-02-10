"""
ID: giliev91
LANG: PYTHON3
TASK: beads
"""
with open("beads.in", "r") as f:
    N = int(f.readline().strip())
    beads = f.readline().strip()


def split(i):
    left = i
    while beads[left] == "w":
        left = (left - 1) % N
    left_color = beads[left]

    right = i + 1
    while beads[right] == "w":
        right = (right + 1) % N
    right_color = beads[right]

    left = 1
    while left < N and (
            beads[(i - left) % N] == left_color or beads[(i - left) % N] == "w"):
        left += 1
    right = 1
    while right < N and (
            beads[(i + 1 + right) % N] == right_color or beads[(i + 1 + right) % N] == "w"):
        right += 1
    #print(i, left, right)
    return left + right

top = 0
for i in range(N - 1):
    if beads[i] != beads[i + 1]:
        #print(i, split(i))
        top = max(top, split(i))

# if no split can be made all colors are the same
if top == 0 or top == 2 * N:
    top = N

#print(top)
with open("beads.out", "w") as f:
    f.write(str(top) + "\n")
