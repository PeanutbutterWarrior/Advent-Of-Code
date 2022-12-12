from collections import deque

with open("Day12.txt", "r") as file:
    data = file.read()

grid = []
start_x, start_y = None, None
end_x, end_y = None, None
for y, line in enumerate(data.split()):
    grid.append([])
    for x, char in enumerate(line):
        if char == 'S':
            start_x, start_y = x, y
            grid[-1].append(0)
        elif char == 'E':
            end_x, end_y = x, y
            grid[-1].append(25)
        else:
            grid[-1].append(ord(char) - 97)

width = len(grid[0])
height = len(grid)
costs = [[float('inf')] * width for _ in range(height)]

to_search = [(end_x, end_y, 0)]
while to_search:
    x, y, cost = to_search.pop(-1)

    if costs[y][x] <= cost:
        continue
    costs[y][x] = cost

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= x + dx < width and 0 <= y + dy < height:
            if grid[y][x] <= grid[y + dy][x + dx] + 1:
                to_search.append((x + dx, y + dy, cost + 1))

print(costs[start_y][start_x])

minimum_length = float('inf')
for y, line in enumerate(grid):
    for x, height in enumerate(line):
        if height == 0 and costs[y][x] < minimum_length:
            minimum_length = costs[y][x]
print(minimum_length)