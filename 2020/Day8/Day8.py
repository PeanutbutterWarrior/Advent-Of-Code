with open('Day8.txt', 'r') as file:
    data = file.read().split('\n')


def execute_program(override=(-1, None)):
    instruction_counter = 0
    accumulator = 0
    visited = [False] * len(data)

    try:
        while not visited[instruction_counter]:
            visited[instruction_counter] = True
            cmd, arg = data[instruction_counter].split(' ')
            if override[0] == instruction_counter:
                cmd = override[1]
            if cmd == 'jmp':
                instruction_counter += int(arg)
            else:
                if cmd == 'acc':
                    accumulator += int(arg)
                instruction_counter += 1
        return accumulator, False
    except IndexError:
        return accumulator, True


# Part 1

print(execute_program()[0])

# Part 2
jumps = [1, 4, 125, 573, 348, 269, 532, 155, 300, 303, 388, 354, 398, 318, 38, 198, 328, 459, 253, 221, 204, 18, 19,
         478, 96, 118, 119, 525, 44, 75, 591, 145, 180, 47, 61, 426, 281, 207, 133, 539, 540, 64, 240, 263, 341, 276,
         420, 81, 523, 585, 451, 245, 465, 231, 382, 314, 166, 367, 360, 492, 194, 325, 216, 400, 445, 505, 487, 405,
         99, 190, 289, 291, 374]

for jump in jumps:
    out, finished = execute_program((jump, 'nop'))
    if finished:
        print(out, jump)
        break
