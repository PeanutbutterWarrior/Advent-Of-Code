import enum
from typing import Self

# First used in 2024 Day 16
class Dir(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def right(self) -> Self:
        return Dir((self.value + 1) % 4)
    
    def left(self) -> Self:
        return Dir((self.value - 1 % 4))
    
    def behind(self) -> Self:
        return Dir((self.value + 2) % 4)
    
    def dxy(self) -> tuple[int, int]:
        match self:
            case Dir.NORTH:
                return (0, -1)
            case Dir.EAST:
                return (1, 0)
            case Dir.SOUTH:
                return (0, 1)
            case Dir.WEST:
                return (-1, 0)
    
    def __add__(self, other):
        if len(other) == 2:
            other = iter(other)
            dx, dy = self.dxy()
            return (other[0] + dx, other[1] + dy)
        
        raise NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)