from typing import Any, Self

# Created for 2019 Day 17
class Maze:
    def __init__(self, maze: list[list[Any]]):
        self.maze: list[list[Any]] = maze
        self.width: int = len(maze[0])
        self.height: int = len(maze)
    
    def __getitem__(self, index: tuple[int, int]) -> Any:
        if len(index) != 2:
            raise ValueError("Index must be a two-length list or tuple")
        x, y = index
        if not(0 <= x < self.width and 0 <= y < self.height):
            return False
        return self.maze[y][x]

    def __contains__(self, index: tuple[int, int]) -> bool:
        if len(index) != 2:
            raise ValueError("Index must be a two-length list or tuple")
        x, y = index
        return 0 <= x < self.width and 0 <= y < self.height

class DjikstraMaze(Maze):
    def __init__(self, maze: list[list[Any]]):
        super().__init__(maze)
        self._costs: list[list[int]] = [[float("inf") for _ in range(self.width)] for _ in range(self.height)]
    
    def __copy__(self):
        return DjikstraMaze(self.maze)
    
    def set_cost(self, index: tuple[int, int], cost: int):
        if len(index) != 2:
            raise ValueError("Index must be a two-length list or tuple")
        x, y = index
        if not(0 <= x < self.width and 0 <= y < self.height):
            return IndexError("Index is not inside the maze")
        self._costs[y][x] = cost
    
    def get_cost(self, index: tuple[int, int]) -> int:
        if len(index) != 2:
            raise ValueError("Index must be a two-length list or tuple")
        x, y = index
        if not(0 <= x < self.width and 0 <= y < self.height):
            return float("inf")
        return self._costs[y][x]

    def visited(self, index: tuple[int, int]) -> bool:
        return self.get_cost(index) != float("inf")

class MazeBuilder:
    def __init__(self):
        self.maze = []
        self._djikstras = False
    
    def new_line(self):
        self.maze.append([])
    
    def add_value(self, value: Any):
        self.maze[-1].append(value)
    
    def __setitem__(self, index: tuple[int, int], value: Any):
        if len(index) != 2:
            raise ValueError("Index must be a two-length list or tuple")
        x, y = index
        self.maze[y][x] = value
    
    def __getitem__(self, index: tuple[int, int]) -> Any:
        if len(index) != 2:
            raise ValueError("Index must be a two-length list or tuple")
        x, y = index
        return self.maze[y][x]

    def djikstras(self) -> Self:
        self._djikstras = True
        return self
    
    def finish(self) -> Maze | DjikstraMaze:
        while len(self.maze[-1]) == 0:
            self.maze.pop(-1)
        if self._djikstras:
            return DjikstraMaze(self.maze)
        else:
            return Maze(self.maze)