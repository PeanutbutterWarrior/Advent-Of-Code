import sys
import re
import math

with open(sys.argv[1], "r") as file:
    data = file.read().strip()


def solve_machine(machine):
    (ax, ay), (bx, by), (tx, ty) = machine
    if bx * ay == ax * by:
        print("Error 1")
    m: float = (ay * tx - ax * ty) / (bx * ay - ax * by)
    n: float = (tx - m * bx) / ax
    assert math.isclose((ty - m * by) / ay, n)
    return n, m

machines = []
button_pattern = re.compile("^Button .: X\+(\d+), Y\+(\d+)$")
prize_pattern = re.compile("^Prize: X=(\d+), Y=(\d+)$")
for machine in data.split("\n\n"):
    a, b, t = machine.split("\n")
    ax, ay = button_pattern.match(a).group(1,2)
    bx, by = button_pattern.match(b).group(1,2)
    tx, ty = prize_pattern.match(t).group(1,2)

    machines.append([(int(ax), int(ay)), (int(bx), int(by)), (int(tx), int(ty))])

total = 0
for machine in machines:
    n, m = solve_machine(machine)
    if m.is_integer() and n.is_integer():
        total += int(n * 3 + m)
print(total)

total = 0
for machine in machines:
    machine[2] = (machine[2][0] + 10000000000000, machine[2][1] + 10000000000000)
    n, m = solve_machine(machine)
    if m.is_integer() and n.is_integer():
        total += int(n * 3 + m)
print(total)