import sys
from collections import deque
import re

with open(sys.argv[1], "r") as file:
    data = file.read().strip("\n")

deal_re = re.compile("deal with increment (\\d+)")
new_stack_re = re.compile("deal into new stack")
cut_re = re.compile("cut (-?\\d+)")

deck_size = 10_007
deck = deque(range(deck_size))
new_deck = [None] * deck_size

for line in data.split("\n"):
    if new_stack_re.fullmatch(line):
        deck.reverse()
    elif (match := cut_re.fullmatch(line)):
        cut = int(match.group(1))
        deck.rotate(-cut)
    elif (match := deal_re.fullmatch(line)):
        step = int(match.group(1))
        index = 0
        while True:
            new_deck[index] = deck.popleft()
            index = (index + step) % deck_size
            if index == 0:
                break
        deck = deque(new_deck)
    else:
        print("No match:", line)
print(deck.index(2019))