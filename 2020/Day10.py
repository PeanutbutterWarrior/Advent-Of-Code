with open('Day10.txt', 'r') as file:
    data = sorted(map(int, file.read().split()))

# Part 1

one_jolt_diffs = 1
three_jolt_diffs = 0
prev = -5
for adaptor in data:
    if adaptor - prev == 1:
        one_jolt_diffs += 1
    elif adaptor - prev == 3:
        three_jolt_diffs += 1
    prev = adaptor
three_jolt_diffs += 1  # Going from final adaptor to device
print(one_jolt_diffs * three_jolt_diffs)
