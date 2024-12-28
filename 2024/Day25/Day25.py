import sys

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

keys = []
locks = []

for mechanism in data.split("\n\n"):
    lines = iter(mechanism.split("\n"))
    if next(lines) == ".....":
        is_lock = False
    else:
        is_lock = True
    
    mech = [0, 0, 0, 0, 0]
    for _ in range(5):
        for ind, char in enumerate(next(lines)):
            if char == "#":
                mech[ind] += 1
    
    if is_lock:
        locks.append(mech)
    else:
        keys.append(mech)

total = 0
for key in keys:
    for lock in locks:
        for i in range(5):
            if key[i] + lock[i] > 5:
                break
        else:
            total += 1
print(total)