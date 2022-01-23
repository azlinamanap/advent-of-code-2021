from itertools import permutations as p
from collections import defaultdict

my_file = open("day12.txt", "r")
content = my_file.read().split('\n')

master = []
for line in content:
    master.append(line)

routes = defaultdict(list)
# dirs = list()
# for row in master:
#     separate = list()
#     new = [s for s in row.split('-')]
#     dirs.append(new)

for row in master:
    frm, to = row.split('-')
    routes[frm].append(to)
    routes[to].append(frm)

print(routes)

visited = set()


def dfs(visited, cave):

    if cave not in visited:
        visited = visited | {cave}
        if cave == 'end':

            return visited
        if cave in visited:
            if cave == 'start':
                return None
            if cave.islower():
                return None

    for next in routes[cave]:
        return dfs(visited, next)


print(dfs(visited, 'start'))


# # big = []
# count = 0

# for i in range(2, 5):
#     pStart = p(starts, 1)
#     pMid = p(mids, i-2)
#     pEnd = p(ends, 1)
#     # final = ()
#     # for item in perm:
#     #     print(item)
#     # listp = list(perm)
#     print(list(pMid))

#     # final = [x for x in listp if x[0][0] == 'start' and x[i][1] == 'end']
#     # print(final)
# #     for l in final:
# #         # print(l)
# #         smalls = []
# #         for n in range(len(l)-1):
# #             if l[n][1] != l[n+1][0]:
# #                 final = [x for x in final if x != l]
# #                 break
# #             else:
# #                 if l[n][1].islower():
# #                     if l[n][1] in smalls:
# #                         final = [x for x in final if x != l]
# #                         break
# #                     else:
# #                         smalls.append(l[n][1])
# #                 else:
# #                     pass

# #     # print(final)
# #     for f in final:
# #         print(f)
# #         count += 1
# #         # big.append(f)

# # print(f'Total is {count}')
