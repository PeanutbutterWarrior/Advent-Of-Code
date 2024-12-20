import sys

def obeys_rules(update, rules):
    seen = set()
    for item in update:
        for prereq in rules.get(item, []):
            if prereq in update and prereq not in seen:
                return False
        seen.add(item)
    return True

def reorder(update, rules):
    seen = set()
    prereqs = {}
    for item in update:
        prereqs[item] = rules.get(item, [])
    
    order = []
    while len(order) < len(update):
        for item, reqs in prereqs.items():
            if item in seen:
                continue
            for req in reqs:
                if req in prereqs and req not in seen:
                    break
            else:
                order.append(item)
                seen.add(item)
    return order
        
        

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

a, b = data.split("\n\n")
rules = {}
for line in a.split("\n"):
    x, y = line.split("|")
    y = int(y)
    if y not in rules:
        rules[y] = []
    rules[y].append(int(x))

updates = []
for update in b.split("\n"):
    updates.append(tuple(map(int, update.split(","))))

total1 = 0
total2 = 0
for update in updates:
    if obeys_rules(update, rules):
        total1 += update[len(update) // 2]
    else:
        update = reorder(update, rules)
        total2 += update[len(update) // 2]

print(total1)
print(total2)