#!/usr/bin/env python3
inp=input("Enter your values: ").split()
A=[int(s) for s in inp if s.isdigit()]
def solution(A):
    return [value for value in range(min(A),max(A)) if value not in A]
try:
    (min(solution(A)))
    print("The value: ",(min(solution(A))), " is missed")
except ValueError:
    B=sorted(A)
    print(A[-1]+1)
#print(min(solution(A)))
