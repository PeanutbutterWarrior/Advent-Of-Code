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

# Part 2

correct_passports = 0
passport = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
for line in data:
    if line:
        for field in line.split():
            key, val = field.split(':')
            if key == 'byr':
                if len(val) == 4 and 1920 <= int(val) <= 2002:
                    passport[key] = True
            elif key == 'iyr':
                if len(val) == 4 and 2010 <= int(val) <= 2020:
                    passport[key] = True
            elif key == 'eyr':
                if len(val) == 4 and 2020 <= int(val) <= 2030:
                    passport[key] = True
            elif key == 'hgt':
                unit = val[-2:]
                if unit not in {'cm', 'in'}:
                    continue
                height = int(val[:-2])
                if unit == 'cm' and 150 <= height <= 193:
                    passport[key] = True
                elif unit == 'in' and 59 <= height <= 76:
                    passport[key] = True
            elif key == 'hcl':
                if re.fullmatch('#[0-9a-f]{6}', val) is not None:
                    passport[key] = True
            elif key == 'ecl':
                if val in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                    passport[key] = True
            elif key == 'pid':
                if val.isnumeric() and len(val) == 9:
                    passport[key] = True
    else:
        if False not in passport.values():
            correct_passports += 1
        passport = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
print(correct_passports)
