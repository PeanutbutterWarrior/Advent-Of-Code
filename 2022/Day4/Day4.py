with open("Day4.txt", "r") as file:
    data = file.read()

pairs = []
for line in data.split():
    if not line:
        continue
    e1, e2 = line.split(',')
    a, b = e1.split('-')
    c, d = e2.split('-')
    pairs.append(((int(a), int(b)), (int(c), int(d))))

count = 0
for (start1, end1), (start2, end2) in pairs:
    if start1 <= start2 and end2 <= end1:
        count += 1
    elif start2 <= start1 and end1 <= end2:
        count += 1
print(count)

count = 0
for (start1, end1), (start2, end2) in pairs:
    if start2 <= start1 <= end2 or start2 <= end1 <= end2:
        count += 1
    elif start1 <= start2 <= end1 or start1 <= end2 <= end1:
        count += 1
print(count)