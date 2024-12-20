with open("input.txt", "r") as file:
    data = file.read()

list1 = []
list2 = []
for line in data.split("\n"):
    a, b = line.split("   ")
    list1.append(int(a))
    list2.append(int(b))

diff = 0
for i, j in zip(sorted(list1), sorted(list2)):
    diff += abs(i - j)

print(diff)

reps = {}
for i in list2:
    reps[i] = reps.get(i, 0) + 1

sim = 0
for i in list1:
    sim += i * reps.get(i, 0)

print(sim)