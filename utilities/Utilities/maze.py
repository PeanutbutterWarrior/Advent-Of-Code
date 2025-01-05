from typing import Any

# Created for 2019 Day 17
class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.width = len(maze[0])
        self.height = len(maze)
    
    def __getitem__(self, index: tuple[int, int]) -> Any:
        if len(index) != 2:
            raise ValueError("Index must be a two-length list or tuple")
        x, y = index
        if not(0 <= x < self.width and 0 <= y < self.height):
            return False
        return self.maze[y][x]

class MazeBuilder:
    def __init__(self):
        self.maze = []
    
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
    
    def finish(self) -> Maze:
        while len(self.maze[-1]) == 0:
            self.maze.pop(-1)
        return Maze(self.maze)