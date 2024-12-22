import sys

with open(sys.argv[1], "r") as file:
    map = file.read().strip().split("\n")

map = [[ord(x) for x in line] for line in map]

width = len(map[0])
height = len(map)

counted = [[False] * width for _ in range(height)]

total = 0
for i in range(height):
    for j in range(width):
        if counted[i][j]: continue
        counted[i][j] = True

        q = [(j, i)]
        char = map[i][j]
        area = 1
        perimeter = 0
        while len(q) > 0:
            x, y = q.pop(-1)

            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if not(0 <= x + dx < width and 0 <= y + dy < height) or map[y + dy][x + dx] != char:
                    perimeter += 1
                elif not counted[y + dy][x + dx]:
                    counted[y + dy][x + dx] = True
                    q.append((x + dx, y + dy))
                    area += 1
        total += area * perimeter
print(total)

file=  open("out.txt", "w+")
for y, line in enumerate(counted):
    for x, item in enumerate(line):
        if item:
            print(chr(map[y][x]).lower(), end="", file=file)
        else:
            print(chr(map[y][x]).upper(), end="", file=file)
    print("", file=file)
file.close()