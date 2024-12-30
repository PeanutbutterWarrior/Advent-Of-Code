numpad_button_pos = {"7": (0, 0), "8": (1, 0), "9": (2, 0), "4": (0, 1), "5": (1, 1), "6": (2, 1), "1": (0, 2), "2": (1, 2), "3": (2, 2), "0": (1, 3), "A": (2, 3), ".": (0, 3)}
keypad_button_pos = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1), ".": (0, 0)}

numpad_button_pos_r = {v: k for k, v in numpad_button_pos.items()}
keypad_button_pos_r = {v: k for k, v in keypad_button_pos.items()}

dir_to_dxy = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

class Robot:
    def __init__(self, is_numpad, next, num):
        self.numpad = is_numpad
        self.buttons = []
        self.next = next
        self.target = "A"
        self.num = num
        self.count = 0
    
    def press(self, key):
        self.count += 1
        if key == "A":
            self.buttons.append(self.target)
            if not self.numpad:
                self.next.press(self.target)
            return
        dx, dy = dir_to_dxy[key]
        if self.numpad:
            x, y = numpad_button_pos[self.target]
            self.target = numpad_button_pos_r[(x + dx, y + dy)]
        else:
            x, y = keypad_button_pos[self.target]
            self.target = keypad_button_pos_r[(x + dx, y + dy)]
        if self.target == ".":
            print(f"Robot {self.num} pointing at blank space after {self.count} instructions")

r1 = Robot(True, None, 1)
r2 = Robot(False, r1, 2)
r3 = Robot(False, r2, 3)

input = "<vA<AA>>^AAvA<^A>AAvA^A<vA>^A<A>A<vA>^A<A>A<vA<A>>^AA<A>vA^A"
for char in input:
    r3.press(char)

print(input)
print("".join(r3.buttons))
print("".join(r2.buttons))
print("".join(r1.buttons))