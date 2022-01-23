my_file = open("day4.txt", "r")
content = my_file.read().split('\n')

numbers = []
for line in content:
    numbers.append(line)

numbers[:] = [x for x in numbers if not x == '']

chunked = list()
third = list()

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
    # print(a)

print(board)

input = [6, 69, 28, 50, 36, 84, 49, 13, 48, 90, 1, 33, 71, 0, 94, 59, 53, 58, 60, 96, 30, 34, 29, 91, 11, 41, 77, 95, 17, 80, 85, 93, 7, 9, 74, 89, 18, 25, 26, 8, 87, 38, 68, 5, 12, 43, 27, 46, 62, 73,
         16, 55, 22, 4, 65, 76, 54, 52, 83, 10, 21, 67, 15, 47, 45, 40, 35, 66, 79, 51, 75, 39, 64, 24, 37, 72, 3, 44, 82, 32, 78, 63, 57, 2, 86, 31, 19, 92, 14, 97, 20, 56, 88, 81, 70, 61, 42, 99, 23, 98]

inp = 0

while len(board) > 2:
    for y in board:
        for row in y:
            row[:] = [z for z in row if not z == input[inp]]
        # print(y)
    for a in board:
        for b in a:
            if b == []:
                if board.index(a) % 2 == 0:
                    board[:] = [n for n in board if not n ==
                                a and board.index(n) != board.index(a) + 1]
                else:
                    board[:] = [n for n in board if not n ==
                                a and board.index(n) != board.index(a) - 1]
                break
            else:
                pass
    inp += 1

print(input[inp])
print(board)

last = board[0]
print(last)

while len(board) > 1:
    for s in board:
        for row in s:
            row[:] = [z for z in row if not z == input[inp]]
        print(s)
    for t in board:
        for r in t:
            if r == []:
                board[:] = [n for n in board if not n == t]
                break
            else:
                pass
    inp += 1

print(board)


sum = 0


for i in last:
    for num in i:
        sum += num

print(sum)

total = sum * input[inp-1]

print(total)
