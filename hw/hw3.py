#!/usr/bin/env python3
import collections
inp=input("Enter your values: ").lower()
arr=inp.split()
col=collections.Counter(arr).most_common()
lira={}
for i in col:
    env=(i[0])
    cont=(i[1])
    lira[env]=cont
freq=max(lira.values())
total={c: v for c, v in lira.items() if v==freq}
tv=list(total.values())
tk=list(total.keys())
val=0
for i in tk:
    print(i,"-",tv[val])
    val+=1

