with open('Day9.txt', 'r') as file:
    data = list(map(int, file.read().split()))


def check_sum(number, pairs):
    for ind1, val1 in enumerate(pairs):
        for ind2, val2 in enumerate(pairs[ind1 + 1:], ind1 + 1):
            if val1 + val2 == number:
                return True
    return False


# Part 1
invalid_number = None
for ind, val in enumerate(data[25:], 25):
    if not check_sum(val, data[ind-25:ind]):
        invalid_number = val
        break
print(invalid_number)

# Part 2

for start_index in range(len(data)):
    end_index = start_index + 1
    while True:
        summed = sum(data[start_index:end_index + 1])
        if summed == invalid_number:
            print(min(data[start_index:end_index + 1]) + max(data[start_index:end_index + 1]))
            exit()
        elif summed > invalid_number:
            break
        end_index += 1

