import sys
from Intcode import Intcode
from Utilities import Dir, MazeBuilder
from collections import defaultdict

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

interp = Intcode(Intcode.parse_input(data))
view = interp.run()

maze = MazeBuilder()
position = None
facing = None
x = 0
y = 0
for char in view:
    char = char
    if char == 10: # \n
        maze.new_line()
        y += 1
        x = -1 # To account for the x += 1 at end of loop
    elif char == 35:
        maze.add_value(True)
    else:
        maze.add_value(False)
    
    if char == 94: # ^
        position = (x, y)
        facing = Dir.NORTH
    elif char == 60: # <
        position = (x, y)
        facing = Dir.WEST
    elif char == 62: # >
        position = (x, y)
        facing = Dir.EAST
    elif char == 118: # >
        position = (x, y)
        facing = Dir.SOUTH
    x += 1

maze = maze.finish()

total = 0
for y in range(1, maze.height - 1):
    for x in range(1, maze.width - 1):
        if maze[x, y] and all(maze[x + dx, y + dy] for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0))):
            total += x * y
print(total)

full_instructions = []
forward_count = 0
while True:
    if maze[position + facing]:
        forward_count += 1
        position += facing
    else:
        if forward_count > 0:
            full_instructions.append(forward_count)
            forward_count = 0
    
        if maze[position + facing.left]:
            full_instructions.append("L")
            facing = facing.left
        elif maze[position + facing.right]:
            full_instructions.append("R")
            facing = facing.right
        else:
            # Nowhere to go
            break

def encode(char):
    if type(char) == str:
        return char
    return chr(char + 96)

full_instructions = "".join(map(str, full_instructions))

substr_counts = defaultdict(int)
for start in range(len(full_instructions)):
    for length in range(1, 11):
        substr_counts[full_instructions[start: start + length]] += 1

scored_substr = {k: len(k) * v**2 for k, v in substr_counts.items()}

best_substr = sorted(scored_substr, key=scored_substr.get, reverse=True)

def find_solution():
    for a in best_substr:
        for b in best_substr:
            for c in best_substr:
                if a in b or b in a or a in c or c in a or b in c or c in b:
                    continue
                main_program = full_instructions.replace(a, "A").replace(b, "B").replace(c, "C")
                if len(main_program) > 20:
                    continue
                if len(set(main_program)) > 3:
                    continue
                return a, b, c, main_program

a, b, c, main_program = find_solution()

robot_input = []

for program in (main_program, a, b, c):
    subprogram_input = []
    for char in program:
        if char in "LR":
            subprogram_input.append(44) # ,

        subprogram_input.append(ord(char))

        if char in "LRABC":
            subprogram_input.append(44) # ,
    if subprogram_input[0] == 44:
        subprogram_input = subprogram_input[1:]
    if subprogram_input[-1] == 44:
        subprogram_input.pop(-1)
    subprogram_input.append(10) # \n
    robot_input += subprogram_input

robot_input.append(ord("n"))
robot_input.append(10)

for char in robot_input:
    print(chr(char), end="")

program = Intcode.parse_input(data)
program[0] = 2
interp = Intcode(program, robot_input)
print(interp.run()[-1])