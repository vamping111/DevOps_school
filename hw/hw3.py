#!/usr/bin/env python3
import numpy as np

enter=input("Enter your values: ").lower()
stage=enter.split()
number=(enter.count(max(set(stage),key=stage.count)))

a=np.array(stage)
un, cnt=np.unique(a, return_counts=True)
words=un[cnt==cnt.max()]
for i in words:
    print(i,'-',number)


