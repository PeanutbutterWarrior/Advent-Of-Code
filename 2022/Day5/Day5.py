import re
from copy import deepcopy

with open("Day5.txt", "r") as file:
    data = file.read()

boxes, instructions = data.split('\n\n')

grid = []
*boxes, _ = boxes.split('\n')
for line in boxes:
    grid.append([])
    for match in re.findall('(   |\[.]) ?', line):
        if match == '   ':
            grid[-1].append(None)
        else:
            grid[-1].append(match[1])

stacks = [[] for _ in range(len(grid[0]))]
for i in range(len(grid[0])):
    for j in range(len(grid) - 1, -1, -1):
        if grid[j][i] is None:
            break
        stacks[i].append(grid[j][i])

stacks1 = stacks
stacks2 = deepcopy(stacks)

for line in instructions.split('\n'):
    if not line:
        continue
    num, start, end = map(int, re.fullmatch('move (\d+) from (\d+) to (\d+)', line).groups())

    for _ in range(num):
        stacks1[end - 1].append(stacks1[start - 1].pop(-1))

    left, taken = stacks2[start-1][:-num], stacks2[start-1][-num:]
    stacks2[end - 1].extend(taken)
    stacks2[start - 1] = left

print(''.join(i[-1] for i in stacks1))
print(''.join(i[-1] for i in stacks2))