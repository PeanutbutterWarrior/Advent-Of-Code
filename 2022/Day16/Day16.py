import re
from pprint import pprint

with open("test.txt", "r") as file:
    data = file.read()

line_regex = re.compile(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)$')

valves = {}

for line in data.split('\n'):
    valve, flow, connections = line_regex.fullmatch(line).groups()
    flow = int(flow)
    valves[valve] = (flow, connections.split(', '))

best_possible: list[dict[str, list[dict[str, int]]]] = [{k: [{l: 0 for l in valves}] for k in valves}]

for time in range(1, 30):
    best = {}
    for valve, (flow, connections) in valves.items():
        best_found = []
        best_score = -1
        for connection in connections:
            if (score := sum(best_possible[-1][connection][0].values())) > best_score:
                best_found = best_possible[-1][connection]
                best_score = score
            elif score == best_score:
                best_found.extend(best_possible[-1][connection])

        new_score = sum(best_possible[-1][valve][0].values())
        for option in best_possible[-1][valve]:
            if (score := new_score - option[valve] + flow * time) > best_score:
                best_found = [option.copy()]
                best_found[0][valve] = flow * time
                best_score = score
            elif score == best_score:
                best_found.append(option.copy())
                best_found[-1][valve] = flow * time

        seen = set()
        correct = []
        for option in best_found:
            if (hashable := tuple(option.items())) not in seen:
                seen.add(hashable)
                correct.append(option)
        if len(correct) > 1:
            print("yes")

        best[valve] = correct
    best_possible.append(best)

pprint(best_possible[-1])
print(sum(best_possible[-1]['AA'][0].values()))