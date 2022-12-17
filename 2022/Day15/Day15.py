from dataclasses import dataclass
import re


@dataclass
class Beacon:
    x: int
    y: int


@dataclass
class Sensor:
    x: int
    y: int
    beacon: Beacon

    def __post_init__(self):
        self.distance = self.distance_from(self.beacon.x, self.beacon.y)

    def distance_from(self, x, y):
        return abs(self.x - x) + abs(self.y - y)


with open("Day15.txt", "r") as file:
    data = file.read()

line_pattern = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

sensors = []
beacons = []
beacon_positions = {}
min_x = min_y = float('inf')
max_x = max_y = max_distance = float('-inf')
for line in data.split('\n'):
    x1, y1, x2, y2 = map(int, line_pattern.fullmatch(line).groups())
    if x1 < min_x:
        min_x = x1
    if x1 > max_x:
        max_x = x1
    if y1 < min_y:
        min_y = y1
    if y1 > max_y:
        max_y = y1

    if x2 < min_x:
        min_x = x2
    if x2 > max_x:
        max_x = x2
    if y2 < min_y:
        min_y = y2
    if y2 > max_y:
        max_y = y2

    if (x2, y2) in beacon_positions:
        beacon = beacon_positions[(x2, y2)]
    else:
        beacon = Beacon(x2, y2)
        beacon_positions[(x2, y2)] = beacon
        beacons.append(beacon)

    sensors.append(Sensor(x1, y1, beacon))
    if sensors[-1].distance > max_distance:
        max_distance = sensors[-1].distance

y = 2000000
ranges = []
for sensor in sensors:
    distance_at_y = sensor.distance - abs(sensor.y - y)
    if distance_at_y >= 0:
        ranges.append((sensor.x - distance_at_y, sensor.x + distance_at_y))

ranges.sort()

index = 0
while index < len(ranges) - 1:
    if ranges[index][1] >= ranges[index + 1][0]:
        ranges[index] = (ranges[index][0], max(ranges[index + 1][1], ranges[index][1]))
        ranges.pop(index + 1)
    else:
        index += 1

count = 0
for r in ranges:
    count += r[1] - r[0] + 1

for beacon in beacons:
    if beacon.y == y:
        count -= 1
print(count)


for y in range(4000000):
    ranges = []
    for sensor in sensors:
        distance_at_y = sensor.distance - abs(sensor.y - y)
        if distance_at_y >= 0:
            ranges.append((sensor.x - distance_at_y, sensor.x + distance_at_y))

    ranges.sort()

    index = 0
    while index < len(ranges) - 1:
        if ranges[index][1] >= ranges[index + 1][0]:
            ranges[index] = (ranges[index][0], max(ranges[index + 1][1], ranges[index][1]))
            ranges.pop(index + 1)
        else:
            index += 1

    count = 0
    for a, b in ranges:
        if a < 0:
            a = 0
        if b > 4000000:
            b = 4000000
        count += b - a + 1

    if count != 4000001:
        a, b = ranges
        print((a[1] + 1) * 4000000 + y)
        break
