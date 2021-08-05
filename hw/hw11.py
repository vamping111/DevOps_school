#!/usr/bin/env python3
array=[]
def letters_range(start, end, step=1):
    for i in range(ord(start), ord(end), step):
         array.append(chr(i))
letters_range(start=input("Enter first value: "),end=input("Enter second value: "),step=int(input("Enter step[1 by default]: ")or 1))
print(array)
