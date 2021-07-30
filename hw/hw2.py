#!/usr/bin/env python3
l=input("Enter some values: ")

space=l.split()
for val in space:
	print(val, end=' ')
print(' ')

total=list(set(l.split()))
for val in total:
        print(val, end=' ')
print(' ')
