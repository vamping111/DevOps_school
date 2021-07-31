#!/usr/bin/env python3
inp=input("Enter your values: ")
array=[]
numeric=''
for char in inp:
    if char.isdigit():
        numeric=numeric+char
    else:
        if numeric!='':
            array.append(int(numeric))
            numeric=''
    if numeric!='':
        array.append(int(numeric))
print(sum(array))
