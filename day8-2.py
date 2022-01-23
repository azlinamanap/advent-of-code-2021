my_file = open("day8.txt", "r")
content = my_file.read().split('\n')

input = []
for line in content:
    input.append(line.split(" |")[0])

output = []
for line in content:
    output.append(line.split("| ")[1])

print(input)
print(output)

key = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
       'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

total = 0

for s in input:
    code = ""
    list = [''.join(sorted(y)) for y in s.split()]
    list.sort(key=len)
    print(list)

    cf = list[0]
    a = "".join([x for x in list[1] if x not in list[0]])
    bd = "".join([x for x in list[2] if x not in list[0]])
    eg = "".join([x for x in list[9] if x not in a.join(bd.join(cf))])
    adg = "".join(
        [x for x in list[9] if (x in list[3] and x in list[4] and x in list[5])])
    dg = adg.replace(a, '')
    g = "".join([x for x in dg if x in eg])
    d = dg.replace(g, '')
    e = eg.replace(g, '')
    abfg = "".join(
        [x for x in list[9] if (x in list[6] and x in list[7] and x in list[8])])
    bf = "".join([x for x in abfg if (x is not a and x is not g)])
    b = "".join([x for x in bf if x in bd])
    f = bf.replace(b, '')
    d = bd.replace(b, '')
    c = cf.replace(f, '')

    keys = [a+b+c+e+f+g, c+f, a+c+d+e+g, a+c+d+f+g, b+c+d+f, a +
            b+d+f+g, a+b+d+e+f+g, a+c+f, a+b+c+d+e+f+g, a+b+c+d+f+g]
    keys = [''.join(sorted(x)) for x in keys]
    print(keys)

    another = [''.join(sorted(y)) for y in output[input.index(s)].split()]
    print(another)
    for t in another:
        digit = str(keys.index(t))
        # print(digit)
        code += digit

    print(code)

    total += int(code)

print('NUM IS '+str(total))
