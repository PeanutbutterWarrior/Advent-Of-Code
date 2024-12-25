import sys
from heapq import *

width = height = 71
num_fall = 1023
inf = float("inf")
costs = [[inf] * width for _ in range(height)]
end = (width - 1, height - 1)

def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def astar(maze):
    for y in range(height):
        for x in range(width):
            costs[y][x] = inf    

    q = [(0, 0, (0, 0), None)]
    prev_pos = {}

    while q:
        _, cost, (x, y), prev = heappop(q)

        if costs[y][x] != inf:
            continue

        costs[y][x] = cost
        prev_pos[(x, y)] = prev

        if (x, y) == end:
            break

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= dx + x < width and \
            0 <= dy + y < height and \
            costs[y + dy][x + dx] == inf and \
            maze[y + dy][x + dx]:
                
                heappush(q, (cost + 1 + dist((x + dx, y + dy), end), cost + 1, (x + dx, y + dy), (x, y)))
    
    path = set()
    pos = end
    if pos not in prev_pos:
        return None, None
    while pos is not None:
        path.add(pos)
        pos = prev_pos[pos]

    return path, costs[end[1]][end[0]]

with open(sys.argv[1], "r") as file:
    data = file.read().strip().split("\n")


coords = []
for i in data:
    x, y = i.split(",")
    coords.append((int(x), int(y)))

grid = [[True] * width for _ in range(height)]
current_path, cost = astar(grid)
for ind, (x, y) in enumerate(coords):
    grid[y][x] = False
    
    if (x, y) in current_path:
        current_path, cost = astar(grid)

    if ind == num_fall:
        print(cost)

    if current_path == None:
        print(f"{x},{y}")
        break

