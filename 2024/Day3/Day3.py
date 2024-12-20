import sys
import re

with open(sys.argv[1], "r") as file:
    data = file.read()

muls = re.findall("mul\((\d+),(\d+)\)", data)
total = 0
for a,b in muls:
    total += int(a) * int(b)

print(total)

ops = re.findall("(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", data)
total = 0
enabled = True
for op, a, b in ops:
    if op == "do()":
        enabled = True
    elif op == "don't()":
        enabled = False
    elif enabled:
        total += int(a) * int(b)
print(total)