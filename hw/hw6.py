#!/usr/bin/env python3

i=0
x=0
xb=0
yb=0
ib=0
while i<=1000000:
    xb=bin(i)[2:]
    yb=xb[::-1]
    x = str(i)[::-1]
    if xb==yb:
        if int(x)==i:
            ib=ib+i
    i=i+1
print(bin(ib))
print(ib)
