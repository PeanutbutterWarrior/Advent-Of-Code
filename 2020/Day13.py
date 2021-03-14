with open('Day13.txt') as file:
    data = file.read().split()
    time = int(data[0])
    buses = list(map(int, filter(str.isdigit, data[1].split(','))))

# Part 1

min_wait = float('inf')
min_bus = -1
for schedule in buses:
    wait = (time // schedule + 1) * schedule - time
    if wait < min_wait:
        min_wait = wait
        min_bus = schedule

print(min_bus * min_wait)