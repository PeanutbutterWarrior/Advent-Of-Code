import sys
from functools import cache

@cache
def num_way_possible(remaining):
    if len(remaining) == 0:
        return 1

    count = 0
    for towel in towels:
        if len(towel) > len(remaining):
            continue

        for di, stripe in enumerate(towel):
            if remaining[di] != stripe:
                break
        else:
            count += num_way_possible(remaining[len(towel):])

    return count

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

towels, data = data.split("\n\n")
towels = tuple(towels.split(", "))

total = 0
total_ways = 0
for t in data.split("\n"):
    count = num_way_possible(t)
    if count > 0:
        total += 1
    total_ways += count

print(total)
print(total_ways)
