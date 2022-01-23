import cmath
from math import ceil

input = "target area: x=117..164, y=-140..-89"

content = input.split(': ')
content = content[1].split(', ')
print(content)

x = content[0]
y = content[1]

x = x.replace('x=', '').split('..')
y = y.replace('y=', '').split('..')
# board = [[[x, y] for x in range(int(x[0]), int(x[1])+1)]
#          for y in range(int(y[0]), int(y[1])+1)]

# for row in board:
#     print(row)

print(x)

maxy = abs(int(y[0])-1)
miny = int(y[0])

maxx = int(x[1])
a = 1
b = 1
c = -2*int(x[0])
d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
minx = ceil(max([sol1.real, sol2.real]))
print(minx, maxx, miny, maxy)

sum = 0


def test(s, t):
    global sum
    hit = False
    p = 0
    q = 0
    while p <= int(x[1]) and q >= int(y[0]) and hit == False:
        p += s
        q += t
        # check if in board
        if p in range(int(x[0]), int(x[1])+1) and q in range(int(y[0]), int(y[1])+1):
            hit = True
        # reduce velocity
        if s > 0:
            s -= 1
        t -= 1

    if hit:
        sum += 1


possibles = [[[x, y] for x in range(minx, maxx+1)]
             for y in range(miny, maxy+1)]

for p in possibles:
    for q in p:
        [a, b] = q
        test(a, b)

print(sum)
