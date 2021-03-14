with open('Day5.txt') as file:
    data = file.read().split()


def get_seat_id(partition):
    num = 0
    for char in partition:
        num <<= 1
        num |= char in {'B', 'R'}
    return num


# Part 1
print(max(map(get_seat_id, data)))
