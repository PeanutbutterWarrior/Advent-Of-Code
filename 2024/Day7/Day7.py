import sys
import math

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

add = lambda x, y: x + y
mul = lambda x, y: x * y
concat = lambda x, y: 10**math.floor(math.log10(y) + 1) * x + y

def try_funcs(index, current, arguments, funcs):
    if index == len(arguments):
        yield current
        return

    for func in funcs:
        yield from try_funcs(index + 1, func(current, arguments[index]), arguments, funcs)


lines = []
for line in data.split("\n"):
    target, nums = line.split(": ")
    lines.append((int(target), tuple(map(int, nums.split(" ")))))

total = 0
funcs = (add, mul)
for target, nums in lines:
    for item in try_funcs(1, nums[0], nums, funcs):
        if item == target:
            total += target
            break
print(total)

total = 0
funcs = (add, mul, concat)
for target, nums in lines:
    for item in try_funcs(1, nums[0], nums, funcs):
        if item == target:
            total += target
            break
print(total)