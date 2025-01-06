import sys
from Intcode import Intcode

with open(sys.argv[1], "r") as file:
    data = file.read().strip("\n")

program = Intcode.parse_input(data)

computers = [Intcode(program.copy(), [i]) for i in range(50)]

has_output_part1 = False
nat = None
last_release = None

while True:
    num_idle = 0

    for index, computer in enumerate(computers):
        is_idle = False
        if computer.waiting_for_input:
            computer.give_input(-1)
            is_idle = True
        
        output = computer.run()
        if len(output) > 0:
            is_idle = False
        
        for i in range(0, len(output), 3):
            address, x, y = output[i:i + 3]
            if address == 255:
                if not has_output_part1:
                    print(y)
                    has_output_part1 = True
                
                nat = (x, y)
            else:
                computers[address].give_input(x)
                computers[address].give_input(y)
        
        if is_idle:
            num_idle += 1
    
    if num_idle == 50:
        x, y = nat
        if y == last_release:
            print(y)
            break
        computers[0].give_input(x)
        computers[0].give_input(y)
        last_release = y