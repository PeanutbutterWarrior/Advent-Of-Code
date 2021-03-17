from collections import defaultdict
from copy import deepcopy

with open('Day17.txt', 'r') as file:
    data = file.read().split()

board = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))

for y, line in enumerate(data):
    for x, char in enumerate(line):
        board[0][y][x] = char == '#'


# Part 1

def get_neighbours(x, y, z):
    count = 0
    for dz in range(-1, 2):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == dy == dz == 0:
                    continue
                if board[z + dz][y + dy][x + dx]:
                    count += 1
    return count


minx = miny = -7
minz = -7
maxx = maxy = 15
maxz = 7

for round in range(6):
    newboard = deepcopy(board)
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            for z in range(minz, maxz + 1):
                neighbours = get_neighbours(x, y, z)
                if board[z][y][x] and (neighbours < 2 or neighbours > 3):
                    board[z][y][x] = False
                elif (not board[z][y][x]) and neighbours == 3:
                    board[z][y][x] = True
    board = newboard

count = 0
for i in board.values():
    for j in i.values():
        for k in j.values():
            if k:
                count += 1
print(count)