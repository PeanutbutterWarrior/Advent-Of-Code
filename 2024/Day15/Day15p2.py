import sys
from enum import Enum, auto

class Tile(Enum):
    WALL = auto()
    BOX = auto()
    ROBOT = auto()
    EMPTY = auto()

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, value):
        if type(value) == Robot: return True
        return value == Tile.ROBOT

    def __str__(self):
        return "@"

    def can_move(self, dx, dy):
        in_way = map[self.y + dy][self.x + dx]
        match (in_way):
            case Tile.WALL:
                return False
            case Tile.EMPTY:
                return True
            case Tile.ROBOT:
                raise ValueError("Trying to move into robot")
            case Tile.BOX:
                return in_way.can_move(dx, dy)
    
    def move(self, dx, dy):
        in_way = map[self.y + dy][self.x + dx]
        match (in_way):
            case Tile.WALL:
                raise ValueError("Moving into wall")
            case Tile.ROBOT:
                raise ValueError("Trying to push robot")
            case Tile.BOX:
                in_way.move(dx, dy)
        
        map[self.y][self.x] = Tile.EMPTY
        self.x += dx
        self.y += dy
        map[self.y][self.x] = self


class Box:
    def __init__(self, x, y, other=None):
        self.x = x
        self.y = y
        if other is None:
            self.left = True
            self.other = Box(x + 1, y, self)
        else:
            self.left = False
            self.other = other
        self.valued = False
    
    def __eq__(self, value):
        if type(value) == Box:
            return value is self or value is self.other
        return value == Tile.BOX

    def __str__(self):
        return "[" if self.left else "]"

    @property
    def right(self):
        return not self.left

    def can_move(self, dx, dy, other_checked=False):
        if not other_checked and not self.other.can_move(dx, dy, True):
            return False
        
        in_way = map[self.y + dy][self.x + dx]
        match (in_way):
            case Tile.WALL:
                return False
            case Tile.EMPTY:
                return True
            case Tile.ROBOT:
                raise ValueError("Trying to move into robot")
            case Tile.BOX:
                if in_way == self.other:
                    return True
                return in_way.can_move(dx, dy)
    
    def move(self, dx, dy, other_moved=False):
        me_first = (dx < 0 and self.left) or (dx > 1 and self.right)
        if not other_moved and not me_first:
            self.other.move(dx, dy, True)
        
        in_way = map[self.y + dy][self.x + dx]
        match (in_way):
            case Tile.WALL:
                raise ValueError("Moving into wall")
            case Tile.ROBOT:
                raise ValueError("Trying to push robot")
            case Tile.BOX:
                in_way.move(dx, dy)
        
        map[self.y][self.x] = Tile.EMPTY
        self.y += dy
        self.x += dx
        map[self.y][self.x] = self

        if not other_moved and me_first:
            self.other.move(dx, dy, True)
    
    def get_value(self):
        try:
            if not self.valued:
                if self.left:
                    return self.x + self.y * 100
                else:
                    return self.other.get_value()
            return 0
        finally:
            self.valued = True
            self.other.valued = True
            

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

m, inp = data.split("\n\n")

map = []
robot = None
for y, line in enumerate(m.split("\n")):
    map.append([])
    for x, item in enumerate(line):
        match (item):
            case ".":
                map[-1].append(Tile.EMPTY)
                map[-1].append(Tile.EMPTY)
            case "#":
                map[-1].append(Tile.WALL)
                map[-1].append(Tile.WALL)
            case "@":
                robot = Robot(x *2, y)
                map[-1].append(robot)
                map[-1].append(Tile.EMPTY)
            case "O":
                box = Box(x * 2, y)
                map[-1].append(box)
                map[-1].append(box.other)

dirs = {"<": (-1, 0), "v": (0, 1), ">": (1, 0), "^":(0, -1)}

for instr in inp:
    if instr == "\n": continue
    dx, dy = dirs[instr]
    i = 1
    if robot.can_move(dx, dy):
        robot.move(dx, dy)

total = 0
for y, row in enumerate(map):
    for x, item in enumerate(row):
        if item == Tile.BOX:
            total += item.get_value()
print(total)