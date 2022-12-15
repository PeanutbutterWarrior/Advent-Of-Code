from enum import Enum, auto


def print_grid(grid):
    for line in grid:
        for cell in line:
            if cell == Cell.Empty:
                print(' ', end='')
            elif cell == Cell.Rock:
                print('#', end='')
            elif cell == Cell.Sand:
                print('.', end='')
        print()


with open("Day14.txt", "r") as file:
    data = file.read()


class Cell(Enum):
    Empty = auto()
    Rock = auto()
    Sand = auto()


grid = [[Cell.Empty for _ in range(1000)] for _ in range(200)]

max_y = 0
for line in data.split('\n'):
    start, *positions = line.split(' -> ')
    start_x, start_y = map(int, start.split(','))
    if start_y > max_y:
        max_y = start_y
    for position in positions:
        end_x, end_y = position.split(',')
        end_x = int(end_x)
        end_y = int(end_y)
        if end_y > max_y:
            max_y = end_y
        for x in range(min(end_x, start_x), max(end_x, start_x) + 1):
            for y in range(min(end_y, start_y), max(end_y, start_y) + 1):
                grid[y][x] = Cell.Rock
        start_x = end_x
        start_y = end_y
grid[max_y + 2] = [Cell.Rock for _ in range(1000)]
grid = grid[:max_y + 3]

sand_count = 0
while grid[0][500] == Cell.Empty:
    sand_x = 500
    sand_y = 0
    while True:
        if grid[sand_y + 1][sand_x] == Cell.Empty:
            sand_y += 1
        elif grid[sand_y + 1][sand_x - 1] == Cell.Empty:
            sand_y += 1
            sand_x -= 1
        elif grid[sand_y + 1][sand_x + 1] == Cell.Empty:
            sand_y += 1
            sand_x += 1
        else:
            grid[sand_y][sand_x] = Cell.Sand
            sand_count += 1
            break
print(sand_count)
