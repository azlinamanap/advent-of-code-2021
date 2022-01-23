my_file = open("day9.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    row = [int(x) for x in line]
    numbers.append(row)

print(numbers)

lows = []
coords = []

for x in range(len(numbers)):
    for y in range(len(numbers[x])):
        s = []

        left = numbers[x][y-1] if y > 0 else None
        s.append(left)

        right = numbers[x][y+1] if y < len(numbers[x])-1 else None
        s.append(right)

        up = numbers[x-1][y] if x > 0 else None
        s.append(up)

        down = numbers[x+1][y] if x < len(numbers)-1 else None
        s.append(down)

        s = [x for x in s if x != None]
        # print('FOR NUMBER '+str(numbers[x][y]))
        # print(s)
        if numbers[x][y] < min(s):
            lows.append(numbers[x][y])
            t = [x, y]
            coords.append(t)


print(lows)
print(coords)

list = []


def check(x, y):

    # print(f"{x},{y}")
    list.append([x, y])
    n = numbers[x][y]
    l = numbers[x][y-1] if y > 0 else None
    r = numbers[x][y+1] if y < len(numbers[x])-1 else None
    u = numbers[x-1][y] if x > 0 else None
    d = numbers[x+1][y] if x < len(numbers)-1 else None

    if l != None and n < l and l != 9:
        check(x, y-1)
    if r != None and n < r and r != 9:
        check(x, y+1)
    if u != None and n < u and u != 9:
        check(x-1, y)
    if d != None and n < d and d != 9:
        check(x+1, y)


total = 1
sizes = []

for n in range(len(lows)):
    list.clear()
    x = coords[n][0]
    y = coords[n][1]
    # print(lows[n])
    check(x, y)
    unique = [x for n, x in enumerate(list) if x not in list[:n]]
    sizes.append(len(unique))

print(sizes)

big = sorted(sizes)[-3:]

for size in big:
    total = total * size

print(total)
