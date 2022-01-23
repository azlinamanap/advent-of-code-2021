from collections import defaultdict

my_file = open("day14.txt", "r")
content = my_file.read().split('\n')

master = []
for line in content:
    master.append(line)

blank = master.index('')
polymer = master[0]
dirs = master[blank+1:]

print(polymer)
print(dirs)

instr = defaultdict(list)

for d in dirs:
    frm, to = d.split(' -> ')
    instr[frm].append(to)

print(instr)


def step(n):
    global polymer
    for x in range(n):
        adds = []
        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            match = instr[pair][0]
            adds.append(match)
        copy = polymer[0]
        for a in range(len(adds)):
            copy = copy+adds[a]+polymer[a+1]

        # print(copy)

        polymer = copy
        print(x)


step(20)

print(polymer)

letters = set(polymer)
counts = []
for l in letters:
    c = polymer.count(l)
    # print(c)
    counts.append(c)

print(max(counts) - min(counts))
