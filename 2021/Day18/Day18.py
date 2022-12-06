from math import floor, ceil
from itertools import permutations

def add(n1, n2):
    num = ['['] + n1 + [','] + n2 + [']']

    changed = True
    while changed:
        changed = False
        depth = 0
        for ind, char in enumerate(num):
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
            if depth == 5:
                changed = True
                popped_num = [num.pop(ind) for _ in range(5)]
                num.insert(ind, 0)
                try:
                    assert popped_num[0] == '['
                    left = popped_num[1]
                    assert popped_num[2] == ','
                    right = popped_num[3]
                    assert popped_num[4] == ']'
                except AssertionError:
                    raise

                for right_ind in range(ind + 1, len(num)):
                    if type(num[right_ind]) == int:
                        num[right_ind] += right
                        break

                for left_ind in range(ind - 1, -1, -1):
                    if type(num[left_ind]) == int:
                        num[left_ind] += left
                        break
                break
        if changed:
            continue

        for ind, char in enumerate(num):
            if type(char) == int:
                if char > 9:
                    changed = True
                    n = num.pop(ind)
                    num.insert(ind, '[')
                    num.insert(ind + 1, floor(n/2))
                    num.insert(ind + 2, ',')
                    num.insert(ind + 3, ceil(n / 2))
                    num.insert(ind + 4, ']')
                    break
    return num


def get_magnitude(number, index):
    if number[index] == '[':
        index, left = get_magnitude(number, index + 1)
        assert number[index] == ','
        index, right = get_magnitude(number, index + 1)
        assert number[index] == ']'
        return index + 1, 3 * left + 2 * right
    else:
        return index + 1, number[index]


with open("Day18.txt", "r") as file:
    data = file.read()

numbers = []
for line in data.split():
    if not line:
        continue
    num = list(line)
    for ind, char in enumerate(num):
        if char.isdigit():
            num[ind] = int(char)
    numbers.append(num)

num, *lines = numbers
for n in lines:
    num = add(num, n)

print(get_magnitude(num, 0))

max_magnitude = 0
for ind, (a, b) in enumerate(permutations(numbers, r=2)):
    _, m = get_magnitude(add(a, b), 0)
    if m > max_magnitude:
        max_magnitude = m
print(max_magnitude)