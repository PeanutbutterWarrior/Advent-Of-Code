with open('Day8.txt', 'r') as file:
    data = file.read().split('\n')


def execute_program(override=(-1, None)):
    instruction_counter = 0
    accumulator = 0
    visited = [False] * len(data)

    while not visited[instruction_counter]:
        visited[instruction_counter] = True
        cmd, arg = data[instruction_counter].split(' ')
        if cmd == 'jmp':
            instruction_counter += int(arg)
        else:
            if cmd == 'acc':
                accumulator += int(arg)
            instruction_counter += 1
    return accumulator


# Part 1

print(execute_program())
