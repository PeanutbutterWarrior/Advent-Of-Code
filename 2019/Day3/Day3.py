import sys

with open(sys.argv[1], "r") as file:
    data = file.read().strip("\n")

def gen_wire(path):
    x, y = 0, 0
    wire = {}
    d = 0
    for instr in path.split(","):
        dir, num = instr[0], int(instr[1:])
        if dir == "L":
            for _ in range(num):
                x -= 1
                d += 1
                wire[x, y] = d
        elif dir == "R":
            for _ in range(num):
                x += 1
                d += 1
                wire[x, y] = d
        elif dir == "U":
            for _ in range(num):
                y -= 1
                d += 1
                wire[x, y] = d
        elif dir == "D":
            for _ in range(num):
                y += 1
                d += 1
                wire[x, y] = d
    return wire

path1, path2 = data.split("\n")
wire1 = gen_wire(path1)
wire2 = gen_wire(path2)
intersections = set(wire1) & set(wire2)
print(min(map(lambda a: abs(a[0]) + abs(a[1]), intersections)))
print(min(map(lambda a: wire1[a] + wire2[a], intersections)))