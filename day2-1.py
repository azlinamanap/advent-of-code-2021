my_file = open("day2.txt", "r")
content = my_file.read().split('\n')

directions = []
for line in content:
    directions.append(line)
# for n in range(0, len(numbers)):
#     numbers[n] = int(numbers[n])

print(directions)

ways = []
numbers = []

for direction in directions:
    list = direction.split()
    ways.append(list[0])
    numbers.append(int(list[1]))

horizontal = 0
depth = 0

for i in range(0, len(ways)):
    if ways[i] == 'forward':
        horizontal = horizontal + numbers[i]
    if ways[i] == 'down':
        depth = depth + numbers[i]
    if ways[i] == 'up':
        depth = depth - numbers[i]

total = horizontal * depth
print(total)
