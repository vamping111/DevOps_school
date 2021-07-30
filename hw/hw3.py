#!/usr/bin/env python3
import collections
inp=input("Enter your values: ").lower()
stage=inp.split()
number=(inp.count(max(set(stage),key=stage.count)))
col=collections.Counter(stage).most_common(number)
total='\n'.join('-'.join(map(str,i))for i in col)
print(total)
