from heapq import *
from itertools import count

class PriorityQueue[T]:
    def __init__(self):
        self._q: list[tuple[int, int, T]] = []
        self._counter: count = count()
    
    def __bool__(self):
        return len(self._q) > 0
    
    def push(self, cost: int, item: T):
        heappush(self._q, (cost, next(self._counter), item))
    
    def pop(self) -> tuple[int, T]:
        cost, _, item = heappop(self._q)
        return (cost, item)