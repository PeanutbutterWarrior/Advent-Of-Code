with open("Day11.txt", "r") as file:
    data = file.read()

octopi = []
for row in data.split():
    if row:
        octopi.append(list(map(int, row)))
flashed = [[False] * 10 for _ in range(10)]

flash_count = 0
step = 0
while True:
    step += 1
    to_flash = []
    for x in range(10):
        for y in range(10):
            octopi[y][x] += 1
            flashed[y][x] = False
            if octopi[y][x] > 9:
                to_flash.append((x, y))

    while to_flash:
        x, y = to_flash.pop(-1)
        if flashed[y][x]:
            continue
        flashed[y][x] = True
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x + dx < 10 and 0 <= y + dy < 10:
                    octopi[y + dy][x + dx] += 1
                    if octopi[y + dy][x + dx] > 9:
                        to_flash.append((x + dx, y + dy))
    found_unflashed = False
    for x in range(10):
        for y in range(10):
            if flashed[y][x]:
                flash_count += 1
                octopi[y][x] = 0
            else:
                found_unflashed = True

    if not found_unflashed:
        print(step)
        break

    if step == 100:
        print(flash_count)
