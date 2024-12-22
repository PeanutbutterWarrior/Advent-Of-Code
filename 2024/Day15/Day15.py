import sys
from enum import Enum, auto

class Tile(Enum):
    WALL = auto()
    BOX = auto()
    ROBOT = auto()
    EMPTY = auto()

def get_at(position, map):
    return map[int(position.imag)][int(position.real)]

def set_at(position, x, map):
    map[int(position.imag)][int(position.real)] = x

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

m, inp = data.split("\n\n")

map = []
robot_pos = None
for y, line in enumerate(m.split("\n")):
    map.append([])
    for x, item in enumerate(line):
        match (item):
            case ".":
                map[-1].append(Tile.EMPTY)
            case "#":
                map[-1].append(Tile.WALL)
            case "@":
                map[-1].append(Tile.ROBOT)
                robot_pos = x + y * 1j
            case "O":
                map[-1].append(Tile.BOX)

dirs = {"<": -1, "v": 1j, ">": 1, "^":-1j}

for instr in inp:
    if instr == "\n": continue
    dir = dirs[instr]
    i = 1
    seen_box = False
    moved = False
    while True:
        front = get_at(robot_pos + i * dir, map)
        match (front):
            case Tile.EMPTY:
                set_at(robot_pos + i * dir, Tile.BOX if seen_box else Tile.ROBOT, map)
                moved = True
                break
            case Tile.WALL:
                break
            case Tile.BOX:
                seen_box = True
            case Tile.ROBOT:
                print("Robot hit robot?")
                exit()
        i += 1
    if moved:
        set_at(robot_pos, Tile.EMPTY, map)
        robot_pos += dir
        set_at(robot_pos, Tile.ROBOT, map)

total = 0
for y, row in enumerate(map):
    for x, item in enumerate(row):
        if item == Tile.BOX:
            total += 100 * y + x
print(total)

import Day15p2