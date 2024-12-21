import sys
import math

def intlen(x):
    return math.floor(math.log10(x) + 1)

class StoneIterator:
    def __init__(self, stone):
        self.stone = stone
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.stone is None:
            raise StopIteration
        value = self.stone
        self.stone = self.stone.next
        return value

class Stone:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        s = str(self.value)
        if self.next is not None:   
            s += " -> "
            s += str(self.next)
        return s
    
    def __add__(self, other):
        if type(other) == int:
            return self.value + other
        elif type(other) == Stone:
            return self.value + other.value
        raise NotImplemented

    def __iter__(self):
        return StoneIterator(self)

    def __len__(self):
        l = 1
        c = self.next
        while c is not None:
            l += 1
            c = c.next
        return l

    def update(self):
        if self.value == 0:
            self.value = 1
        elif (length := intlen(self.value)) % 2 == 0:
            offset = 10**(length//2)

            new_stone = Stone(self.value % offset)
            new_stone.next = self.next

            self.value = self.value // offset
            self.next = new_stone
        else:
            self.value *= 2024


with open(sys.argv[1], "r") as file:
    data = map(int, file.read().strip().split(" "))

head = Stone(next(data))
prev = head
for item in data:   
    prev.next = Stone(item)
    prev = prev.next

for i in range(25):
    for stone in head:
        stone.update()
print(len(head))