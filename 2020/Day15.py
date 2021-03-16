with open('Day15.txt', 'r') as file:
    times = list(map(int, file.read().split(',')))

# Part 1

last_time_said = {val: (None, ind) for ind, val in enumerate(times)}
previous_number = times[-1]

for turn in range(len(times), 2020):
    first, second = last_time_said.get(previous_number, (None, None))
    if first is None:
        number = 0
    else:
        number = second - first
    last_time_said[number] = (last_time_said.get(number, (None, None))[1], turn)
    print(number)
    previous_number = number

print(previous_number)
