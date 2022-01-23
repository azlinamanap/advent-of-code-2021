my_file = open("day9.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    row = [int(x) for x in line]
    numbers.append(row)

print(numbers)

lows = []

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
        print('FOR NUMBER '+str(numbers[x][y]))
        print(s)
        if numbers[x][y] < min(s):
            lows.append(numbers[x][y])

print(lows)

sum = 0
for low in lows:
    sum += low + 1

print('SUM IS '+str(sum))
