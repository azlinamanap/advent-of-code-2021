my_file = open("day11.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    row = [int(x) for x in line]
    numbers.append(row)

# print(numbers)

simult = False
steps = 0

while simult == False:
    # flashes = 0
    steps += 1
    # print(steps)
    # for n in range(s):
    for row in numbers:
        row[:] = [a+1 for a in row]
        # print(row)
    counter = 0
    for row in numbers:
        for elem in row:
            if elem >= 10:
                counter += 1
    while counter > 0:
        master = []
        for x in range(len(numbers)):
            list = []
            for y in range(len(numbers[x])):
                count = 0
                l = numbers[x][y-1] if y > 0 else None
                r = numbers[x][y+1] if y < len(numbers[x])-1 else None
                u = numbers[x-1][y] if x > 0 else None
                d = numbers[x+1][y] if x < len(numbers)-1 else None
                ul = numbers[x-1][y-1] if x > 0 and y > 0 else None
                ur = numbers[x-1][y +
                                  1] if x > 0 and y < len(numbers[x])-1 else None
                ll = numbers[x+1][y -
                                  1] if x < len(numbers)-1 and y > 0 else None
                lr = numbers[x+1][y+1] if x < len(numbers) - \
                    1 and y < len(numbers[x])-1 else None

                for n in (l, r, u, d, ul, ur, ll, lr):
                    if n != None and n >= 10:
                        count += 1

                list.append(count)
        # print(list)
            master.append(list)

        # print(numbers)
        # print(master)

        for x in range(len(numbers)):
            numbers[x][:] = [a+b if a < 10 and a != 0 else 0 for a,
                             b in zip(numbers[x], master[x])]

        another = 0
        for row in numbers:
            for elem in row:
                if elem >= 10:
                    another += 1

        counter = another

    check = []
    for row in numbers:
        for elem in row:
            check.append(elem)

    # print(check)

    if check.count(0) == len(check):
        simult = True


print(f'first step is {steps}')
