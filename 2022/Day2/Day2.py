import enum

with open("Day2.txt", "r") as file:
    data = file.read()

matches = []
for line in data.split("\n"):
    if not line:
        continue

    other, own = line.split()
    matches.append(
        (
            ord(other) - ord("A"),
            ord(own) - ord("X")
        )
    )

total_score = 0
for other, own in matches:
    if (other + 1) % 3 == own:
        total_score += 6
    elif other == own:
        total_score += 3
    total_score += own + 1
print(total_score)

total_score = 0
for other, aim in matches:
    aim -= 1
    own = (other + aim) % 3

    total_score += (aim + 1) * 3
    total_score += own + 1
print(total_score)