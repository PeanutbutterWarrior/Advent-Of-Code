def b26(a):
    output = ''
    while a:
        output = chr(a % 26 + 65) + output
        a //= 26
    return output


#           |            |
inp = iter('00000000000000')

w = int(next(inp))
x = 1
y = w + 15
z = w + 15
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
x += 14
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 12
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 1
x += 11
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 15
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 26
x += -9
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 12
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 26
x += -7
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 15
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 1
x += 11
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 2
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 26
x += -1
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 11
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 26
x += -16
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 15
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 1
x += 11
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 10
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 26
x += -15
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 2
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 1
x += 10
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 0
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 1
x += 12
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 0
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 26
x += -4
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 15
y *= x
z += y
print(f'x: {x}, y: {y}, z: {b26(z)}')

w = int(next(inp))
x = z
x %= 26
z //= 26
x += 0
x = int(x == w)
x = int(x == 0)
y = 25
y *= x
y += 1
z *= y
y = w
y += 15
y *= x
z += y


print(f'x: {x}, y: {y}, z: {b26(z)}')