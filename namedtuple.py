from collections import namedtuple

n = int(raw_input())
Student = namedtuple('Student', raw_input())
sum = 0
for _ in range(n):
    s = Student(*raw_input().split())
    sum += float(s.MARKS)
print "%.2f" % (sum/n)