import sys

class Intcode:
    def __init__(self, program):
        self.memory = program
        self.ip = 0
    
    def read_instr(self):
        self.ip += 1
        return self.read(self.ip - 1)

    def read_args(self):
        self.ip += 3
        return self.read(self.ip - 3), self.read(self.ip - 2), self.read(self.ip - 1)

    def read(self, index):
        return self.memory[index]

    def write(self, index, value):
        self.memory[index] = value

    def run(self):
        while True:
            match self.read_instr():
                case 1:
                    a, b, target = self.read_args()
                    self.write(target, self.read(a) + self.read(b))
                case 2:
                    a, b, target = self.read_args()
                    self.write(target, self.read(a) * self.read(b))
                case 99:
                    break


with open(sys.argv[1], "r") as file:
    data = file.read().strip()

data = list(map(int, data.split(",")))
data[1] = 12
data[2] = 2
interp = Intcode(data.copy())
interp.run()
print(interp.read(0))

for noun in range(99):
    for verb in range(99):
        data[1] = noun
        data[2] = verb
        interp = Intcode(data.copy())
        interp.run()
        if interp.read(0) == 19690720:
            print(100 * noun + verb)
            break