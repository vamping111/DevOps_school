#!/usr/bin/env python3

def matrix(a):
    x = ''
    quan=len(a)
    if (quan == 1):
        return [x] * a[0]
    else:
        return [matrix(a[1:]) for j in range(a[0])]
