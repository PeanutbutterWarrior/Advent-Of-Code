with open("Day3.txt", "r") as file:
    data = file.read()
nums = list(data.split())


def most_common_bits(numbers):
    totals = [0] * len(numbers[0])
    for num in numbers:
        for ind, val in enumerate(num):
            if val == "0":
                totals[ind] -= 1
            else:
                totals[ind] += 1
    return ''.join('1' if i >= 0 else '0' for i in totals)


gamma = most_common_bits(nums)
gamma = int(gamma, 2)
epsilon = gamma ^ 0b1111_1111_1111
print(gamma * epsilon)

o2_candidates = nums.copy()
index = 0
while len(o2_candidates) > 1 and index < 12:
    common_bit = most_common_bits(o2_candidates)[index]
    new_o2_candidates = []
    for candidate in o2_candidates:
        if candidate[index] == common_bit:
            new_o2_candidates.append(candidate)
    o2_candidates = new_o2_candidates
    index += 1

co2_candidates = nums.copy()
index = 0
while len(co2_candidates) > 1 and index < 12:
    common_bit = most_common_bits(co2_candidates)[index]
    new_co2_candidates = []
    for candidate in co2_candidates:
        if candidate[index] != common_bit:
            new_co2_candidates.append(candidate)
    co2_candidates = new_co2_candidates
    index += 1

print(int(o2_candidates[0], 2) * int(co2_candidates[0], 2))
