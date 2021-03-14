with open('Day3.txt', 'r') as file:
    data = file.read().split()

# Part 1

x_position = 0
tree_count = 0
for line in data:
    if line[x_position] == '#':
        tree_count += 1
    x_position = (x_position + 3) % len(line)
print(tree_count)
