import sys

with open(sys.argv[1], "r") as file:
    data = iter(file.read().strip().split("\n"))

def move(instr, x, y):
    direction, distance = instr[0], int(instr[1:])
    match direction:
        case "U":
            nx, ny = x, y - distance
        case "D":
            nx, ny = x, y + distance
        case "L":
            nx, ny = x - distance, y
        case "R":
            nx, ny = x + distance, y
    return nx, ny, distance

def get_intersection(horizontal_line, vertical_line):
    (ax, ay), (bx, by), d1 = horizontal_line
    (cx, cy), (dx, dy), d2 = vertical_line

    if min(cy, dy) <= ay <= max(cy, dy) and min(ax, bx) <= cx <= max(ax, bx):
        return (cx, ay), d1 + abs(ax - cx) + d2 + abs(ay - dy)
    return None



vertical_lines = []
horizontal_lines = []

x, y = 0, 0
d = 0
for instr in next(data).split(","):
    nx, ny, dist = move(instr, x, y)

    if x == nx:
        vertical_lines.append(((x, y), (nx, ny), d))
    else:
        horizontal_lines.append(((x, y), (nx, ny), d))
    
    x, y = nx, ny
    d += dist

intersections = []

x, y = 0, 0
d = 0
for instr in next(data).split(","):
    nx, ny, dist = move(instr, x, y)

    if x == nx:
        for line in horizontal_lines:
             if (inter := get_intersection(((x, min(y, ny)), (x, max(y, ny)), d), line)) is not None:
                intersections.append(inter)
    else:
        for line in vertical_lines:
            if (inter := get_intersection(((min(x, nx), y), (max(x, nx), y), d), line)) is not None:
                intersections.append(inter)
        
    x, y = nx, ny
    d += dist

print(min(map(lambda i: abs(i[0][0]) + abs(i[0][1]), intersections)))
print(min(map(lambda i: i[1], intersections)))