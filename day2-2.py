my_file = open("day2.txt", "r")
content = my_file.read().split('\n')

directions = []
for line in content:
    directions.append(line)

print(directions)

ways = []
numbers = []

for direction in directions:
    list = direction.split()
    ways.append(list[0])
    numbers.append(int(list[1]))

horizontal = 0
depth = 0
aim = 0

for i in range(0, len(ways)):
    if ways[i] == 'forward':
        horizontal = horizontal + numbers[i]
        depth = depth + numbers[i] * aim
    if ways[i] == 'down':
        aim = aim + numbers[i]
    if ways[i] == 'up':
        aim = aim - numbers[i]

total = horizontal * depth
print(total)
