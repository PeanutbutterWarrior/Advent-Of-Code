import sys
from heapq import *
from enum import Enum

class Dir(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def right(self):
        return Dir((self.value + 1) % 4)
    
    def left(self):
        return Dir((self.value - 1 % 4))
    
    def behind(self):
        return Dir((self.value + 2) % 4)
    
    def cost(self, other):
        dist = abs(other.value - self.value)
        if dist == 3: dist = 1
        return dist * 1000
    
    def dxy(self):
        match self:
            case Dir.NORTH:
                return (0, -1)
            case Dir.EAST:
                return (1, 0)
            case Dir.SOUTH:
                return (0, 1)
            case Dir.WEST:
                return (-1, 0)
    
    def __add__(self, other):
        if type(other) == tuple and len(other) == 2:
            dx, dy = self.dxy()
            return (other[0] + dx, other[1] + dy)
        raise NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)


with open(sys.argv[1], "r") as file:
    data = file.read().strip()

start = None
end=None
maze = []
for y, line in enumerate(data.split("\n")):
    maze.append([])
    for x, char in enumerate(line):
        if char == "#":
            maze[-1].append(False)
        else:
            if char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)
            maze[-1].append(True)

width = len(maze[0])
height = len(maze)

costs = [[float("inf") for _ in range(width)] for _ in range(height)]
costs[start[1]][start[0]] = 0

# cost, (x,y), direction
unvisited = [(0, start, Dir.EAST)]
heapify(unvisited)

while True:
    cost, pos, dir = heappop(unvisited)
    if pos == end:
        print(cost)
        break
    cost = costs[pos[1]][pos[0]]
    for new_dir in Dir:
        x, y = pos + new_dir
        if 0 <= x < width and 0 < y < height and maze[y][x] and costs[y][x] == float("inf"):
            new_cost = cost + 1 + dir.cost(new_dir)
            if new_cost < costs[y][x]:
                costs[y][x] = new_cost
            heappush(unvisited, (new_cost, (x, y), new_dir))