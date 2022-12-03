from heapq import *

with open("Day15.txt", "r") as file:
    data = file.read()

maze = []
for line in data.split():
    if line:
        width = len(line)
        line = [int(i) for i in line]
        for _ in range(4 * width):
            cost = line[-width] + 1
            if cost == 10:
                cost = 1
            line.append(cost)
        maze.append(line)

width = len(maze[0])
height = len(maze)
for _ in range(4 * height):
    new_line = []
    for c in maze[-height]:
        cost = c + 1
        if cost == 10:
            cost = 1
        new_line.append(cost)
    maze.append(new_line)

height = len(maze)

costs = [[float('inf') for _ in range(width)] for _ in range(height)]

to_check = [(0, 0, 0)]
heapify(to_check)
min_risk = float('inf')
while True:
    cost, x, y = heappop(to_check)
    if cost > min_risk:
        break
    if x == width - 1 and y == height - 1:
        min_risk = cost
        continue
    if cost >= costs[y][x]:
        continue
    costs[y][x] = cost
    if x < width - 1:
        heappush(to_check, (cost + maze[y][x + 1], x + 1, y))
    if x > 0:
        heappush(to_check, (cost + maze[y][x - 1], x - 1, y))
    if y < height - 1:
        heappush(to_check, (cost + maze[y + 1][x], x, y + 1))
    if y > 0:
        heappush(to_check, (cost + maze[y - 1][x], x, y - 1))
print(min_risk)
