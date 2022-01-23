my_file = open("day1.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    numbers.append(line)
for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])

print(numbers)


def run():
    new = []
    increase = 0
    for i in range(2, len(numbers)):
        x = numbers[i]
        y = numbers[i-1]
        z = numbers[i-2]

        sum = x + y + z
        new.append(sum)

    for j in range(1, len(new)):
        diff = new[j] - new[j-1]
        if diff > 0:
            increase = increase + 1

    print(increase)


run()
