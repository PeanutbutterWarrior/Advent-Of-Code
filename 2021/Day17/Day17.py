import re

with open("Day17.txt", "r") as file:
    data = file.read()

x1, x2, y1, y2 = re.fullmatch(r'target area: x=(\d+)\.\.(\d+), y=-(\d+)\.\.-(\d+)', data).groups()
x_left = int(x1)
x_right = int(x2)
y_bottom = -int(y1)
y_top = -int(y2)

