from enum import Enum
import itertools

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
    9: (1, 0),
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
    RBASE = 9

class Mode(Enum):    
    POS = 0
    IMM = 1
    REL = 2

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
        self.rbase: int = 0
        
        self.waiting_for_input: bool = False
        self.running: bool = False
    
    def get(self, index):
        if index < 0:
            raise ValueError("Attempt to read from negative index")
        if index >= len(self.memory):
            self.memory.extend(itertools.repeat(0, index - len(self.memory) + 1))
        return self.memory[index]

    def set(self, index, value):
        if index < 0:
            raise ValueError("Attempt to write to negative index")
        if index >= len(self.memory):
            self.memory.extend(itertools.repeat(0, index - len(self.memory) + 1))
        self.memory[index] = value
    
    def read_instr(self) -> tuple[Opcode, ModeList]:
        instr = self.get(self.ip)
        self.ip += 1

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
            out.append(self.read_value(self.ip, next(modes)))
            self.ip += 1
        
        for _ in range(opcode.num_out):
            out.append(self.read_addr(self.ip, next(modes)))
            self.ip += 1
        
        return tuple(out)

    def read_value(self, index: int, mode: Mode) -> int:
        val = self.get(index)
        match mode:
            case Mode.POS:
                return self.get(val)
            case Mode.IMM:
                return val
            case Mode.REL:
                return self.get(val + self.rbase)
            case _:
                raise ValueError(f"Unknown reading Mode {mode}")
        
    def read_addr(self, index: int, mode: Mode) -> int:
        val = self.get(index)
        match mode:
            case Mode.POS:
                return val
            case Mode.IMM:
                raise ValueError("Cannot read address in immediate mode")
            case Mode.REL:
                return val + self.rbase
            case _:
                raise ValueError(f"Unknown reading Mode {mode}")
    
    def step(self):
        opcode, modes = self.read_instr()
        args = self.read_args(opcode, modes)
        match opcode:
                case Opcode.ADD:
                    self.set(args[2], args[0] + args[1])
                case Opcode.MUL:
                    self.set(args[2], args[0] * args[1])
                case Opcode.HALT:
                    self.running = False
                case Opcode.IN:
                    if self.input_pointer  < len(self.inputs):
                        value = self.inputs[self.input_pointer]
                        self.input_pointer += 1
                        self.set(args[0], value)
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
                    self.set(args[2], 1 if args[0] < args[1] else 0)
                case Opcode.EQ:
                    self.set(args[2], 1 if args[0] == args[1] else 0)
                case Opcode.RBASE:
                    self.rbase += args[0]
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
