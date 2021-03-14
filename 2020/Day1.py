with open('Day1.txt', 'r') as file:
    data = list(map(int, file.read().split()))

# Part 1
for ind1, val1 in enumerate(data):
    for ind2, val2 in enumerate(data[ind1 + 1:]):
        if val1 + val2 == 2020:
            print(f'{val1} * {val2} = {val1 * val2}')

# Part 2
for ind1, val1 in enumerate(data):
    for ind2, val2 in enumerate(data[ind1 + 1:]):
        for ind3, val3 in enumerate(data[ind2 + 1:]):
            if val1 + val2 + val3 == 2020:
                print(f'{val1} * {val2} * {val3} = {val1 * val2 * val3}')
