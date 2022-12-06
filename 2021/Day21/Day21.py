from itertools import cycle, product
from collections import Counter
from functools import cache

with open("Day21.txt", "r") as file:
    data = file.read()

p1, p2 = data.split('\n')
p1_start = int(p1[-1])
p2_start = int(p2[-1])
p1 = p1_start
p2 = p2_start
p1_score = 0
p2_score = 0

dice = cycle(range(1, 101))
num_rolls = 0

while p2_score < 1000:
    p1 += next(dice) + next(dice) + next(dice)
    num_rolls += 3
    p1 = (p1 - 1) % 10 + 1
    p1_score += p1

    if p1_score >= 1000:
        break

    p2 += next(dice) + next(dice) + next(dice)
    num_rolls += 3
    p2 = (p2 - 1) % 10 + 1
    p2_score += p2

print(min(p1_score, p2_score) * num_rolls)

probabilities = Counter(map(sum, product(*[(1, 2, 3) for _ in range(3)])))


@cache
def simulate(p1, p2, p1_score, p2_score, p1_turn):
    if p1_score > 20:
        return 1, 0
    if p2_score > 20:
        return 0, 1

    if p1_turn:
        p1_wins, p2_wins = 0, 0
        for roll, chance in probabilities.items():
            p1_new = p1 + roll
            if p1_new > 10:
                p1_new -= 10
            p1_score_new = p1_score + p1_new
            a, b = simulate(p1_new, p2, p1_score_new, p2_score, False)
            p1_wins += chance * a
            p2_wins += chance * b
        return p1_wins, p2_wins
    else:
        p1_wins, p2_wins = 0, 0
        for roll, chance in probabilities.items():
            p2_new = p2+ roll
            if p2_new > 10:
                p2_new -= 10
            p2_score_new = p2_score + p2_new
            a, b = simulate(p1, p2_new, p1_score, p2_score_new, True)
            p1_wins += chance * a
            p2_wins += chance * b
        return p1_wins, p2_wins


print(max(simulate(p1_start, p2_start, 0, 0, True)))