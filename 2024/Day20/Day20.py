import sys

with open(sys.argv[1], "r") as file:
    data = file.read().strip().split("\n")

def is_skip(x1, y1, x2, y2):
    if not (0 <= x1 < width and 0 <= x2 < width and 0 <= y1 < height and 0 <= y2 < height): return -1

    a, b = distance[y1][x1], distance[y2][x2]
    if a == -1 or b == -1: return -1

    return a - b - abs(x1 - x2) - abs(y1 - y2)

height = len(data)
width = len(data[0])

maze = [[True] * width for _ in range(height)]

start = end = None
for y in range(height):
    for x in range(width):
        match data[y][x]:
            case "S":
                start = (x, y)
            case "E":
                end = (x, y)
            case "#":
                maze[y][x] = False

distance = [[-1] * width for _ in range(height)]

x, y = end
dist = 0
while (x, y) != start:
    distance[y][x] = dist
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if maze[y + dy][x + dx] and distance[y + dy][x + dx] == -1:
            x += dx
            y += dy
            break
    dist += 1
distance[y][x] = dist

count = 0
for y in range(height):
    for x in range(width):
        save = is_skip(x, y, x + 2, y)
        if save >= 100:
            count += 1
        save = is_skip(x, y, x, y + 2)
        if save >= 100:
            count += 1
        save = is_skip(x, y, x, y - 2)
        if save >= 100:
            count += 1
        save = is_skip(x, y, x - 2, y)
        if save >= 100:
            count += 1
print(count)

count = 0
for y in range(height):
    for x in range(width):
        for dy in range(-20, 21):
            for dx in range(-20 + abs(dy), 21 - abs(dy)):
                save = is_skip(x, y, x + dx, y + dy)
                if save >= 100:
                    count += 1
print(count)