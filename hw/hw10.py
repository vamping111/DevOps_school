#!/usr/bin/env python3
array=[]
def recuts(x):
    while True:
            if int(x)==1:
                array.append(x)
                print(len(array)-1)
                exit()
            elif int(x)%2==0:
                array.append(x/2)
                recuts(array[-1])
            else:
                array.append((int(x)*3)+1)
                recuts(array[-1])
recuts(x=int(input("Enter your value: ")))
