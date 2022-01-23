my_file = open("day1.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    numbers.append(line)
for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])

print(numbers)


def run():
    increase = 0
    for i in range(0, len(numbers)):
        x = numbers[i]
        if i == 0:
            pass
        else:
            y = numbers[i-1]
            if x - y > 0:
                increase = increase + 1
    print(increase)


run()
