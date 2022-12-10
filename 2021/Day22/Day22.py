import re
from dataclasses import dataclass

@dataclass
class Box:
    state: bool
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    def size(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)

    def get_collision(self, r2):
        min_collision_x = None
        max_collision_x = None
        min_collision_y = None
        max_collision_y = None
        min_collision_z = None
        max_collision_z = None
        if self.x1 <= r2.x1 <= self.x2:
            min_collision_x = r2.x1
            max_collision_x = min(r2.x2, self.x2)
        elif self.x1 <= r2.x2 <= self.x2:
            min_collision_x = max(self.x1, r2.x1)
            max_collision_x = r2.x2

        if self.y1 <= r2.y1 <= self.y2:
            min_collision_y = r2.y1
            max_collision_y = min(r2.y2, self.y2)
        elif self.y1 <= r2.y2 <= self.y2:
            min_collision_y = max(self.y1, r2.y1)
            max_collision_y = r2.y2

        if self.z1 <= r2.z1 <= self.z2:
            min_collision_z = r2.z1
            max_collision_z = min(r2.z2, self.z2)
        elif self.z1 <= r2.z2 <= self.z2:
            min_collision_z = max(self.z1, r2.z1)
            max_collision_z = r2.z2

        if min_collision_x is None or min_collision_y is None or min_collision_z is None:
            return None
        return Box(False,
                   min_collision_x, max_collision_x,
                   min_collision_y, max_collision_y,
                   min_collision_z, max_collision_z)

    def split_other(self, other):
        intersection = self.get_collision(other)
        if intersection is None:
            return [other]

        if intersection.x1 == other.x1:
            b1_x1 = intersection.x1
            b1_x2 = other.x2
            b2_x1 = intersection.x2
            b2_x2 = other.x2
            b3_x1 = other.x1
            b3_x2 = intersection.x2
        else:
            b1_x1 = other.x1
            b1_x2 = intersection.x2
            b2_x1 = other.x1
            b2_x2 = intersection.x1
            b3_x1 = intersection.z1
            b3_x2 = other.x2

        if intersection.y1 == other.y1:
            b1_y1 = intersection.y2
            b1_y2 = other.y2
            b2_y1 = other.y1
            b2_y2 = intersection.y2
            b3_y1 = other.y1
            b3_y2 = intersection.y2
        else:
            b1_y1 = other.y1
            b1_y2 = intersection.y1
            b2_y1 = intersection.y1
            b2_y2 = other.y2
            b3_y1 = other.y1
            b3_y2 = intersection.y2

        if intersection.z1 == other.z1:
            b1_z1 = intersection.z1
            b1_z2 = other.z2
            b2_z1 = intersection.z1
            b2_z2 = other.z2
            b3_z1 = intersection.z2
            b3_z2 = other.z2
        else:
            b1_z1 = other.z1
            b1_z2 = intersection.z2
            b2_z1 = other.z1
            b2_z2 = intersection.z2
            b3_z1 = other.z1
            b3_z2 = intersection.z1
        
        b1 = Box(True, b1_x1, b1_x2, b1_y1, b1_y2, b1_z1, b1_z2)
        b2 = Box(True, b2_x1, b2_x2, b2_y1, b2_y2, b2_z1, b2_z2)
        b3 = Box(True, b3_x1, b3_x2, b3_y1, b3_y2, b3_z1, b3_z2)

        return list(filter(lambda i: i.size() > 0, (b1, b2, b3)))


with open("test.txt", "r") as file:
    data = file.read()

line_regex = re.compile('(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)')

instructions = []
for line in data.split('\n'):
    if line:
        state, *corners = line_regex.match(line).groups()
        instructions.append(Box(state == 'on', *map(int, corners)))

areas = []
total = 0
for box in instructions[::-1]:
    sub_areas = [box]
    for area in areas:
        new_areas = []
        for sub_area in sub_areas:
            new_areas.extend(area.split_other(area))
        sub_areas = new_areas
    areas.extend(sub_areas)
    if box.state:
        for area in sub_areas:
            total += area.size()

print(total)