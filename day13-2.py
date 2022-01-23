my_file = open("day13.txt", "r")
content = my_file.read().split('\n')

master = []
for line in content:
    master.append(line)

blank = master.index('')
coords = master[:blank]
dirs = master[blank+1:]

print(coords)
print(dirs)

points = []
for c in coords:
    new = [int(x) for x in c.split(',')]
    points.append(new)

print(points)

folds = []
for d in dirs:
    new = d.split()[2]
    mew = [x for x in new.split('=')]
    folds.append(mew)

print(folds)

for f in folds:
    foldline = int(f[1])
    if f[0] == 'y':
        allpoints = [p for p in points if p[1] > foldline]
        print(allpoints)
        newpoints = [[a, foldline-(b-foldline)] for a, b in allpoints]
        print(newpoints)
    if f[0] == 'x':
        allpoints = [p for p in points if p[0] > foldline]
        print(allpoints)
        newpoints = [[foldline-(a-foldline), b] for a, b in allpoints]
        print(newpoints)

    half = [h for h in points if h not in allpoints]
    # print(half)
    points = half + [n for n in newpoints if n not in half]
    # print(points)

print(len(points))

print(points)

for y in range(10):
    row = []
    for x in range(50):
        if [x, y] in points:
            row.append('#')
        else:
            row.append('.')

    print(row)
