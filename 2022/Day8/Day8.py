with open("Day8.txt", "r") as file:
    data = file.read()

forest = [[int(i) for i in line] for line in data.split()]
width = len(forest[0])
height = len(forest)

max_score = 0
visible_count = 0
for y, line in enumerate(forest):
    for x, tree in enumerate(line):
        score = 1
        visible = False

        count = 0
        for dx in range(x + 1, width):
            count += 1
            if forest[y][dx] >= tree:
                break
        else:
            visible = True
        score *= count

        count = 0
        for dx in range(x - 1, -1, -1):
            count += 1
            if forest[y][dx] >= tree:
                break
        else:
            visible = True
        score *= count

        count = 0
        for dy in range(y + 1, height):
            count += 1
            if forest[dy][x] >= tree:
                break
        else:
            visible = True
        score *= count

        count = 0
        for dy in range(y - 1, -1, -1):
            count += 1
            if forest[dy][x] >= tree:
                break
        else:
            visible = True
        score *= count

        if score > max_score:
            max_score = score
        if visible:
            visible_count += 1
print(visible_count)
print(max_score)
