import re

with open('Day14.txt', 'r') as file:
    data = file.read().split('\n')


def apply_mask(val):
    return (val & ~mask) | forced


mask = 0
forced = 0

memory = {}
memory_pattern = re.compile('mem\[(\d+)\] = (\d+)')
mask_pattern = re.compile('mask = ([X10]+)')

for line in data:
    if line[1] == 'e':
        match = re.match(memory_pattern, line)
        memory[int(match[1])] = apply_mask(int(match[2]))
    else:
        match = re.match(mask_pattern, line)
        mask = int(''.join('0' if i == 'X' else '1' for i in match[1]), 2)
        forced = int(''.join('1' if i == '1' else '0' for i in match[1]), 2)

print(sum(memory.values()))
