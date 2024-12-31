import sys

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

bodies = {"COM": (None, 0)}
for line in data.split("\n"):
    center, body = line.split(")")

    if center in bodies and (suborbits := bodies[center][1]) is not None:
        suborbits = suborbits + 1
    else:
        suborbits = None

    bodies[body] = (center, suborbits)

def get_orbits(body):
    center, orbits = bodies[body]
    if orbits is None:
        orbits = get_orbits(center) + 1
        bodies[body] = (center, orbits)
    return orbits

total = 0
for body in bodies:
    total += get_orbits(body)
print(total)

you, you_start = bodies["YOU"]
san, san_start = bodies["SAN"]

you_cur = you_start
san_cur = san_start

while True:
    if you == san:
        break
    elif you_cur > san_cur:
        you, you_cur = bodies[you]
    else:
        san, san_cur = bodies[san]
print((you_start - you_cur) + (san_start - san_cur))