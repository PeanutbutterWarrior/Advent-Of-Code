with open('Day12.txt', 'r') as file:
    data = file.read().split()


# Part 1

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

# Part 2

x = 10
y = 1
ax = 0
ay = 0

for command in data:
    action = command[0]
    arg = int(command[1:])
    if action == 'N':
        y += arg
    elif action == 'S':
        y -= arg
    elif action == 'W':
        x -= arg
    elif action == 'E':
        x += arg
    elif action == 'L':
        for i in range(arg//90):
            x, y = -y, x
    elif action == 'R':
        for i in range(arg//90):
            x, y = y, -x
    elif action == 'F':
        ax += x * arg
        ay += y * arg

print(abs(ax) + abs(ay))
