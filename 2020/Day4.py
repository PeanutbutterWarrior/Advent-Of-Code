import re

with open('Day4.txt', 'r') as file:
    data = file.read().split('\n')

# Part 1

correct_passports = 0
passport = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
for line in data:
    if line:
        for field in line.split():
            key, val = field.split(':')
            passport[key] = True
    else:
        if False not in passport.values():
            correct_passports += 1
        passport = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
print(correct_passports)

