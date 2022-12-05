import re
with open("Day5.txt", "r") as file:
    data = file.read()

boxes, instructions = data.split('\n\n')

grid = []
*boxes, _ = boxes.split('\n')
for line in boxes:
    grid.append([])
    for match in re.findall('(   |\[.]) ?', line):
        print(match)
        if match == '   ':
            grid[-1].append(None)
        else:
            grid[-1].append(match[1])

stacks = []
for
