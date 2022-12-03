from collections import defaultdict

with open("Day12.txt", "r") as file:
    data = file.read()

caves = defaultdict(set)
for line in data.split():
    if not line:
        continue
    a, b = line.split('-')
    caves[a].add(b)
    caves[b].add(a)


def explore(position, double_visited, *visited):
    if position == 'end':
        return 1
    count = 0
    for option in caves[position]:
        if option not in visited or option.isupper():
            count += explore(option, double_visited, *visited, position)
        elif not double_visited and option != 'start':
            count += explore(option, True, *visited, position)
    return count


print(explore('start', True))
print(explore('start', False))
