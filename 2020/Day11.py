from copy import deepcopy

with open('Day11.txt', 'r') as file:
    data = list(map(list, file.read().split()))


# Part 1

def count_neighbours(x, y, data):
    count = 0
    for dx in range(-1, 2):
        ax = x + dx
        if ax < 0:
            continue
        for dy in range(-1, 2):
            ay = y + dy
            if ay < 0:
                continue
            if not dx == dy == 0:
                try:
                    count += int(data[y + dy][x + dx] == '#')
                except IndexError:
                    pass
    return count


board = deepcopy(data)
WIDTH = len(board[0])
HEIGHT = len(board)
changed = set((x, y) for y in range(HEIGHT) for x in range(WIDTH))

while len(changed) > 0:
    new_board = deepcopy(board)
    new_changed = set()
    for x, y in changed:
        if x < 0 or y < 0:
            continue
        try:
            tile = board[y][x]
        except IndexError:
            continue
        if tile != '.':
            neighbours = count_neighbours(x, y, board)
            if tile == 'L' and neighbours == 0:
                new_board[y][x] = '#'
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        new_changed.add((x + dx, y + dy))
            elif tile == '#' and neighbours >= 4:
                new_board[y][x] = 'L'
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        new_changed.add((x + dx, y + dy))
    changed = new_changed
    board = new_board

count = 0
for line in board:
    count += line.count('#')
print(count)


# Part 2

def count_neighbours(x, y, data):
    count = 0
    neighbours = set()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if not dx == dy == 0:
                ax = x + dx
                ay = y + dy
                try:
                    while data[ay][ax] == '.':
                        ax += dx
                        ay += dy
                        if ax < 0 or ay < 0:
                            break
                    else:
                        if ax < 0 or ay < 0:
                            continue
                        neighbours.add((ax, ay))
                        count += int(data[ay][ax] == '#')
                except IndexError:
                    continue
    return count, neighbours


board = deepcopy(data)
WIDTH = len(board[0])
HEIGHT = len(board)
changed = set((x, y) for y in range(HEIGHT) for x in range(WIDTH))

while len(changed) > 0:
    new_board = deepcopy(board)
    new_changed = set()
    for x, y in changed:
        if x < 0 or y < 0:
            continue
        try:
            tile = board[y][x]
        except IndexError:
            continue
        if tile != '.':
            num_neighbours, neighbours = count_neighbours(x, y, board)
            if tile == 'L' and num_neighbours == 0:
                new_board[y][x] = '#'
                new_changed |= neighbours
                new_changed.add((x, y))
            elif tile == '#' and num_neighbours >= 5:
                new_board[y][x] = 'L'
                new_changed |= neighbours
                new_changed.add((x, y))
    changed = new_changed
    board = new_board

count = 0
for line in board:
    count += line.count('#')
print(count)