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

max_signal = 0
for perm in permutations([5, 6, 7, 8, 9], r=5):
    comps = [Intcode(base_mem.copy(), [perm[i]]) for i in range(5)]
    for comp in comps:
        comp.run()
    
    signal = 0
    last_signal = 0
    while comps[-1].running:
        for comp in comps:
            comp.give_input(signal)
            signal = comp.run()[-1]
    max_signal = max(signal, max_signal)
print(max_signal)
    