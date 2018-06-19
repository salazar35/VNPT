from collections import deque

n = int(raw_input())
r = []
d = deque()
f = "Yes"
for _ in range(n):
    m = int(raw_input())
    ar = map(int, raw_input().split())
    for j in ar:
        d.append(j)
    f = "Yes"
    for i in range(m/2):
        if len(d) > 1:
            if d[0] >= d[1]:
                d.popleft()
            else:
                f = "No"
                r.append(f)
                break
        if len(d) > 1:
            if d[-1] >= d[-2]:
                d.pop()
            else:
                f = "No"
                r.append(f)
                break
    if f == "Yes":
        r.append(f)
for x in r:
    print x