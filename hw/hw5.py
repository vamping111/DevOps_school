#!/usr/bin/env python3
inp=input("Enter your values: ").split()
A=[int(s) for s in inp if s.isdigit()]
def solution(A):
    return [value for value in range(min(A),max(A)) if value not in A]
if min(sorted(A))==1:
    print("The value: ",(min(solution(A))), " is missed!")
else:
    print("The value: ",(A[0]-1), " is missed!")

