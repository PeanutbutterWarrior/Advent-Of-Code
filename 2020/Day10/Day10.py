with open('Day10.txt', 'r') as file:
    data = sorted(map(int, file.read().split()))

data.insert(0, 0)  # Source
data.append(max(data) + 3)  # Device

# Part 1

one_jolt_diffs = 0
three_jolt_diffs = 0
prev = -5
for adaptor in data:
    if adaptor - prev == 1:
        one_jolt_diffs += 1
    elif adaptor - prev == 3:
        three_jolt_diffs += 1
    prev = adaptor
print(one_jolt_diffs * three_jolt_diffs)

# Part 2

data = set(data)
checked = {}


def paths_to(number):
    if number in checked:
        return checked[number]
    if number == 0:
        return 1

    ways_here = 0
    if number - 1 in data:
        ways_here += paths_to(number - 1)
    if number - 2 in data:
        ways_here += paths_to(number - 2)
    if number - 3 in data:
        ways_here += paths_to(number - 3)
    checked[number] = ways_here
    return ways_here


print(paths_to(max(data)))
