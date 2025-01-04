import sys
from Intcode import Intcode
from Utilities import Dir
from enum import Enum
from heapq import *

SCALE = 10
XOFFSET = 25
YOFFSET = 25

class Tile(Enum):
    UNKNOWN = -1
    WALL = 0
    PATH = 1
    TARGET = 2
    START = 3

    def walkable(self):
        match self:
            case Tile.PATH | Tile.TARGET | Tile.START:
                return True
            case _:
                return False

colors = {Tile.UNKNOWN: (100, 100, 100), Tile.WALL: (0, 0, 0), Tile.PATH: (255, 255, 255), Tile.TARGET: (0, 255, 0), Tile.START: (255, 0, 0)}

class Maze:
    def __init__(self):
        self.maze = {(0, 0): Tile.PATH}

    def __getitem__(self, key):
        return self.maze.get(key, Tile.UNKNOWN)
    
    def __setitem__(self, key, value):
        self.maze[key] = value

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

dirs = {Dir.NORTH: 1, Dir.SOUTH:2, Dir.WEST: 3, Dir.EAST: 4}

interp = Intcode(Intcode.parse_input(data))


direction = Dir.EAST
at_o2 = False
position = (0, 0)
maze = Maze()
end_position = None

while not at_o2:
    for dir in (direction.left, direction, direction.right, direction.behind):
        interp.give_input(dirs[dir])
        out = interp.run()[0]
        maze[position + dir] = Tile(out)
        match out:
            case 1:
                direction = dir
                position += dir
                break
            case 2:
                position += dir
                end_position = position
                break
    
    if position == (0, 0):
        break

costs = {}
q = [(0, end_position)]

while q:
    cost, position = heappop(q)
    if costs.get(position, None) is not None:
        continue

    costs[position] = cost

    for dir in Dir:
        new_position = position + dir
        if maze[new_position].walkable():
            heappush(q, (cost + 1, new_position))
print(costs[(0, 0)])
print(max(costs.values()))