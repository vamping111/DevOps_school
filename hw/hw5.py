#!/usr/bin/env python3
inp=input("Enter your values: ").split()
A=[int(s) for s in inp if s.isdigit()]
def solution(A):
    return [value for value in range(min(A),max(A)) if value not in A]
try:
    (min(solution(A)))
    print("The value: ",(min(solution(A))), " is missed")
except ValueError:
    B = (A[0]-1)
    if B == 0:
        print(A[-1]+1)
    elif B >= 0:
        print(B)

