import sys
from Intcode import Intcode
from collections import deque

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

program = Intcode.parse_input(data)

def is_pulled(x, y):
    interp = Intcode(program.copy(), (x, y))
    return interp.run()[0] == 1

total = 1

target_size = 100
target_size -= 1

left, y = 4, 4
right = left

lefts = deque(maxlen=target_size)
rights = deque(maxlen=target_size)

while True:
    y += 1
    if not is_pulled(left, y):
        left += 1
    if is_pulled(right + 1, y):
        right += 1
    
    if y < 50:
        total += right - left + 1

    if len(lefts) == target_size and left + target_size <= rights[0] and right - left >= target_size:
        break

    lefts.append(left)
    rights.append(right)

print(total)
print(y - target_size + left * 10_000)