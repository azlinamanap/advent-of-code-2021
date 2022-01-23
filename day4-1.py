my_file = open("day4.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    numbers.append(line)

numbers[:] = [x for x in numbers if not x == '']

chunked = list()
third = list()

# for i in range(0, len(numbers), 5):
#     chunked.append(numbers[i:i+5])


for row in numbers:
    new = [int(s) for s in row.split() if s.isdigit()]
    chunked.append(new)

# print(chunked)

for i in range(0, len(chunked), 5):
    third.append(chunked[i:i+5])

# print(third)

board = list()
for i in third:
    board.append(i)
    # print(i)
    a = [[], [], [], [], []]
    for j in range(0, len(i)):
        for k in range(0, len(i[j])):
            a[k].append(i[j][k])
    board.append(a)
    # transposing

print(board)

input = [6, 69, 28, 50, 36, 84, 49, 13, 48, 90, 1, 33, 71, 0, 94, 59, 53, 58, 60, 96, 30, 34, 29, 91, 11, 41, 77, 95, 17, 80, 85, 93, 7, 9, 74, 89, 18, 25, 26, 8, 87, 38, 68, 5, 12, 43, 27, 46, 62, 73,
         16, 55, 22, 4, 65, 76, 54, 52, 83, 10, 21, 67, 15, 47, 45, 40, 35, 66, 79, 51, 75, 39, 64, 24, 37, 72, 3, 44, 82, 32, 78, 63, 57, 2, 86, 31, 19, 92, 14, 97, 20, 56, 88, 81, 70, 61, 42, 99, 23, 98]

index = 0
inp = 0

while index == 0:
    for y in board:
        for row in y:
            row[:] = [z for z in row if not z == input[inp]]
        print(y)
    for a in board:
        for b in a:
            if b == []:
                index = board.index(a)
                print(index)
                break
            else:
                pass
    inp += 1

print(board)

stopped = input[inp-1]

sum = 0
winning = board[index]

for i in winning:
    for num in i:
        sum += num

print(sum)

total = stopped * sum
print(total)

print(winning)
