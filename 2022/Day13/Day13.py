from functools import cmp_to_key


def parse_list(string, index):
    if string[index] == '[':
        index += 1
        l = []
        while string[index] != ']':
            item, index = parse_list(string, index)
            l.append(item)
            if string[index] == ',':
                index += 1
        index += 1
        return l, index
    else:
        start_index = index
        while string[index].isdigit():
            index += 1
        return int(string[start_index:index]), index


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif type(left) == list and type(right) == list:
        for a, b in zip(left, right):
            result = compare(a, b)
            if result != 0:
                return result
        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        else:
            return 0
    else:
        if type(left) == int:
            left = [left]
        if type(right) == int:
            right = [right]
        return compare(left, right)


with open("Day13.txt", "r") as file:
    data = file.read()

total = 0
for index, (list_1, list_2) in enumerate(map(str.split, data.split('\n\n')), start=1):
    list_1_parsed, _ = parse_list(list_1, 0)
    list_2_parsed, _ = parse_list(list_2, 0)
    if compare(list_1_parsed, list_2_parsed) == -1:
        total += index
print(total)

lists = [parse_list(line, 0)[0] for line in data.split() if line]
lists.append([[2]])
lists.append([[6]])
lists = sorted(lists, key=cmp_to_key(compare))
num = 1
for ind, l in enumerate(lists, start=1):
    if l == [[2]] or l == [[6]]:
        num *= ind
print(num)