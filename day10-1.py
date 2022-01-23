my_file = open("day10.txt", "r")
content = my_file.read().split('\n')

chunks = []
for line in content:
    chunks.append(list(line))

print(chunks)

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

n = 0

errors = []

for chunk in chunks:
    a = chunk
    while len(a) > 0:
        try:
            end = next(x for x in a if x in closing)
        except StopIteration:
            # print("PASS")
            break
        i = a.index(end)
        # print(a)
        # print(a[:end])
        open = a[a.index(end)-1]
        if closing.index(end) == opening.index(open):
            del a[i]
            del a[i-1]
        else:
            # print('FAIL')
            errors.append(end)
            break

print(errors)

dict = {')': 3, ']': 57, '}': 1197, '>': 25137}

sum = 0

for error in errors:
    sum += dict.get(error)

print(sum)
