import sys
import re
from dataclasses import dataclass
from collections import Counter
from PIL import Image

width = 101
height = 103

@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int

    def position_after(self, time: int):
        return (self.x + self.dx * time) % width, (self.y + self.dy * time) % height

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

robots = []
pattern = re.compile("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
for line in data.split("\n"):
    x, y, dx, dy = map(int, pattern.match(line).group(1, 2, 3, 4))
    robots.append(Robot(x, y, dx, dy))

quadrants = [0, 0, 0, 0]
for robot in robots:
    x, y = robot.position_after(100)
    if x == width // 2 or y == height // 2: continue
    quadrant = (x < width // 2) + (y < height // 2) * 2

    quadrants[quadrant] += 1

total = 1
for i in quadrants:
    total *= i
print(total)

img = Image.new("L", (width, height), 255)
pix = img.load()
for robot in robots:
    x, y = robot.position_after(8053)
    pix[x, y] = 0
img.save("out.png")
print(8053)