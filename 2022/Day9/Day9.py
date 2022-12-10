with open("Day9.txt", "r") as file:
    data = file.read()


def follow(head, tail):
    dist = max(abs(head[0] - tail[0]), abs(head[1] - tail[1]))
    new_x = tail[0]
    new_y = tail[1]
    if dist == 1:
        if tail[0] < head[0] - 1:
            new_x = tail[0] + 1
        elif tail[0] > head[0] + 1:
            new_x = tail[0] - 1
        if tail[1] < head[1] - 1:
            new_y = tail[1] + 1
        elif tail[1] > head[1] + 1:
            new_y = tail[1] - 1
    elif dist >= 2:
        if tail[0] <= head[0] - 1:
            new_x = tail[0] + 1
        elif tail[0] >= head[0] + 1:
            new_x = tail[0] - 1
        if tail[1] <= head[1] - 1:
            new_y = tail[1] + 1
        elif tail[1] >= head[1] + 1:
            new_y = tail[1] - 1
    return new_x, new_y


head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
knots = [(0, 0) for _ in range(9)]


knot_first_visited = {(0, 0)}
knot_last_visited = {(0, 0)}
for line in data.split('\n'):
    if not line:
        continue
    direction, steps = line.split()
    for _ in range(int(steps)):
        if direction == 'U':
            head_y -= 1
        elif direction == 'D':
            head_y += 1
        elif direction == 'L':
            head_x -= 1
        elif direction == 'R':
            head_x += 1

        previous = (head_x, head_y)
        for ind, knot in enumerate(knots):
            previous = follow(previous, knot)
            knots[ind] = previous

        knot_first_visited.add(knots[0])
        knot_last_visited.add(knots[-1])

print(len(knot_first_visited))
print(len(knot_last_visited))