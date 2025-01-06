import sys
from Utilities import Dir, MazeBuilder, PriorityQueue
from collections import defaultdict
from copy import copy

with open(sys.argv[1], "r") as file:
    data = file.read().strip("\n")

data = list(data.split("\n"))
maze = MazeBuilder()
portal_pairs = defaultdict(list)

for y in range(2, len(data) - 2):
    line = data[y]
    maze.new_line()
    for x in range(2, len(line) - 2):
        char = line[x]
        if char == ".":
            maze.add_value(True)
            pos = (x, y)
            for dir in Dir:
                nx, ny = pos + dir
                if (l1 := data[ny][nx]) not in " .#":
                    nnx, nny = (nx, ny) + dir
                    l2 = data[nny][nnx]
                    match dir:
                        case Dir.NORTH | Dir.WEST:
                            portal_pairs[l2 + l1].append((x - 2, y - 2))
                        case Dir.SOUTH | Dir.EAST:
                            portal_pairs[l1 + l2].append((x - 2, y - 2))
        else:
            maze.add_value(False)
maze = maze.djikstras().finish()

start = portal_pairs.pop("AA")[0]
end = portal_pairs.pop("ZZ")[0]
portals = {}
outer_portals = set()
for a, b in portal_pairs.values():
    portals[a] = b
    portals[b] = a

    if a[0] == 0 or a[1] == 0 or a[0] == maze.width - 1 or a[1] == maze.height - 1:
        outer_portals.add(a)
    else:
        outer_portals.add(b)

q = PriorityQueue()
q.push(0, start)
while q:
    cost, pos = q.pop()
    maze.set_cost(pos, cost)
    if pos == end:
        break
    for dir in Dir:
        new_pos = pos + dir
        if maze[new_pos] and not maze.visited(new_pos):
            q.push(cost + 1, new_pos)
    if pos in portals and not maze.visited(portals[pos]):
        q.push(cost + 1, portals[pos])

print(maze.get_cost(end))

mazes = [copy(maze)]
q = PriorityQueue()
q.push(0, (start, 0))

while q:
    cost, (pos, depth) = q.pop()
    mazes[depth].set_cost(pos, cost)
    if pos == end and depth == 0:
        break
    for dir in Dir:
        new_pos = pos + dir
        if mazes[depth][new_pos] and not mazes[depth].visited(new_pos):
            q.push(cost + 1, (new_pos, depth))
    if pos in portals and not mazes[depth].visited(portals[pos]):
        if pos in outer_portals:
            depth -= 1
        else:
            depth += 1
            if len(mazes) == depth:
                mazes.append(copy(maze))
        q.push(cost + 1, (portals[pos], depth))
print(mazes[0].get_cost(end))