from enum import Enum

opcode_data = {
    99: (0, 0),
    1: (2, 1),
    2: (2, 1),
    3: (0, 1),
    4: (1, 0),
    5: (2, 0),
    6: (2, 0),
    7: (2, 1),
    8: (2, 1),
}

class Opcode(Enum):
    def __init__(self, value):
        self.num_in, self.num_out = opcode_data[value]
    
    HALT = 99
    ADD = 1
    MUL = 2
    IN = 3
    OUT = 4
    JNZ = 5
    JZ = 6
    LT = 7
    EQ = 8

class Mode(Enum):
    @property
    def indirected(self):
        match self:
            case Mode.IMM:
                return Mode.POS
            case _:
                raise ValueError(f"Cannot indirect {self}")
    
    @property
    def directed(self):
        match self:
            case Mode.POS:
                return Mode.IMM
            case _:
                raise ValueError(f"Cannot direct {self}")
    
    POS = 0
    IMM = 1

type ModeList = tuple[Mode, ...]

class Intcode:
    @staticmethod
    def parse_input(inp):
        return list(map(int, inp.split(",")))
    
    def __init__(self, program, inputs):
        self.memory: list[int] = program
        self.inputs: list[int] = inputs
        self.output: list[int] = []

        self.ip: int = 0
        self.input_pointer: int = 0
        
        self.waiting_for_input: bool = False
        self.running: bool = False
    
    def read_instr(self) -> tuple[Opcode, ModeList]:
        self.ip += 1
        instr = self.memory[self.ip - 1]

        op = Opcode(instr % 100)
        instr //= 100
        
        modes = []
        while instr > 0:
            modes.append(Mode(instr % 10))
            instr //= 10
        
        for _ in range(op.num_in + op.num_out - len(modes)):
            modes.append(Mode(0))
        
        return op, tuple(modes)

    def read_args(self, opcode: Opcode, modes: ModeList) -> tuple[int, ...]:
        out = []
        modes = iter(modes)
        for _ in range(opcode.num_in):
            out.append(self.read(self.ip, next(modes)))
            self.ip += 1
        
        for _ in range(opcode.num_out):
            out.append(self.read(self.ip, next(modes).directed))
            self.ip += 1
        
        return tuple(out)

    def read(self, index: int, mode: Mode):
        val = self.memory[index]
        match mode:
            case Mode.POS:
                return self.memory[val]
            case Mode.IMM:
                return val
            case _:
                raise ValueError(f"Unknown reading Mode {mode}")

    def write(self, index, value):
        self.memory[index] = value
    
    def step(self):
        opcode, modes = self.read_instr()
        args = self.read_args(opcode, modes)
        match opcode:
                case Opcode.ADD:
                    self.write(args[2], args[0] + args[1])
                case Opcode.MUL:
                    self.write(args[2], args[0] * args[1])
                case Opcode.HALT:
                    self.running = False
                case Opcode.IN:
                    if self.input_pointer  < len(self.inputs):
                        value = self.inputs[self.input_pointer]
                        self.input_pointer += 1
                        self.write(args[0], value)
                    else:
                        self.waiting_for_input = True
                        self.ip -= 2
                case Opcode.OUT:
                    self.output.append(args[0])
                case Opcode.JNZ:
                    if args[0]:
                        self.ip = args[1]
                case Opcode.JZ:
                    if not args[0]:
                        self.ip = args[1]
                case Opcode.LT:
                    self.write(args[2], 1 if args[0] < args[1] else 0)
                case Opcode.EQ:
                    self.write(args[2], 1 if args[0] == args[1] else 0)
                case _:
                    raise ValueError(f"Unknown opcode {opcode}")

    def run(self):
        self.running = True
        while self.running and not self.waiting_for_input:
            self.step()
        return self.output

    def give_input(self, value):
        self.inputs.append(value)
        self.waiting_for_input = False