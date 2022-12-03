with open("Day7.txt", "r") as file:
    data = file.read()

positions = list(map(int, data.split(',')))

costs = [0]
for i in range(1, max(positions) + 1):
    costs.append(costs[-1] + i)

min_cost = float('inf')
for aim_position in range(max(positions) + 1):
    cost = 0
    for position in positions:
        cost += costs[abs(aim_position - position)]
    if cost < min_cost:
        min_cost = cost
print(min_cost)