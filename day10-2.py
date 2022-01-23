from statistics import median

my_file = open("day10.txt", "r")
content = my_file.read().split('\n')

chunks = []
for line in content:
    chunks.append(list(line))

print(chunks)

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

n = 0

incomplete = []

for chunk in chunks:
    a = chunk
    while len(a) > 0:
        try:
            end = next(x for x in a if x in closing)
        except StopIteration:
            incomplete.append(a)
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
            # errors.append(end)
            break

print(incomplete)

dict = {')': 1, ']': 2, '}': 3, '>': 4}

scores = []

for i in incomplete:
    score = 0
    for char in reversed(i):
        close = closing[opening.index(char)]
        score = score * 5 + dict.get(close)

    print(score)
    scores.append(score)

print(median(scores))
