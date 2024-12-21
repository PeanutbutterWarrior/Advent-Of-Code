import sys
import math
from functools import cache

def intlen(x):
    return math.floor(math.log10(x) + 1)

with open(sys.argv[1], "r") as file:
    data = list(map(int, file.read().strip().split(" ")))

@cache
def solve_evolution(num, lifetime):
    if lifetime == 0:
        return 1

    if num == 0:
        return solve_evolution(1, lifetime - 1)
    elif (length := intlen(num)) % 2 == 0:
        offset = 10**(length//2)
        return solve_evolution(num % offset, lifetime - 1) + solve_evolution(num // offset, lifetime - 1)
    else:
        return solve_evolution(num * 2024, lifetime - 1)

total = 0
for i in data:
    total += solve_evolution(i, 25)
print(total)

total = 0
for i in data:
    total += solve_evolution(i, 75)
print(total)