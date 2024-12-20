import sys

with open(sys.argv[1], "r") as file:
    data = file.read().split("\n")


def search(data, offsets, aim):
    dx, dy = zip(*offsets)
    min_dx = min(dx)
    max_dx = max(dx)
    min_dy = min(dy)
    max_dy = max(dy)

    count = 0
    for y in range(-min_dy, len(data) - max_dy):
        for x in range(-min_dx, len(data[y]) - max_dx):
            for (dx, dy), target in zip(offsets, aim):
                if data[y + dy][x + dx] != target:
                    break
            else:
                count += 1
    return count

count = 0

dir_options = ((0, 0, 0, 0), (0, 1, 2, 3), (0, -1, -2, -3))
for x_opt in dir_options:
    for y_opt in dir_options:
        count += search(data, list(zip(x_opt, y_opt)), "XMAS")
print(count)

offsets = ((0, 0), (0, 2), (1, 1), (2, 0), (2, 2))
count = 0 
count += search(data, offsets, "MMASS")
count += search(data, offsets, "MSAMS")
count += search(data, offsets, "SMASM")
count += search(data, offsets, "SSAMM")
print(count)