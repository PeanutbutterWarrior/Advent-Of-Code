import sys

def simulate_walk(guard, obstacles, bonus_obstacle = None):
    direction = 0 - 1j
    positions = set()
    posdirs = set()
    while 0 <= guard.real < width and 0 <= guard.imag < height:
        if (guard, direction) in posdirs:
            return None
        posdirs.add((guard, direction))
        positions.add(guard)
        new_pos = guard + direction
        while new_pos in obstacles or new_pos == bonus_obstacle:
            direction *= 1j
            new_pos = guard + direction
        guard = new_pos
    return positions

with open(sys.argv[1], "r") as file:
    data = file.read().strip().split("\n")

height = len(data)
width = len(data[0])

obstacles = set()
guard = None
for x in range(width):
    for y in range(height):
        if data[y][x] == "#":
            obstacles.add(x + y * 1j)
        elif data[y][x] == "^":
            guard = x + y * 1j

positions = simulate_walk(guard, obstacles)
print(len(positions))

count = 0
for x in range(width):
    for y in range(height):
        new_obj = x + 1j * y
        if simulate_walk(guard, obstacles, new_obj) is None:
            count += 1
print(count)
