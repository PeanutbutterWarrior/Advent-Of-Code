import sys

with open(sys.argv[1], "r") as file:
    map = file.read().strip().split("\n")

map = [[ord(x) for x in line] for line in map]

width = len(map[0])
height = len(map)

counted = [[False] * width for _ in range(height)]

total1 = 0
total2 = 0
for i in range(height):
    for j in range(width):
        if counted[i][j]: continue
        counted[i][j] = True

        q = [(j, i)]
        char = map[i][j]
        area = 1
        perimeter = 0
        corners = 0
        while len(q) > 0:
            x, y = q.pop(-1)

            sides = []

            for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)): # NESW
                inside_map = 0 <= x + dx < width and 0 <= y + dy < height
                if not inside_map or map[y + dy][x + dx] != char:
                    perimeter += 1
                elif not counted[y + dy][x + dx]:
                    counted[y + dy][x + dx] = True
                    q.append((x + dx, y + dy))
                    area += 1
                
                sides.append(inside_map and map[y + dy][x + dx] == char)
            
            match sides.count(True):
                case 0:
                    corners += 4
                case 1:
                    corners += 2
                case 2:
                    if not((sides[0] and sides[2]) or (sides[1] and sides[3])):
                        corners += 1
            
            corners_inside = []
            for dx, dy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
                inside_map = 0 <= x + dx < width and 0 <= y + dy < height
                corners_inside.append(not inside_map or map[y + dy][x + dx] == char)
            if not corners_inside[0] and sides[0] and sides[3]:
                corners += 1
            if not corners_inside[1] and sides[0] and sides[1]:
                corners += 1
            if not corners_inside[2] and sides[1] and sides[2]:
                corners += 1
            if not corners_inside[3] and sides[2] and sides[3]:
                corners += 1

        total1 += area * perimeter
        total2 += area * corners
print(total1)
print(total2)