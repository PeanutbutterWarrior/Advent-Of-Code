with open("input.txt", "r") as file:
    data = file.read()

rows = [tuple(map(int, line.split(" "))) for line in data.split("\n")]

def is_ok(a, b):
    if not (1 <= abs(a - b) <= 3):
        return False, False
    return True, b > a

def is_level_ok(levels):
    if len(levels) < 2:
        return True
    asc = None

    for prev, lev in zip(levels, levels[1:]):
        ok, dir = is_ok(prev, lev)
        if not ok: return False
        if asc is None: asc = dir
        if dir != asc: return False
    return True

num_safe = 0
for level in rows:
    if is_level_ok(level):
        num_safe += 1

print(num_safe)

num_safe = 0
for levels in rows:
    for skipping in range(len(levels)):
        if is_level_ok(levels[:skipping] + levels[skipping + 1:]):
            num_safe += 1
            break
print(num_safe)
    
    