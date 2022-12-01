from collections import defaultdict

with open('Day7.txt', 'r') as file:
    data = file.read().split('\n')


def parse_line(line):
    line = line.split(' ')
    parent = f'{line[0]} {line[1]}'
    if line[4] == 'no':
        return parent, []
    children_words = line[4:]
    children = []
    for i in range(0, len(children_words), 4):
        num, name1, name2, _ = children_words[i:i + 4]
        children.append((f'{name1} {name2}', int(num)))
    return parent, children


# Part 1

parents = defaultdict(list)
for rule in data:
    if rule:
        parent, children = parse_line(rule)
        for child in children:
            parents[child[0]].append(parent)

possible_parents = set()
unchecked_parents = ['shiny gold']
while len(unchecked_parents) > 0:
    child = unchecked_parents.pop(-1)
    for parent in parents[child]:
        if parent not in possible_parents:
            possible_parents.add(parent)
            unchecked_parents.append(parent)
print(len(possible_parents))

# Part 2

children = defaultdict(list)
count = 0
for rule in data:
    if rule:
        parent, childs = parse_line(rule)
        children[parent] += childs


def check_children(bag):
    count = 0
    for child, num in children[bag]:
        count += num * check_children(child)
    return count + 1


print(check_children('shiny gold') - 1)
