with open("Day1.txt", "r") as file:
    data = file.read()

calories = []
for elf in data.split("\n\n"):
    total = 0
    for item in elf.split():
        total += int(item)
    calories.append(total)
calories.sort(reverse=True)

print(calories[0])
print(calories[0] + calories[1] + calories[2])