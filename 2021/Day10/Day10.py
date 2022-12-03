with open("Day10.txt", "r") as file:
    data = file.read()

open_brackets = ['(', '[', '{', '<']
close_brackets = [')', ']', '}', '>']
scores = [3, 57, 1197, 25137]
mapping = dict(zip(open_brackets, close_brackets))

score = 0
correct_lines = []
for line in data.split():
    if not line:
        continue

    seen_chars = []
    for char in line:
        if char in {'(', '{', '[', '<'}:
            seen_chars.append(char)
        elif char == mapping[seen_chars[-1]]:
            seen_chars.pop(-1)
        else:
            score += scores[close_brackets.index(char)]
            break
    else:
        correct_lines.append((line, seen_chars))
print(score)

scores = []
for line, needed_chars in correct_lines:
    score = 0
    for char in needed_chars[::-1]:
        score *= 5
        score += open_brackets.index(char) + 1
    scores.append(score)
scores.sort()
print(scores[len(scores) // 2])