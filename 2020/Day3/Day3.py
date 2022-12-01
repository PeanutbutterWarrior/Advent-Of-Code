with open('Day3.txt', 'r') as file:
    data = file.read().split()


def check_slope(across, down):
    x_position = 0
    tree_count = 0
    for index, line in enumerate(data):
        if index % down != 0:
            continue
        if line[x_position] == '#':
            tree_count += 1
        x_position = (x_position + across) % len(line)
    return tree_count


# Part 1

print(check_slope(3, 1))

# Part 2
combinations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1
for combo in combinations:
    product *= check_slope(*combo)
print(product)
