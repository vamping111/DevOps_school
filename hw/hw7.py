#!/usr/bin/env python3
import re
import collections
inputfile='/etc/passwd'
arr=[]
myfile=open(inputfile,mode='r',encoding='utf_8')
for line in myfile:
    stage=((line.split(":"))[6].strip())
    arr.append(stage)
col=collections.Counter(arr).most_common()
for i in col:
    env=(i[0])
    cont=(i[1])
    print(env,"-",cont)
