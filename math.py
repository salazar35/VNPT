from collections import defaultdict

n, m = map(int, raw_input().split())
a = defaultdict(list)
for i in xrange(n):
    a[raw_input()].append(i+1)
for i in xrange(m):
    b = raw_input()
    if a[b]:
        print " ".join(map(str, a[b]))
    else:
        print "-1"
