from collections import defaultdict
from math import ceil

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
    instr[frm] = to

print(instr)

starting = [polymer[i:i+2] for i in range(0, len(polymer)-1)]
print(starting)

counter = defaultdict(list)
for l in polymer:
    counter[l] = counter.get(l, 0) + 1
print(counter)

pairs = defaultdict(list)
for s in starting:
    pairs[s] = 1
print(pairs)


def split(steps):
    for _ in range(steps):
        for (a, b), c in pairs.copy().items():
            match = instr[a+b]
            pairs[a+b] = pairs.get(a+b, 0) - c
            pairs[a+match] = pairs.get(a+match, 0) + c
            pairs[match+b] = pairs.get(match+b, 0) + c
            counter[match] = counter.get(match, 0) + c


split(40)

print(counter)
vals = counter.values()
print(vals)
print(ceil(max(vals)-min(vals)))
