import sys

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

WIDTH = 25
HEIGHT = 6

min_num_0 = float("inf")
min_val = None

for i in range(0, len(data), WIDTH * HEIGHT):
    seq = data[i:i + WIDTH * HEIGHT]
    if (count := seq.count("0")) < min_num_0:
        min_val = seq.count("1") * seq.count("2")
        min_num_0 = count
print(min_val)

image = [["2" for _ in range(WIDTH)] for _ in range(HEIGHT)]

for layer_start in range(0, len(data), WIDTH * HEIGHT):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if image[y][x] == "2":
                image[y][x] = data[layer_start + y * WIDTH + x]

for line in image:
    print("".join(line).replace("0", " ").replace("1", "#"))