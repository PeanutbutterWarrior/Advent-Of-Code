import sys
from itertools import product

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

def evolve(s):
    s = (s ^ (s << 6)) & 0xFFFFFF
    s = (s ^ (s >> 5)) & 0xFFFFFF
    s = (s ^ (s << 11)) & 0xFFFFFF
    return s


total = 0
changes = []
for line in data.split("\n"):
    e = {}
    changes.append(e)
    a, b, c, d = 100, 100, 100, 100
    i = int(line)
    for _ in range(2000):
        j = evolve(i)
        a, b, c, d = b, c, d, (j % 10) - (i % 10)
        i = j
        if (a, b, c, d) not in e:
            e[(a, b, c, d)] = i % 10
    total += i
print(total)

max_total = 0
checked = set()
ind = 0
for d in changes:
    for i in d.keys():
        if any(map(lambda k: k == 100, i)):
            continue
        if i in checked: continue
        checked.add(i)

        total = 0
        for change in changes:
            total += change.get(i, 0)
        if total > max_total:
            max_total = total
print(max_total)