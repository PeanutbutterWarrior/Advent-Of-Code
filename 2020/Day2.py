with open('Day2.txt', 'r') as file:
    data = file.read().split('\n')

# Part 1
num_correct_password = 0
for password in data:
    if password:
        dash_ind = password.index('-')
        space_ind = password.index(' ')
        minimum = int(password[:dash_ind])
        maximum = int(password[dash_ind + 1:space_ind])
        letter = password[space_ind + 1]
        word = password[space_ind + 4:]
        if minimum <= word.count(letter) <= maximum:
            num_correct_password += 1
print(num_correct_password)

# Part 2
num_correct_password = 0
for password in data:
    if password:
        dash_ind = password.index('-')
        space_ind = password.index(' ')
        ind1 = int(password[:dash_ind])
        ind2 = int(password[dash_ind + 1:space_ind])
        letter = password[space_ind + 1]
        word = password[space_ind + 4:]
        if (word[ind1 - 1] == letter) ^ (word[ind2 - 1] == letter):
            num_correct_password += 1
print(num_correct_password)
