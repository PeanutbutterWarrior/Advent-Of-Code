import sys
from Intcode import Intcode
from Utilities import Dir
from collections import defaultdict

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

position = (0, 0)
dir = Dir.NORTH
hull = defaultdict(int)

interp = Intcode(Intcode.parse_input(data), [])
interp.run()

while interp.running:
    interp.give_input(hull[position])
    color, turn = interp.run()
    hull[position] = color

    if turn == 0:
        dir = dir.left
    else:
        dir = dir.right
    
    position += dir

print(len(hull))

position = (0, 0)
dir = Dir.NORTH
hull = defaultdict(int)
hull[position] = 1

interp = Intcode(Intcode.parse_input(data), [])
interp.run()

while interp.running:
    interp.give_input(hull[position])
    color, turn = interp.run()
    hull[position] = color

    if turn == 0:
        dir = dir.left
    else:
        dir = dir.right
    
    position += dir

minx, miny = float("inf"),float("inf")
maxx, maxy = float("-inf"), float("-inf")

for x, y in hull:
    minx = min(x, minx)
    maxx = max(x, maxx)
    miny = min(y, miny)
    maxy = max(y, maxy)

for y in range(miny, maxy + 1):
    for x in range(minx, maxx):
        if hull[(x, y)]:
            print("#", end="")
        else:
            print(" ", end="")
    print()