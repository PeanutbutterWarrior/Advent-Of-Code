with open("Day3.txt", "r") as file:
    data = file.read()


def score(char):
    if 97 <= (value := ord(char)) <= 122:
        return value - 96
    else:
        return value - 38


backpacks = []
for line in data.split():
    if not line:
        continue
    midpoint = len(line) // 2
    backpacks.append((set(line[:midpoint]), set(line[midpoint:])))


total = 0
for b1, b2 in backpacks:
    total += score((b1 & b2).pop())
print(total)

total = 0
for ind in range(0, len(backpacks), 3):
    b1, b2 = backpacks[ind]
    b3, b4 = backpacks[ind + 1]
    b5, b6 = backpacks[ind + 2]
    e1 = b1 | b2
    e2 = b3 | b4
    e3 = b5 | b6

    total += score((e1 & e2 & e3).pop())
print(total)
