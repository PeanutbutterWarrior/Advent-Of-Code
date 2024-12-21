import sys
from collections import Counter

with open(sys.argv[1], "r") as file:
    data = file.read().strip().split("\n")

map = [[int(i) for i in line] for line in data]
width = len(map[0])
height = len(map)

def walk(x, y):
    value = map[y][x]
    if value == 9: return Counter({(x, y): 1})

    heads = Counter()
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= x +dx < width and 0 <= y + dy < height and map[y + dy][x + dx] == value + 1:
            heads += walk(x + dx, y + dy)

    return heads

total1 = 0
total2 = 0
for y in range(height):
    for x in range(width):
        if map[y][x] == 0:
            n = walk(x, y)
            total1 += len(n)
            total2 += sum(n.values())
print(total1)
print(total2)