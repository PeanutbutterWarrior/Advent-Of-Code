with open('Day9.txt', 'r') as file:
    data = list(map(int, file.read().split()))


def check_sum(number, pairs):
    for ind1, val1 in enumerate(pairs):
        for ind2, val2 in enumerate(pairs[ind1 + 1:], ind1 + 1):
            if val1 + val2 == number:
                return True
    return False


# Part 1

for ind, val in enumerate(data[25:], 25):
    if not check_sum(val, data[ind-25:ind]):
        print(val)
        break
