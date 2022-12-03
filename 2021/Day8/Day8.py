with open("Day8.txt", "r") as file:
    data = file.read()

displays = []
for line in data.split('\n'):
    if not line:
        continue
    a, b = line.split(' | ')
    displays.append((sorted(map(set, a.split()), key=len), b.split()))

count = 0
for display in displays:
    for item in display[1]:
        if len(item) in {2, 3, 4, 7}:
            count += 1
print(count)

total = 0
for train, output in displays:
    mappings = {}

    counts = {}
    for digit in train:
        for segment in digit:
            counts[segment] = counts.get(segment, 0) + 1
    for segment, count in counts.items():
        if count == 4:
            mappings[segment] = 'e'
        elif count == 6:
            mappings[segment] = 'b'
        elif count == 9:
            mappings[segment] = 'f'

    a = train[1] - train[0]
    mappings[a.pop()] = 'a'

    a, b = train[0]
    if a in mappings:
        mappings[b] = 'c'
    else:
        mappings[a] = 'c'

    a, b = train[2] - train[0]
    if a in mappings:
        mappings[b] = 'd'
        d = b
    else:
        mappings[a] = 'd'
        d = a

    for segment, count in counts.items():
        if count == 7 and segment != d:
            mappings[segment] = 'g'
            break

    num = 0
    translations = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
    }
    for display in output:
        num *= 10
        num += translations[''.join(sorted(map(mappings.get, display)))]

    total += num
print(total)