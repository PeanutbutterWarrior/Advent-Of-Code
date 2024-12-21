from __future__ import annotations
import sys
from collections import deque
        
with open(sys.argv[1], "r") as file:
    data = file.read().strip()

def printmem(memory):
    for i in memory:
        if i != -1:
            print(i, end="")
        else:
            print(".", end="")
    print()

memory = []
filled = True
index = 0
for i in data:
    if filled:
        memory.extend([index] * int(i))
        index += 1
    else:
        memory.extend([-1] * int(i))
    filled = not filled

fp, bp = 0, len(memory) - 1

while memory[fp] != -1: fp += 1
while memory[bp] == -1: bp -= 1

while fp < bp:
    memory[fp], memory[bp] = memory[bp], memory[fp]
    while memory[fp] != -1: fp += 1
    while memory[bp] == -1: bp -= 1

total = sum(map(lambda x: x[0] * x[1], filter(lambda w: w[1] != -1, enumerate(memory))))
print(total)

memory.clear()
filled = True
index = 0
spaces = [deque() for _ in range(10)]
block_starts = deque()
for i in data:
    i = int(i)
    if filled:
        block_starts.append((len(memory), i))
        memory.extend([index] * i)
        index += 1
    else:
        spaces[i].append(len(memory))
        memory.extend([-1] * i)
    filled = not filled

spaces[0] = None

while len(block_starts) > 0:
    address, length = block_starts.pop()

    min_address, min_space_length = float("inf"), -1
    for space_length, dq in enumerate(spaces[length:], start=length):
        if len(dq) > 0 and dq[0] < min_address:
            min_address = dq[0]
            min_space_length = space_length
        
    if min_space_length == -1: continue
    if min_address > address: continue

    block_address = spaces[min_space_length].popleft()
    space_length = min_space_length

    for i in range(length):
        memory[block_address + i] = memory[address + i]
        memory[address + i] = -1
    
    if space_length > length:
        new_length = space_length - length
        new_address = block_address + length

        for ind, addr in enumerate(spaces[new_length]):
            if addr > new_address:
                spaces[new_length].insert(ind, new_address)
                break
        else:
            spaces[new_length].append(new_address)

total = sum(map(lambda x: x[0] * x[1], filter(lambda w: w[1] != -1, enumerate(memory))))
print(total)