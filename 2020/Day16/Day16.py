import re

with open('Day16.txt', 'r') as file:
    data = file.read().split('\n')

rule_pattern = re.compile('([a-zA-Z ]+): (\d+)-(\d+) or (\d+)-(\d+)')

rules = {}
iterator = iter(data)

for line in iterator:
    if not line:
        break
    match = re.fullmatch(rule_pattern, line)
    name, *nums = match.groups()
    start1, end1, start2, end2 = map(int, nums)
    rules[name] = (range(start1, end1 + 1), range(start2, end2 + 1))

next(iterator)  # Consumes 'your ticket:'
own_ticket_fields = list(map(int, next(iterator).split(',')))

next(iterator)  # Consumes blank line
next(iterator)  # Consumes 'nearby tickets:'

tickets = [list(map(int, line.split(','))) for line in iterator]

# Part 1

error_total = 0

for ticket in tickets:
    for field in ticket:
        for rule in rules.values():
            if field in rule[0] or field in rule[1]:
                break
        else:
            error_total += field

print(error_total)

# Part 2

valid_tickets = []

for ticket in tickets:
    for field in ticket:
        for rule in rules.values():
            if field in rule[0] or field in rule[1]:
                break
        else:
            break
    else:
        valid_tickets.append(ticket)

tickets = valid_tickets
possible_fields = [set(rules.keys()) for i in range(len(own_ticket_fields))]

for ticket in tickets:
    for rule, (range1, range2) in rules.items():
        for ind, field in enumerate(ticket):
            if field not in range1 and field not in range2:
                possible_fields[ind].discard(rule)

changed = True
rule_order = [None] * len(possible_fields)
while changed:
    changed = False
    for ind, possible in enumerate(possible_fields):
        if len(possible) == 1:
            changed = True
            item = possible.pop()
            rule_order[ind] = item
            for i in possible_fields:
                if i is not possible:
                    i.discard(item)

product = 1
for rule, field in zip(rule_order, own_ticket_fields):
    if rule[:9] == 'departure':
        product *= field
print(product)