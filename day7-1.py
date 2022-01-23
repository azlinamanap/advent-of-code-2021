my_file = open("day7.txt", "r")
content = my_file.read().split(',')

numbers = [int(x) for x in content]

print(numbers)

diff = []

for n in range(min(numbers), max(numbers) + 1):
    new = [(abs(x-n)*(abs(x-n)+1))/2 for x in numbers]
    print(new)
    calc = sum(new)
    print(calc)
    diff.append(calc)

print(diff)
print(min(diff))
