with open("Day9.txt", "r") as file:
    data = file.read()

grid = []
for line in data.split():
    if line:
        grid.append([int(i) for i in line])

height = len(grid)
width = len(grid[0])

low_points = []
for y, line in enumerate(grid):
    for x, value in enumerate(line):
        if x > 0 and line[x - 1] <= value:
            continue
        if x < width - 1 and line[x + 1] <= value:
            continue
        if y > 0 and grid[y - 1][x] <= value:
            continue
        if y < height - 1 and grid[y + 1][x] <= value:
            continue
        low_points.append((x, y))

total = 0
for x, y in low_points:
    total += int(grid[y][x]) + 1
print(total)

basin_sizes = []
for low_x, low_y, in low_points:
    size = 0
    to_expand = [(low_x, low_y)]
    while to_expand:
        x, y = to_expand.pop(-1)
        if grid[y][x] == 9:
            continue
        size += 1
        grid[y][x] = 9
        if x > 0:
            to_expand.append((x - 1, y))
        if x < width - 1:
            to_expand.append((x + 1, y))
        if y > 0:
            to_expand.append((x, y - 1))
        if y < height - 1:
            to_expand.append((x, y + 1))
    basin_sizes.append(size)

basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])