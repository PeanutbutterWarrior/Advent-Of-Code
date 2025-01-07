import sys
from Utilities import MazeBuilder, Dir
from copy import deepcopy
from collections import deque
from pprint import pprint

with open(sys.argv[1], "r") as file:
    data = file.read().strip("\n")

map = MazeBuilder()
new_map = MazeBuilder()

for line in data.split("\n"):
    map.new_line()
    new_map.new_line()

    for char in line:
        if char == "#":
            map.add_value(True)
        else:
            map.add_value(False)
        new_map.add_value(False)

map = map.finish()
new_map = new_map.finish()
original_map = deepcopy(map)
blank_map = deepcopy(new_map)

seen_maps = set()
while True:
    map_hash = 0
    for y in range(map.height - 1, -1, -1):
        for x in range(map.width-1, -1, -1):
            count = 0
            for dir in Dir:
                if map[(x, y) + dir]:
                    count += 1
            
            is_alive = (map[x, y] and count == 1) or (not map[x, y] and (count == 1 or count == 2))
            new_map[x, y] = is_alive
            map_hash <<= 1
            map_hash |= is_alive

    map, new_map = new_map, map
    if map_hash in seen_maps:
        print(map_hash)
        break
    seen_maps.add(map_hash)

neighbours = {}
for x in range(5):
    for y in range(5):
        if x == y == 2:
            continue
        neighbours[x, y] = set()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1,0)):
            nx, ny = x + dx, y + dy
            if nx == ny == 2:
                continue
            if 0 <= nx < 5 and 0 <= ny < 5:
                neighbours[x, y].add((nx, ny, 0))

for x in range(5):
    neighbours[x, 0].add((2, 1, -1))
    neighbours[x, 4].add((2, 3, -1))
    neighbours[0, x].add((1, 2, -1))
    neighbours[4, x].add((3, 2, -1))
    
    neighbours[2, 1].add((x, 0, 1))
    neighbours[2, 3].add((x, 4, 1))
    neighbours[1, 2].add((0, x, 1))
    neighbours[3, 2].add((4, x, 1))

grids = [deepcopy(blank_map), original_map, deepcopy(blank_map)]
spare_grids = [deepcopy(blank_map), deepcopy(blank_map), deepcopy(blank_map)]

for _ in range(200):
    first_changed = False
    last_changed = False
    for z in range(len(grids)):
        changed = False

        for x in range(5):
            for y in range(5):
                if x == y == 2:
                    continue
                count = 0
                for nx, ny, dz in neighbours[x, y]:
                    nz = z + dz

                    if nz < 0 or nz >= len(grids):
                        continue
                    if grids[nz][nx, ny]:
                        count += 1
                current_state = grids[z][x, y]
                is_alive = (current_state and count == 1) or (not current_state and (count == 1 or count == 2))
                if is_alive != current_state:
                    changed = True
                spare_grids[z][x, y] = is_alive
        
        if changed:
            if z == 0:
                first_changed = True
            elif z == len(grids) - 1:
                last_changed = True
    
    if first_changed:
        spare_grids.insert(0, deepcopy(blank_map))
        grids.insert(0, deepcopy(blank_map))
    if last_changed:
        spare_grids.append(deepcopy(blank_map))
        grids.append(deepcopy(blank_map))
    
    grids, spare_grids = spare_grids, grids

total = 0
for grid in grids:
    for x in range(5):
        for y in range(5):
            if grid[x, y]:
                total += 1
print(total)