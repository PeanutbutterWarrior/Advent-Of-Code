import sys
from itertools import cycle, repeat, chain

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

vals = list(map(int, data))
new_vals = [0] * len(vals)

for j in range(100):
    for i in range(len(vals)):
        total = 0
        iterator = cycle(chain(repeat(0, i +1), repeat(1, i +1), repeat(0, i + 1), repeat(-1, i + 1)))
        next(iterator)
        for a, b in zip(vals, iterator):
            total += a * b
        
        if total < 0:
            new_vals[i] = (10 - total % 10) % 10
        else:
            new_vals[i] = total % 10
    
    vals, new_vals = new_vals, vals
print("".join(map(str, vals[:8])))