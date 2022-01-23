my_file = open("day5.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    numbers.append(line)

# print(numbers)

# numbers[:] = [x for x in numbers if not x == '']


master = list()
for row in numbers:
    separate = list()
    new = [s for s in row.split(' -> ')]
    for coord in new:
        newer = [int(t) for t in coord.split(',')]
        separate.append(newer)
        # print(separate)
    master.append(separate)

# print(master)

filtered = master.copy()

filtered[:] = [z for z in filtered if z[0]
               [0] == z[1][0] or z[0][1] == z[1][1]]

print(filtered)

marker = 0

big = list()
# coords = list()
for set in filtered:
    coords = list()
    if set[0][0] == set[1][0]:
        if set[1][1] > set[0][1]:
            for n in range(set[0][1], set[1][1]+1):
                pos = str(set[0][0])+','+str(n)
                coords.append(pos)
        else:
            for n in range(set[1][1], set[0][1]+1):
                pos = str(set[0][0])+','+str(n)
                coords.append(pos)
    else:
        if set[1][0] > set[0][0]:
            for n in range(set[0][0], set[1][0]+1):
                pos = str(n)+','+str(set[0][1])
                coords.append(pos)
        else:
            for n in range(set[1][0], set[0][0]+1):
                pos = str(n)+','+str(set[0][1])
                coords.append(pos)
    big.append(coords)
    # marker += 1
    # print(marker)

# multiples = [y for n, y in enumerate(coords) if y in coords[:n]]
# count = [[x, coords.count(x)] for x in coords]

# count = [y for n, y in enumerate(count) if y not in count[:n]]

# print(multiples)
# print(len(multiples))

# non laggy code below

print(big)

multiple = []
done = 0

for set in big:

    copy = big[big.index(set)+1:]
    for num in set:
        for x in copy:
            if x.count(num) > 0:
                multiple.append(num)
                # break
            else:
                pass
    done += 1
    print(done)

print(multiple)

unique = [y for n, y in enumerate(multiple) if y not in multiple[:n]]

print(len(unique))
