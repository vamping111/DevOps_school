#!/usr/bin/env python3
def temperature(ch):
    if ch=='Fo':
        print("From Celsius to Fahrenheit")
        Tf=float(input("Enter your value in Celsius: "))
        Tc=9/5*Tf+32
        print("In Fahrengeit is is: ",Tc)
        exit()
    elif ch=='Co':
        print("From Fahrenheit to Celsius")
        Tc=input("Enter your value in Fahrenheit: ")
        Tf=((5/9)*(float(Tc)-32))
        print("In Celsius it is: ", Tf)
        exit()

temperature(ch=input("If you want conver Co to Fo, enter Fo\nIf you want convert Fo to Co, enter Co: "))
