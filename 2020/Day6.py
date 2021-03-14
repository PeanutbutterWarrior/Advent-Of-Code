with open('Day6.txt', 'r') as file:
    data = file.read().split('\n')

# Part 1
count = 0
answers = [False] * 26
for line in data:
    if line:
        for char in line:
            answers[ord(char) - 97] = True
    else:
        count += answers.count(True)
        answers = [False] * 26
print(count)