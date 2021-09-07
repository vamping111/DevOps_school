#!/usr/bin/env python3
inp=input("Enter your values: ").split()
A=[int(s) for s in inp if s.isdigit()]
def solution(A):
    return [value for value in range(min(A),max(A)) if value not in A]
if min(sorted(A))==1:
    try:
        print("The value: ",(min(solution(A))), " is missed!")
    except ValueError:
        print("The value: ",(sorted(A)[-1]+1)," is missed")
else:
    print("The value: ",1, " is missed!")

