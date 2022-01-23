my_file = open("test.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    row = [int(x) for x in line]
    numbers.append(row)

print(numbers)

start = numbers[0][0]

leny = len(numbers)
lenx = len(numbers[leny-1])

x = 0
y = 0
while x < lenx and y < leny:
    l = numbers[y][x-1] if x > 0 else None
    r = numbers[y][x+1] if x < len(numbers[y])-1 else None
    u = numbers[y-1][x] if y > 0 else None
    d = numbers[y+1][x] if y < len(numbers)-1 else None

    for n in [l, r, u, d]:
