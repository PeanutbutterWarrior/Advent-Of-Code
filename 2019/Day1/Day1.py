import sys

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

total1 = 0
total2 = 0
for line in  data.split("\n"):
    fuel = int(line) // 3 - 2
    total1 += fuel
    while fuel > 0:
        total2 += fuel
        fuel = fuel // 3 - 2
print(total1)
print(total2)