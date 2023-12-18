with open("Day24.txt", "r") as file:
    data = file.read()


# 26**6 26**5 0 0 26**4 0 0 26**3 0 26**2 26 0 0 1
#   0     0   3 9   5   8 5   0   5   4    0 4 0 0

#           |            |
inp = iter('00395850540400')

v = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

for line in data.split('\n'):
    if not line:
        continue
    instr, *args = line.split()
    if instr == 'inp':
        v[args[0]] = int(next(inp))
    elif instr == 'add':
        if args[1] in v:
            a = v[args[1]]
        else:
            a = int(args[1])
        v[args[0]] += a
    elif instr == 'mul':
        if args[1] in v:
            a = v[args[1]]
        else:
            a = int(args[1])
        v[args[0]] *= a
    elif instr == 'div':
        if args[1] in v:
            a = v[args[1]]
        else:
            a = int(args[1])
        v[args[0]] //= a
    elif instr == 'mod':
        if args[1] in v:
            a = v[args[1]]
        else:
            a = int(args[1])
        v[args[0]] %= a
    elif instr == 'eql':
        if args[1] in v:
            a = v[args[1]]
        else:
            a = int(args[1])
        v[args[0]] = int(v[args[0]] == a)

print(v)