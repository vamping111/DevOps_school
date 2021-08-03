#!/usr/bin/env python3

def recuts(x):
    while True:
        if x=='cancel':
            print("Bye!")
            break
        else:
            try:
                if int(x) % 2 == 0:
                    print((int(x))/2)
                    recuts(x=input("Enter your value: "))
                else:
                    print((int(x)*3)+1)
                    recuts(x=input("Enter your value: "))
            except ValueError:
                print("You wrote a text, enter your value")
                recuts(x=input("Enter your value: "))
recuts(x=input("Enter your value: "))
