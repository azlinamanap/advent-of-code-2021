from collections import defaultdict

my_file = open("test.txt", "r")
content = my_file.read().split('\n')

master = []
for line in content:
    master.append(line)

blank = master.index('')
message = master[0]
dirs = master[blank+1:]

print(message)
print(dirs)

instr = defaultdict(list)

for d in dirs:
    frm, to = d.split(' = ')
    instr[frm] = to

print(instr)

decoded = ""
for m in message:
    match = instr[m]
    decoded += match

print(decoded)


def literal(d):
    n = 6
    last = False
    number = ""
    count = 0
    while last == False:
        group = d[n:n+5]
        number += group[1:]
        print(group[0])
        print(number)
        if group[0] == "0":
            n += 5
            count += 1
            last = True
        else:
            n += 5
            count += 1

    print(count)
    zeros = count*5 % 4
    current = d[:n+zeros]
    print(d)
    d = d[n+zeros:]
    print(d)
    return current, d
    # print(d)
    # print(current)
    # number = int(number, 2)
    # print(number)


def parse(decoded):
    version = int(decoded[:3], 2)
    typeID = int(decoded[3:6], 2)
    print(version)
    if typeID == 4:
        literal(decoded)
    else:
        lenTypeID = int(decoded[6], 2)
        if lenTypeID == 0:
            bitLength = int(decoded[7:22], 2)
            print(bitLength)
            decoded = decoded[22:]
            print(decoded)
            lengthCount = 0
            while lengthCount < bitLength:
                current, d = parse(decoded)
                print(current)
                lengthCount += len(current)
                decoded = d
                print(d)

        if lenTypeID == 1:
            numSubPac = int(decoded[7:18], 2)


parse(decoded)
