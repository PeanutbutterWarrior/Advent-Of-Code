import sys
from enum import Enum

from Intcode import Intcode

class Tile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

colors = {
    Tile.EMPTY: (0, 0, 0),
    Tile.WALL: (255, 255, 255),
    Tile.BLOCK: (255, 0 , 0),
    Tile.PADDLE: (0, 255,  0),
    Tile.BALL: (0, 0, 255),
}

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

prog = Intcode.parse_input(data)
interp = Intcode(prog.copy())
output = interp.run()

tiles = {}
for i in range(0, len(output), 3):
    x, y, tile = output[i:i + 3]
    tiles[(x, y)] = Tile(tile)

total = 0
for k, v in tiles.items():
    if v == Tile.BLOCK:
        total += 1
print(total)

prog[0] = 2 
interp = Intcode(prog.copy())

output = interp.run()
paddle_x, ball_x = 0, 0
score = 0

blocks = set()

while interp.running:
    for i in range(0, len(output), 3):
        x, y, val = output[i:i+3]
        if x == -1 and y == 0:
            score = val
            continue

        tile = Tile(val)
        if tile is Tile.BALL:
            ball_x = x
        elif tile is Tile.PADDLE:
            paddle_x = x
        elif tile is Tile.BLOCK:
            blocks.add((x, y))
        elif tile is Tile.EMPTY and (x, y) in blocks:
            blocks.remove((x, y))

    button = 0
    if paddle_x < ball_x:
        button = 1
    elif paddle_x > ball_x:
        button = -1
    interp.give_input(button)

    output = interp.run()
    
    if len(blocks) == 0:
        break
print(score)