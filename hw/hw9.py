#!/usr/bin/env python3
a=[]
for i in range(1,1000000):
    a.append(i)
n=''.join(map(str,a))
one=(str(n)[1-1])
ten=(str(n)[10-1])
hand=(str(n)[100-1])
tous=(str(n)[1000-1])
tentous=(str(n)[10000-1])
handtous=(str(n)[100000-1])
mil=(str(n)[1000000-1])
total=int(one)*int(ten)*int(hand)*int(tous)*int(tentous)*int(handtous)*int(mil)
print(total)
