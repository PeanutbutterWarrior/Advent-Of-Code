with open('Day12.txt', 'r') as file:
    data = file.read().split()

x = 0
y = 0
direction = 0

for command in data:
    action = command[0]
    arg = int(command[1:])
    if action == 'F':
        if direction == 0:
            action = 'E'
        elif direction == 1:
            action = 'S'
        elif direction == 2:
            action = 'W'
        elif direction == 3:
            action = 'N'

    if action == 'N':
        y += arg
    elif action == 'S':
        y -= arg
    elif action == 'W':
        x -= arg
    elif action == 'E':
        x += arg
    elif action == 'L':
        direction = (direction - arg // 90) % 4
    elif action == 'R':
        direction = (direction + arg // 90) % 4

print(abs(x) + abs(y))
