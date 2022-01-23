from collections import Counter

tpl, _, *rules = open("test.txt").read().split('\n')
rules = dict(r.split(" -> ") for r in rules)
pairs = Counter(map(str.__add__, tpl, tpl[1:]))
chars = Counter(tpl)

print(tpl)
print(_)
print(rules)
print(pairs)
print(chars)

for _ in range(40):
    for (a, b), c in pairs.copy().items():
        x = rules[a+b]
        pairs[a+b] -= c
        pairs[a+x] += c
        pairs[x+b] += c
        chars[x] += c

print(pairs)
print(chars)
print(max(chars.values())-min(chars.values()))
