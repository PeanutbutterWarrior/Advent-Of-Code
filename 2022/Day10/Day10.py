with open("Day10.txt", "r") as file:
    data = file.read()

x = 1
cycle_count = 0

strength_total = 0
cycle_nums = {20, 60, 100, 140, 180, 220}

screen = [False] * (40 * 6)

for line in data.split('\n'):
    if not line:
        continue
    command, *val = line.split()
    if command == 'addx':
        cycle_count += 1
        if cycle_count in cycle_nums:
            strength_total += x * cycle_count
        if x - 1 <= cycle_count % 40 - 1 <= x + 1:
            screen[cycle_count] = True

        cycle_count += 1
        if cycle_count in cycle_nums:
            strength_total += x * cycle_count
        if x - 1 <= cycle_count % 40 - 1 <= x + 1:
            screen[cycle_count] = True
        x += int(val[0])
    elif command == 'noop':
        cycle_count += 1
        if cycle_count in cycle_nums:
            strength_total += x * cycle_count
        if x - 1 <= cycle_count % 40 - 1 <= x + 1:
            screen[cycle_count] = True

print(strength_total)
for line_num in range(0, len(screen), 40):
    print(''.join('#' if char else ' ' for char in screen[line_num:line_num + 40]))
