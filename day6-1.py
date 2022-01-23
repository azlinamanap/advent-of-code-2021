my_file = open("day6.txt", "r")
content = my_file.read().split(',')

numbers = [int(x) for x in content]

# print(numbers)


# def fish(x):
#     for n in range(1, x+1):
#         mom = numbers.count(0)
#         numbers[:] = [(s-1) if s > 0 else 6 for s in numbers]
#         new = [8]*mom
#         numbers.extend(new)

#         print(len(numbers))

# print(len(numbers))

dict = {}
for n in range(9):
    dict[n] = dict.get(n, 0)

print(dict)

# initialise dict
for s in numbers:
    dict[s] = dict.get(s)+1

print(dict)
num = 0


def fish(x):
    for n in range(1, x+1):
        # print(dict)
        for s in dict.copy():
            count = dict.get(s)
            if s > 0:
                dict[s-1] = dict.get(s-1)+count
                dict[s] = dict.get(s)-count
                if s == 8:
                    dict[s] = dict.get(s)+eight
                if s == 6:
                    dict[s] = dict.get(s)+six
                else:
                    pass
            else:
                six = count
                eight = count
                dict[s] = dict.get(s)-count

        # print(dict)


fish(256)
print(dict)

num = 0
for key in dict:
    num += dict.get(key)

print(num)
