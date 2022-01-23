my_file = open("day3.txt", "r")
content = my_file.read().split('\n')

original = []
for line in content:
    original.append(line)

print(original)

numbers = original.copy()
second = original.copy()

for m in range(0, 12):
    common = 0
    for i in range(0, len(numbers)):
        x = numbers[i][m]
        if x == '0':
            common -= 1
        else:
            common += 1
    if common >= 0:
        bit_most = 1
    else:
        bit_most = 0
    numbers[:] = [y for y in numbers if y[m]
                  == str(bit_most) or len(numbers) == 1]
    print(numbers)

oxygen = int(numbers[0], 2)
print(oxygen)

for n in range(0, 12):
    common = 0
    for i in range(0, len(second)):
        x = second[i][n]
        if x == '0':
            common -= 1
        else:
            common += 1
    if common >= 0:
        bit_least = 0
    else:
        bit_least = 1
    second[:] = [z for z in second if z[n] ==
                 str(bit_least) or len(second) == 1]
    print(second)

scrubber = int(second[0], 2)
print(scrubber)

life = oxygen * scrubber
print(life)
