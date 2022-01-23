import ast

my_file = open("day18.txt", "r")
content = my_file.read().split('\n')

master = []
for line in content:
    master.append(ast.literal_eval(line))

print(master)

input = master


def nested(l):
    try:
        y = next(x for x in l if isinstance(x, list))
    except StopIteration:
        return l
    return nested(y)


print(nested(input))
