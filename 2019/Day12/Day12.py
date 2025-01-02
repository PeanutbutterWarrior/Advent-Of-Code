import sys
import re
from itertools import combinations

class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
    
    def apply_gravity(self, other):
        for axis, vaxis in (("x", "vx"), ("y", "vy"), ("z", "vz")):
            if getattr(self, axis) < getattr(other, axis):
                d = 1
            elif getattr(self, axis) > getattr(other, axis):
                d = -1
            else:
                d = 0
            setattr(self, vaxis, getattr(self, vaxis) + d)
            setattr(other, vaxis, getattr(other, vaxis) - d)
    
    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    @property
    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    @property
    def xhash(self):
        return (self.x, self.vx)

    @property
    def yhash(self):
        return (self.y, self.vy)
    
    @property
    def zhash(self):
        return (self.z, self.vz)

    def __str__(self):
        just = 3
        return f"pos=<x={self.x: >{just}}, y={self.y: >{just}}, z={self.z: >{just}}>, vel=<x={self.vx: >{just}}, y={self.vy: >{just}}, z={self.vz: >{just}}>"

    def __repr__(self):
        return str(self)


moon_pattern = re.compile(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

moons = []
for line in data.split("\n"):
    pos = moon_pattern.match(line)
    moons.append(Moon(*map(int, pos.groups())))

x_states = {}
y_states = {}
z_states = {}

x_repeat = None
y_repeat = None
z_repeat = None

t = 1
while x_repeat is None or y_repeat is None or z_repeat is None or t < 1000:
    for a, b in combinations(moons, r=2):
        a.apply_gravity(b)
    
    for moon in moons:
        moon.apply_velocity()
    
    if t == 1000:
        total = 0
        for moon in moons:
            total += moon.potential_energy * moon.kinetic_energy
        print(total)
    
    if x_repeat is None:
        x_state = tuple(moon.xhash for moon in moons)
        if x_state in x_states:
            x_repeat=  (x_states[x_state], t)
        else:
            x_states[x_state] = t
    
    if y_repeat is None:
        y_state = tuple(moon.yhash for moon in moons)
        if y_state in y_states:
            y_repeat = (y_states[y_state], t)
        else:
            y_states[y_state] = t
    
    if z_repeat is None:
        z_state = tuple(moon.zhash for moon in moons)
        if z_state in z_states:
            z_repeat = (z_states[z_state], t)
        else:
            z_states[z_state] = t
    t += 1

sx, dx = x_repeat
dx -= sx
sy, dy = y_repeat
dy -= sy
sz, dz = z_repeat
dz -= sz

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

d = gcd(dx, dy)
w = dx // d * dy

d = gcd(w, dz)
print(w // d * dz)