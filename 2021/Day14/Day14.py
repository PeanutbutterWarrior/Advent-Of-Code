from itertools import repeat

with open("Day14.txt", "r") as file:
    data = file.read()

base, rules = data.split('\n\n')
letters = ['O', 'S', 'H', 'B', 'K', 'F', 'V', 'C', 'N', 'P']
empty_totals = dict(zip(letters, repeat(0)))

inserts = {}
total_after_steps = [{}]
for rule in rules.split('\n'):
    if rule:
        k, v = rule.split(' -> ')
        inserts[k] = v
        totals = empty_totals.copy()
        totals[k[0]] += 1
        totals[k[1]] += 1
        total_after_steps[0][k] = totals

for _ in range(40):
    total_after_steps.append({})
    for k, v in inserts.items():
        totals = empty_totals.copy()
        for a, b in total_after_steps[-2][k[0] + v].items():
            totals[a] += b
        for a, b in total_after_steps[-2][v + k[1]].items():
            totals[a] += b
        totals[v] -= 1
        total_after_steps[-1][k] = totals

totals = empty_totals.copy()
for i in range(len(base) - 1):
    for a, b in total_after_steps[-1][base[i] + base[i + 1]].items():
        totals[a] += b
for i in range(1, len(base) - 1):
    totals[base[i]] -= 1
print(max(totals.values()) - min(totals.values()))