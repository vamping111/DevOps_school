#!/usr/bin/env python3

def merge(a,b):
  for i,j in zip(a,b):
    yield i
    yield j
  return merge(a,b)

print(list(merge((a for a in range(1,4)),(b for b in range(2,5)))))
