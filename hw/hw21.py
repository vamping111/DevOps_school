#!/usr/bin/env python3
def arr(a,b):
  total = []
  for i in a:
    total.append(i)
  for j in b:
    total.append(j)
  for x in sorted(total):
    yield x
        
s = arr([8,96,124],[72,487,620])
print(next(s))
8
print(next(s))
72
print(next(s))
96
print(next(s))
124
print(next(s))
487
print(next(s))
620
print(next(s))
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#StopIteration
