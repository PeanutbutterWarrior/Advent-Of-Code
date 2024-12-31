import sys
from Intcode import Intcode
from itertools import permutations

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

base_mem = Intcode.parse_input(data)

max_signal = 0
for perm in permutations([0, 1, 2, 3, 4], r=5):
    signal = 0
    for setting in perm:
        interp = Intcode(base_mem.copy(), [setting, signal])
        signal = interp.run()[0]
    max_signal = max(max_signal, signal)
print(max_signal)