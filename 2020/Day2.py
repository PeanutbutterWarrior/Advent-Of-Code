with open('Day2.txt', 'r') as file:
    data = file.read().split('\n')

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
