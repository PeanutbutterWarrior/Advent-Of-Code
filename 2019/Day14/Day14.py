import sys
import re
from collections import defaultdict
from math import ceil

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

reaction_regex = re.compile("(\\d+) ([A-Z]+)")

reactions = {}
for line in data.split("\n"):
    items = reaction_regex.findall(line)
    *inputs, output = items
    n, output = output
    ingredients = tuple((int(i), j) for i, j in inputs)
    reactions[output] = (int(n), ingredients)

TRILLION = 1_000_000_000_000

def ore_cost(num_fuel):
    wants = defaultdict(int)
    wants["FUEL"] = num_fuel

    has = defaultdict(int)

    ore = 0

    while len(wants) > 0:
        item, num = wants.popitem()
        if num <= has[item]:
            has[item] -= num
            continue
        else:
            num -= has[item]
            has[item] = 0

        out_num, inputs = reactions[item]

        repeats = ceil(num / out_num)
        has[item] += repeats * out_num - num
        for n, inp in inputs:
            if inp == "ORE":
                ore += n * repeats
            else:
                wants[inp] += n * repeats
    return ore

one_fuel_cost = ore_cost(1)
print(ore_cost(1))

for _ in range(10):
    new_cost = ore_cost(int(TRILLION / one_fuel_cost))
    new_cost = new_cost / int(TRILLION / one_fuel_cost)
    if new_cost == one_fuel_cost:
        break
    one_fuel_cost = new_cost
print(int(TRILLION / one_fuel_cost))
