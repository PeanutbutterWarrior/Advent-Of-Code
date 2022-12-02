with open("Day6.txt", "r") as file:
    data = file.read()

fish = []
for i in data.split(','):
    fish.append(int(i))

for _ in range(80):
    for ind in range(len(fish)):
        if fish[ind] == 0:
            fish[ind] = 6
            fish.append(8)
        else:
            fish[ind] -= 1

print(len(fish))

fish = [0] * 9
for i in data.split(','):
    fish[int(i)] += 1

for _ in range(256):
    new_fish = fish.pop(0)
    fish[6] += new_fish
    fish.append(new_fish)

print(sum(fish))