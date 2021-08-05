#!/usr/bin/env python3
last = current = 1
elem = int(input("Enter your value: "))
for i in range(int(elem-2)):
    stage = last + current
    last = current
    current = stage
print("Your value is: " + str(current))
    
