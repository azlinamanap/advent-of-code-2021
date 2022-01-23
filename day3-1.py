my_file = open("day3.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    numbers.append(line)

print(numbers)

gamma = ''
epsilon = ''

for n in range(0, 12):
    common = 0
    for i in range(0, len(numbers)):
        x = numbers[i][n]
        if x == '0':
            common -= 1
        else:
            common += 1
    if common > 0:
        bit_most = 1
        bit_least = 0
    else:
        bit_most = 0
        bit_least = 1
    gamma += str(bit_most)
    epsilon += str(bit_least)

g = int(gamma, 2)
e = int(epsilon, 2)

power = g * e

print(power)
