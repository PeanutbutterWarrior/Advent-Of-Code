import sys
from Intcode import Intcode

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

program = Intcode.parse_input(data)
interp = Intcode(program.copy(), [1])
print(interp.run()[-1])

interp = Intcode(program.copy(), [2])
print(interp.run()[-1])