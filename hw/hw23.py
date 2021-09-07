#!/usr/bin/env python3

def matrix(a):
    x = ''
    quan=len(a)
    ent = a[0] * [x]
    if (quan == 1):
        return ent
    else:
        return [matrix(a[1:]) for j in range(a[0])]
