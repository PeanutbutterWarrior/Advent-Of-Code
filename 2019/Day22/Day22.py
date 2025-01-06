import sys
import re
from enum import Enum
from functools import cache

class Action(Enum):
    NEW_STACK = 0
    CUT = 1
    DEAL = 2

with open(sys.argv[1], "r") as file:
    data = file.read().strip("\n")

deal_re = re.compile("deal with increment (\\d+)")
new_stack_re = re.compile("deal into new stack")
cut_re = re.compile("cut (-?\\d+)")

actions = []

for line in data.split("\n"):
    if new_stack_re.fullmatch(line):
        actions.append((Action.NEW_STACK, None))
    elif (match := cut_re.fullmatch(line)):
        cut = int(match.group(1))
        actions.append((Action.CUT, cut))
    elif (match := deal_re.fullmatch(line)):
        step = int(match.group(1))
        actions.append((Action.DEAL, step))
    else:
        print("No match:", line)

deck_size = 10_007
current_index = 2019

for action, argument in actions:
    match action:
        case Action.NEW_STACK:
            current_index = (-current_index - 1) % deck_size
        case Action.CUT:
            current_index = (current_index - argument) % deck_size
        case Action.DEAL:
            current_index = (current_index * argument) % deck_size

print(current_index)

actions.reverse()
deck_size   = 119_315_717_514_047
num_repeats = 101_741_582_076_661

def eea(a, b):
    old_r, r = a, b
    old_s, s = 1, 0

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    
    return old_s
    
def reverse_shuffle(current_index):
    for action, argument in actions:
        match action:
            case Action.NEW_STACK:
                current_index = (-current_index - 1) % deck_size
            case Action.CUT:
                current_index = (current_index + argument) % deck_size
            case Action.DEAL:
                current_index = (current_index * eea(argument, deck_size)) % deck_size
    return current_index

mul = 1
add = 0
for action, argument in actions:
    match action:
        case Action.CUT:
            add += argument
        case Action.NEW_STACK:
            mul *= -1
            add *= -1
            add -= 1
        case Action.DEAL:
            n = eea(argument, deck_size)
            mul *= n
            add *= n
    mul %= deck_size
    add %= deck_size

final_add = add * ((-1 % deck_size) * pow(mul, num_repeats, deck_size) + 1) * eea((1 - mul), deck_size)
final_add %= deck_size

final_mul = pow(mul, num_repeats, deck_size)

print((final_mul * 2020 + final_add) % deck_size)
