import sys
from Intcode import AsciiIntcode

with open(sys.argv[1], "r") as file:
    data = file.read().strip("\n")

interp = AsciiIntcode(AsciiIntcode.parse_input(data))

# hologram
# cake
# coin
# hypercube

while True:
    print(interp.run()[0], end="")
    interp.give_input(input())