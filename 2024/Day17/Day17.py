import sys

with open(sys.argv[1], "r") as file:
    data = file.read().strip().split("\n")

class CPU:
    def __init__(self, a, b, c, memory):
        self.a = a
        self.b = b
        self.c = c
        self.mem = memory
        self.i = 0
        self.output = []
    
    def combo(self, operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case 7:
                raise ValueError("Combo operand 7")
            case _:
                raise ValueError(f"Bad combo operand {operand}")
    
    def halt(self):
        return self.i >= len(self.mem)
    
    def step(self):
        opcode = self.mem[self.i]
        operand = self.mem[self.i + 1]
        self.i += 2

        match opcode:
            case 0:
                self.a = self.a >> self.combo(operand)
            case 1:
                self.b = self.b ^ operand
            case 2:
                self.b = self.combo(operand) % 8
            case 3:
                if self.a != 0:
                    self.i = operand
            case 4:
                self.b = self.b ^ self.c
            case 5:
                self.output.append(self.combo(operand) % 8)
            case 6:
                self.b = self.a >> self.combo(operand)
            case 7:
                self.c = self.a >> self.combo(operand)
    
    def run(self):
        while not self.halt():
            self.step()
        
    def reset(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.output.clear()
        self.i = 0

data = iter(data)
a = int(next(data)[12:])
b = int(next(data)[12:])
c = int(next(data)[12:])

next(data)
memory = list(map(int, next(data)[9:].split(",")))

computer = CPU(a, b, c, memory)
computer.run()
print(",".join(map(str, computer.output)))

def check(*args):
    a = 0
    for i in args:
        a <<= 3
        a |= i
    
    if len(args) == 16:
        print(a)
        exit()
    
    target_length = len(args) + 1
    for na in range(8):
        computer.reset(a << 3 | na, b, c)
        computer.run()
        if computer.output == memory[-target_length:]:
            check(*args, na)

check()