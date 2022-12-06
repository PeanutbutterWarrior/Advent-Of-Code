from itertools import product

class Grid:
    def __init__(self, rules, grid):
        self.grid = list(map(list, grid.split()))
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.rules = rules
        self.outside = '0'

    def enhance(self):
        self.expand()
        new_grid = []
        for y in range(self.height):
            new_grid.append([])
            for x in range(self.width):
                new_char_index = ''.join(self.get(x + dx, y + dy) for dy, dx in product([-1, 0, 1], [-1, 0, 1]))
                new_grid[-1].append(self.rules[int(new_char_index, 2)])
        self.grid = new_grid

        self.outside = self.rules[int(self.outside * 9, 2)]

    def expand(self):
        self.width += 2
        self.height += 2
        for line in self.grid:
            line.insert(0, self.outside)
            line.append(self.outside)
        self.grid.insert(0, [self.outside] * self.width)
        self.grid.append([self.outside] * self.width)

    def get(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return self.outside
        return self.grid[y][x]

    def count(self):
        count = 0
        for line in self.grid:
            for char in line:
                if char == '1':
                    count += 1
        return count


with open("Day20.txt", "r") as file:
    data = file.read().replace('.', '0').replace('#', '1')

grid = Grid(*data.split('\n\n'))
grid.enhance()
grid.enhance()
print(grid.count())

for _ in range(48):
    grid.enhance()
print(grid.count())