import sys
from Intcode import AsciiIntcode

with open(sys.argv[1], "r") as file:
    data = file.read().strip("\n")

program = AsciiIntcode.parse_input(data)
interp = AsciiIntcode(program.copy())

code = """NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J"""
interp.run()
interp.give_input(code)
interp.give_input("WALK")

text, result = interp.run()
if result is None:
    print(text)
else:
    print(result)


interp = AsciiIntcode(program.copy())
code = """NOT A J
NOT T T
AND B T
AND C T
NOT T T
AND D T
AND H T
OR T J""" # t = 0

interp.run()
interp.give_input(code)
interp.give_input("RUN")
text, result = interp.run()
if result is None:
    print(text)
else:
    print(result)