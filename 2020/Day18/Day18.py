with open('Day18.txt') as file:
    data = file.read().split('\n')


def evaluate_expression(expr, ind=0):
    total = None
    operator = None
    while True:
        try:
            char = expr[ind]
        except IndexError:
            break

        if char == ' ':
            pass
        elif char in {'+', '*'}:
            operator = char
        elif char == ')':
            break
        elif char == '(':
            val, ind = evaluate_expression(expr, ind + 1)
            if operator == '+':
                total += val
            elif operator == '*':
                total *= val
            else:
                total = val
        else:
            char = int(char)
            if operator == '+':
                total += char
            elif operator == '*':
                total *= char
            else:
                total = char
        ind += 1
    return total, ind


answer = 0
for line in data:
    val, _ = evaluate_expression(line)
    answer += val
print(answer)
