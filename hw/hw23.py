#!/usr/bin/env python3

def matrix(*a):
	x=''
	quan = len(list(*a))
	for i in range(int(quan)):
		x = [x for j in range(list(*a)[i])]
	return x

print(matrix([2,2]))


