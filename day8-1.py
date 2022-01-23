my_file = open("day8.txt", "r")
content = my_file.read().split('\n')

output = []
for line in content:
    output.append(line.split("| ")[1])

print(output)

count = 0
for x in output:
    list = [y for y in x.split() if len(y) in (2, 3, 4, 7)]
    print(list)
    count += len(list)

print(count)
