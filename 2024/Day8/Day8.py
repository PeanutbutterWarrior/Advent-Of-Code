import sys
from collections import defaultdict
from itertools import combinations

with open(sys.argv[1], "r") as file:
    data = file.read().strip().split("\n")

height = len(data)
width = len(data[0])

def inbounds(x: complex):
    return 0 <= x.real < width and 0 <= x.imag < height

antennas = defaultdict(list)
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != ".":
            antennas[char].append(x + y * 1j)

nodes: set[complex] = set()

for char, items in antennas.items():
    for a, b in combinations(items, 2):
        d = a - b
        nodes.add(a + d)
        nodes.add(b - d)

total = 0
for node in nodes:
    if inbounds(node):
        total += 1

print(total)

nodes.clear()
for char, items in antennas.items():
    for a, b in combinations(items, 2):
        d = a - b
        while inbounds(a):
            nodes.add(a)
            a += d
        while inbounds(b):
            nodes.add(b)
            b -= d

print(len(nodes))