import sys

with open(sys.argv[1], "r") as file:
    data = file.read().strip()

start, end = data.split("-")
start = int(start)
end = int(end)

count1 = 0
count2 = 0
for i in range(start, end):
    i = str(i)
    is_valid1 = False
    is_valid2 = False
    current_repeat = i[0]
    repeat_length = 1
    for a, b in zip(i, i[1:]):
        if int(b) < int(a):
            is_valid1 = False
            is_valid2 = False
            break
        
        if a == b:
            is_valid1 =  True
        
        if current_repeat == b:
            repeat_length += 1
        else:
            current_repeat = b
            if repeat_length == 2:
                is_valid2 = True
            repeat_length = 1
    else:
        if repeat_length == 2:
            is_valid2 = True
        
    if is_valid1:
        count1 += 1
    if is_valid2:
        count2 += 1

print(count1)
print(count2)