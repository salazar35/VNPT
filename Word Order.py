from collections import OrderedDict, Counter

s = OrderedDict()
n = int(raw_input())
for _ in range(n):
    item = str(raw_input())
    s[item] = s.get(item, 0) + 1
print s.__len__()
print " ".join(map(str,s.values()))
