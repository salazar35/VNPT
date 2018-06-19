from collections import OrderedDict

n = int(raw_input())
s = OrderedDict()
for _ in range(n):
    name, space, price = raw_input().rpartition(' ')
    s[name] = s.get(name, 0) + int(price)
for name, price in s.items():
    print str(name) + " " + str(price)