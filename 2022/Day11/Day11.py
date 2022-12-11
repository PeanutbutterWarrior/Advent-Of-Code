import re


class Monkey:
    def __init__(self, items, operation, test, on_true, on_false):
        self.items = items
        self.operation = operation
        self.modulus = test
        self.on_true = on_true
        self.on_false = on_false
        self.inspection_count = 0

    def take_turn(self):
        success = []
        failed = []
        for item in self.items:
            self.inspection_count += 1
            stress = self.operation(item)
            # stress //= 3  # First part
            stress %= 9699690
            if stress % self.modulus == 0:
                success.append(stress)
            else:
                failed.append(stress)
        self.items.clear()
        return (self.on_true, success), (self.on_false, failed)


with open("Day11.txt", "r") as file:
    data = file.read()

monkeys = []
for monkey in data.split('\n\n'):
    lines = iter(monkey.split('\n'))
    next(lines)
    items = list(map(int, re.findall('\d+', next(lines))))
    operation = re.match('  Operation: new = (.+)$', next(lines)).group(1)
    func = eval('lambda old: ' + operation)
    test = int(re.match('  Test: divisible by (\d+)', next(lines)).group(1))
    on_true = int(re.match('    If true: throw to monkey (\d+)', next(lines)).group(1))
    on_false = int(re.match('    If false: throw to monkey (\d+)', next(lines)).group(1))
    monkeys.append(Monkey(items, func, test, on_true, on_false))

for turn in range(10000):
    for monkey in monkeys:
        m1, m2 = monkey.take_turn()
        monkeys[m1[0]].items.extend(m1[1])
        monkeys[m2[0]].items.extend(m2[1])

m1, m2 = sorted(map(lambda i: i.inspection_count, monkeys), reverse=True)[:2]
print(m1 * m2)