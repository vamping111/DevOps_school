#!/usr/bin/env python3

def matrix(*a):
	x=''
	quan = len(list(*a))
	for i in range(int(quan)):
		x = [x for j in range(list(*a)[i])]
	print(x)
total = list(map(int , (input("Enter: ").split(','))))
matrix(total)