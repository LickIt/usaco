"""
ID: giliev91
LANG: PYTHON3
TASK: contact
"""


def input():
    with open("contact.in", "r") as f:
        A, B, N = tuple(map(int, f.readline().strip().split()))
        sequence = [int(x) for x in f.read().replace('\n', '')]
        return A, B, N, sequence


def solve(A, B, N, sequence):
    occurances = [[0] * 2**i for i in range(B+1)]

    # calculate all numbers with all bit lengths
    # reuse older values calculation by just adding the new bit at the end
    values = [[] for _ in range(B+1)]
    values[0] = [0] * len(sequence)
    for bitlen in range(1, B+1):
        for pos in range(len(sequence) - bitlen + 1):
            value = values[bitlen - 1][pos] * 2 + sequence[pos + bitlen - 1]
            occurances[bitlen][value] += 1
            values[bitlen].append(value)

    # sort by number of occurances, bit length and value
    result = []
    for bitlen, occurance in enumerate(occurances[A:], A):
        for value, count in enumerate(occurance):
            if count > 0:
                result.append((count, bitlen, value))

    result.sort(key=lambda x: (-x[0], x[1], x[2]))

    # group by number of occurances
    groups = []
    pos = i = 0
    while i < N and pos < len(result):
        items = []

        count = result[pos][0]
        while pos < len(result) and result[pos][0] == count:
            count, bitlen, value = result[pos]
            items.append(bin(value)[2:].zfill(bitlen))
            pos += 1

        groups.append((count, items))
        i += 1

    return groups


def output(groups):
    with open("contact.out", "w") as f:
        for count, items in groups:
            f.write("%d\n" % count)
            for i in range(0, len(items), 6):
                f.write("%s\n" % " ".join(items[i:i+6]))


A, B, N, sequence = input()
groups = solve(A, B, N, sequence)
output(groups)
