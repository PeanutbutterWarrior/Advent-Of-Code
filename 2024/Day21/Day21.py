import sys
from functools import cache

numpad_button_pos = {"7": (0, 0), "8": (1, 0), "9": (2, 0), "4": (0, 1), "5": (1, 1), "6": (2, 1), "1": (0, 2), "2": (1, 2), "3": (2, 2), "0": (1, 3), "A": (2, 3)}
keypad_button_pos = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}

@cache
def numpad_path(current, next):
    x1, y1, x2, y2 = *numpad_button_pos[current], *numpad_button_pos[next]
    dx, dy = shortest_path_safe(x1, y1, x2, y2)

    if x1 == 0 and y2 == 3:
        return (dx + dy + "A",)
    
    if y1 == 3 and x2 == 0:
        return (dy + dx + "A",)
    
    return dx + dy + "A", dy + dx + "A"
    

def shortest_path_safe(x1, y1, x2, y2):
    vertical = ""
    if y2 < y1:
        vertical = "^" * abs(y2 - y1)
    elif y2 > y1:
        vertical = "v" * abs(y2 - y1)

    horizontal = ""
    if x2 > x1:
        horizontal = ">" * abs(x2 - x1)
    elif x2 < x1:
        horizontal = "<" * abs(x2 - x1)
    return horizontal, vertical

@cache
def keypad_path(current, next):
    x1, y1 = keypad_button_pos[current]
    x2, y2 = keypad_button_pos[next]
    dx, dy = shortest_path_safe(x1, y1, x2, y2)

    if x1 == 0 and y2 == 0:
        return (dx + dy + "A", )
    if y1 == 0 and x2 == 0:
        return (dy + dx +"A", )
    return dx + dy + "A", dy + dx + "A"

@cache
def shortest_path_for_robot(robot_num, start, end):
    if robot_num == 1:
        key_options = numpad_path(start, end)
    else:
        key_options = keypad_path(start, end)
    
    if robot_num == final_robot_num:
        return len(key_options[0])
    if len(key_options) == 1:
        return shortest_path_for_robot_seq(robot_num + 1, key_options[0])
    
    a = shortest_path_for_robot_seq(robot_num + 1, key_options[0])
    b = shortest_path_for_robot_seq(robot_num + 1, key_options[1])

    return min(a, b)

def shortest_path_for_robot_seq(robot_num, seq):
    return sum(shortest_path_for_robot(robot_num, prev, next) for prev, next in zip("A" + seq, seq))

with open(sys.argv[1], "r") as file:
    data = file.read().strip()


final_robot_num = 3


total = 0
for line in data.split("\n"):
    seq = shortest_path_for_robot_seq(1, line)
    total += int(line[:-1]) * seq
print(total)


shortest_path_for_robot.cache_clear()
final_robot_num = 26

total = 0
for ind, line in enumerate(data.split("\n")):
    seq = shortest_path_for_robot_seq(1, line)
    total += int(line[:-1]) * seq
print(total)