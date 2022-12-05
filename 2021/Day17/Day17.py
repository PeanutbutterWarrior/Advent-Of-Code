import re
from math import sqrt

with open("Day17.txt", "r") as file:
    data = file.read()

x1, x2, y1, y2 = re.fullmatch(r'target area: x=(\d+)\.\.(\d+), y=-(\d+)\.\.-(\d+)', data).groups()
x_left = int(x1)
x_right = int(x2)
y_bottom = -int(y1)
y_top = -int(y2)


# 0.5 * (max + 1) * max - y_top < 0.5 * (n + 1) * n
# 0.5 * (n + 1) * n <  0.5 * (max + 1) * max - y_bottom

y_options = []
for y_vel_max in range(-200, 200):
    y_vel = y_vel_max
    y_pos = 0
    while True:
        if y_pos < y_bottom:
            break
        elif y_pos <= y_top:
            y_options.append(y_vel_max)
            break
        y_pos += y_vel
        y_vel -= 1
    y_vel_max += 1

print(0.5 * (y_options[-1] - 1) * y_options[-1])

count = 0
for y_vel_max in y_options:
    for x_vel_max in range(1, 160):
        y_vel = y_vel_max
        x_vel = x_vel_max
        x_pos = 0
        y_pos = 0
        while True:
            if y_pos < y_bottom:
                break
            elif y_pos <= y_top and x_left <= x_pos <= x_right:
                count += 1
                break
            x_pos += x_vel
            y_pos += y_vel
            y_vel -= 1
            if x_vel > 0:
                x_vel -= 1
print(count)
