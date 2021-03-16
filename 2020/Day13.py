with open('Day13.txt') as file:
    data = file.read().split()
    time = int(data[0])
    buses = data[1].split(',')

# Part 1

min_wait = float('inf')
min_bus = -1
for schedule in buses:
    if schedule == 'x':
        continue
    schedule = int(schedule)
    wait = (time // schedule + 1) * schedule - time
    if wait < min_wait:
        min_wait = wait
        min_bus = schedule

print(min_bus * min_wait)

# Part 2

times = []
for ind, val in enumerate(buses):
    if val != 'x':
        val = int(val)
        times.append((val, val - (ind % val)))

step, count = times.pop(0)
times = sorted(times, key=lambda a: a[0])
looking, modulo = times.pop(0)

while True:
    if count % looking == modulo:
        step *= looking
        if len(times) == 0:
            break
        looking, modulo = times.pop(0)
    count += step

print(count)

