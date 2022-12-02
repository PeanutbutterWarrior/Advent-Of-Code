from PIL import Image
import os

with open("Day5.txt", "r") as file:
    data = file.read()

lines = []
for line in data.split('\n'):
    if not line:
        continue
    start, end = line.split(' -> ')
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    lines.append(((int(x1), int(y1)), (int(x2), int(y2))))

grid = [[0] * 1000 for _ in range(1000)]
for (x1, y1), (x2, y2) in lines:
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] += 1

count = 0
for row in grid:
    for item in row:
        if item > 1:
            count += 1
print(count)

for (x1, y1), (x2, y2) in lines:
    if abs(x1 - x2) == abs(y1 - y2):
        mx = min(x1, x2)
        my = min(y1, y2)
        for diff in range(abs(x1 - x2) + 1):
            if x1 == mx:
                x = x1 + diff
            else:
                x = x1 - diff
            if y1 == my:
                y = y1 + diff
            else:
                y = y1 - diff
            grid[y][x] += 1

count = 0
for row in grid:
    for item in row:
        if item > 1:
            count += 1
print(count)

img = Image.new('RGB', (1000, 1000))
pix = img.load()
for x in range(1000):
    for y in range(1000):
        pix[x, y] = (grid[y][x] * 63, 0, 0)
img.save("out.png")