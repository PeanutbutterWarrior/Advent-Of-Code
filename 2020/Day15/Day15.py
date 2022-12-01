with open('Day15.txt', 'r') as file:
    times = list(map(int, file.read().split(',')))

# Part 1

last_time_said = {val: (None, ind) for ind, val in enumerate(times)}
number = times[-1]

for turn in range(len(times), 2020):
    first, second = last_time_said.get(number, (None, None))
    if first is None:
        number = 0
    else:
        number = second - first
    last_time_said[number] = (last_time_said.get(number, (None, None))[1], turn)

print(number)

# Part 2

indexes = {val: ind for ind, val in enumerate(times)}

num = 0
for turn in range(len(times), 30000000 - 1):
    last_index = indexes.get(num, None)
    indexes[num] = turn
    if last_index is not None:
        num = turn - last_index
    else:
        num = 0

print(num)

