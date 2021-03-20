import re

with open('Day19.txt') as file:
    data = file.read().split('\n')


rule_pattern = re.compile('(\d+): (.*)')

iterator = iter(data)

rules = {}

for line in iterator:
    if not line:
        break
    number, rule = re.fullmatch(rule_pattern, line).groups()
    number = int(number)
    rule = rule.split()
    if not rule[0].isdigit():
        sub_rules = rule[0][1]
    else:
        sub_rules = [[]]
        for item in rule:
            if item == '|':
                sub_rules.append([])
            else:
                sub_rules[-1].append(int(item))
        sub_rules = tuple(map(tuple, sub_rules))
    rules[number] = sub_rules

messages = [i for i in iterator]

class FailedMatchError(Exception):
    pass


def match_rule(string, rule_num, start_ind=0):
    possible_rules = rules[rule_num]
    for rule in possible_rules:
        if type(rule) == str:
            if string[start_ind] == rule:
                return start_ind + 1
            else:
                raise FailedMatchError
        else:
            backup_ind = start_ind
            for item in rule:
                try:
                    start_ind = match_rule(string, item, start_ind)
                except FailedMatchError:
                    start_ind = backup_ind
                    break
            else:
                break
    else:
        raise FailedMatchError
    return start_ind


# Part 1

count = 0
for message in messages:
    try:
        if match_rule(message, 0) != len(message):
            raise FailedMatchError
        count += 1
    except FailedMatchError:
        pass
print(count)
