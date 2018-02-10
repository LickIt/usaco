"""
ID: giliev91
LANG: PYTHON3
TASK: castle
"""

directions = {(0, -1): 1, (-1, 0): 2, (0, 1): 4, (1, 0): 8}

with open("castle.in", "r") as f:
    M, N = map(int, f.readline().strip().split())
    castle = [[int(y) for y in x.strip().split()] for x in f.readlines()]


def tuple_sum(a, b):
    return (a[0] + b[0], a[1] + b[1])


def bfs(i, j, used):
    queue = [(i, j)]
    used.add((i, j))
    while queue:
        cur = queue.pop()
        yield cur
        for direction, mask in directions.items():
            pos = tuple_sum(cur, direction)
            if pos[0] >= 0 and pos[1] >= 0 and pos[0] < N and pos[1] < M:
                if pos not in used and (castle[cur[0]][cur[1]] & mask) == 0:
                    queue.append(pos)
                    used.add(pos)


# find connected components
used = set()
rooms = []
for i in range(N):
    for j in range(M):
        if (i, j) not in used:
            rooms.append(list(bfs(i, j, used)))

num_rooms = len(rooms)
biggest_room = max([len(x) for x in rooms])

# reverse lookup for room size based on coordinates
room_size = [[0 for j in range(M)] for i in range(N)]
for idx, room in enumerate(rooms):
    size = len(room)
    for i, j in room:
        room_size[i][j] = (size, idx)


max_size = 0
wall = ()
for j in range(M):
    for i in reversed(range(N)):
        # North, East
        for d in [(-1, 0), (0, 1)]:
            if castle[i][j] & directions[d]:
                pos = tuple_sum((i, j), d)
                if pos[0] >= 0 and pos[1] >= 0 and pos[0] < N and pos[1] < M:
                    if room_size[i][j][1] == room_size[pos[0]][pos[1]][1]:
                        # same room
                        continue

                    size = room_size[i][j][0] + room_size[pos[0]][pos[1]][0]
                    if size > max_size:
                        max_size = size
                        wall = (i+1, j+1, "N" if d == (-1, 0) else "E")


with open("castle.out", "w") as f:
    f.write(str(num_rooms) + "\n")
    f.write(str(biggest_room) + "\n")
    f.write(str(max_size) + "\n")
    f.write("%d %d %s\n" % wall)
