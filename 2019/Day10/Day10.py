import sys

def dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

data = data.split("\n")
width = len(data[0])
height = len(data)

asteroids = set()
for y in range(height):
    for x in range(width):
        if data[y][x] == "#":
            asteroids.add((x, y))

max_size = 0
final_bearings = None
for bx, by in asteroids:
    bearings = {}
    for x, y in asteroids:
        dx, dy = x - bx, y - by

        bearing = None
        if dx == 0:
            if dy < 0:
                bearing = (False, float("-inf"))
            elif dy  > 0:
                bearing = (True, float("-inf"))
            else:
                continue
        else:
            bearing = (dx <  0, dy / dx)
        
        previous_found = bearings.get(bearing, None)
        if previous_found is None or dist(bx, by, x, y) < dist(bx, by, previous_found[0], previous_found[1]):
            bearings[bearing] = (x, y)
    if len(bearings) > max_size:
        max_size = len(bearings)
        final_bearings = bearings
print(max_size)


_, final_target = sorted(final_bearings.items())[199]
print(final_target[0] * 100 + final_target[1])
