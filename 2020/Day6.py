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

# Part 2


def convert_to_num(answer):
    num = 0
    for char in answer:
        num |= 1 << ord(char) - 97
    return num


count = 0
answers = 2 ** 26 - 1
for line in data:
    if line:
        answers &= convert_to_num(line)
    else:
        count += bin(answers).count('1')
        answers = 2 ** 26 - 1
print(count)
