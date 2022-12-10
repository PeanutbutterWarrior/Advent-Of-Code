with open("Day19.txt", "r") as file:
    data = file.read()

transformations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (x, -y, -z),

    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, z, y),

    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (y, -z, -x),

    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-y, -z, x),

    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (z, x, y),

    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (-z, -x, y),
]

class Beacon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.relatives = None
        self.base_relative = None

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        if type(other) == Beacon:
            return self.x == other.x and self.y == other.y and self.z == other.z
        elif type(other) == tuple:
            return self.x == other[0] and self.y == other[1] and self.z == other[2]

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

    def __repr__(self):
        return str(self)

    def calculate_base_relative(self, others):
        self.base_relative = frozenset(
            (other.x - self.x, other.y - self.y, other.z - self.z) for other in others
        )

    def calculate_relatives(self, others):
        self.calculate_base_relative(others)
        self.relatives = [
            frozenset(f(*pos) for pos in self.base_relative)
            for f in transformations
        ]
        return self.relatives


scanners = []
for scanner in data.split('\n\n'):
    scanners.append([])
    for line in scanner.split('\n')[1:]:
        x, y, z = line.split(',')
        scanners[-1].append(Beacon(int(x), int(y), int(z)))
    for beacon in scanners[-1]:
        beacon.calculate_relatives(scanners[-1])

scanner_0, *scanners = scanners
scanner_0 = set(scanner_0)

scanner_positions = [(0, 0, 0)]


while len(scanners) > 0:
    print(f"{len(scanners)} scanners left to merge")
    break_1 = False
    for scanner_index, scanner in enumerate(scanners):
        break_2 = False
        for beacon_0 in scanner_0:
            break_3 = False
            for beacon_other in scanner:
                for transformation_index, relatives in enumerate(beacon_other.relatives):
                    if len(beacon_0.base_relative & relatives) >= 12:
                        x, y, z = transformations[transformation_index](beacon_other.x, beacon_other.y, beacon_other.z)
                        dx = x - beacon_0.x
                        dy = y - beacon_0.y
                        dz = z - beacon_0.z
                        scanner_positions.append((-dx, -dy, -dz))
                        new_beacons = []
                        for beacon in scanner:
                            x, y, z = transformations[transformation_index](beacon.x, beacon.y, beacon.z)
                            new_beacons.append(Beacon(x - dx, y - dy, z - dz))
                        scanner_0.update(new_beacons)
                        for beacon in new_beacons:
                            beacon.calculate_relatives(scanner_0)
                        scanners.pop(scanner_index)
                        break_1 = break_2 = break_3 = True
                        break
                if break_3:
                    break
            if break_2:
                break
        if break_1:
            break
    else:
        print("No scanners overlap")
        break

print(len(scanner_0))

max_distance = 0
for x1, y1, z1 in scanner_positions:
    for x2, y2, z2 in scanner_positions:
        dist = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
        if dist > max_distance:
            max_distance = dist
print(max_distance)