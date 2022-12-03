with open("Day13.txt", "r") as file:
    data = file.read()

points, folds = data.split('\n\n')

xs = []
ys = []
for point in points.split('\n'):
    x, y = point.split(',')
    xs.append(int(x))
    ys.append(int(y))

paper = [[False for _ in range(max(xs) + 1)] for _ in range(max(ys) + 1)]
for x, y in zip(xs, ys):
    paper[y][x] = True

for fold_number, fold in enumerate(folds.split('\n'), start=1):
    if not fold:
        continue
    *_, fold = fold.split()
    axis, pos = fold.split('=')
    pos = int(pos)

    if axis == 'x':
        for dx in range(1, len(paper[0]) - pos):
            for y in range(len(paper)):
                if paper[y][pos + dx]:
                    paper[y][pos - dx] = True
        for y in range(len(paper)):
            paper[y] = paper[y][:pos]
    else:
        for dy in range(1, len(paper) - pos):
            for x, val in enumerate(paper[pos + dy]):
                if val:
                    paper[pos - dy][x] = True
        paper = paper[:pos]

    if fold_number == 1:
        point_count = 0
        for line in paper:
            for val in line:
                point_count += val
        print(point_count)

for line in paper:
    print(''.join('#' if i else ' ' for i in line))