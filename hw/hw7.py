#!/usr/bin/env python3

import collections
print("First part of the task")

inputfile='./passwd'
arr=[]
myfile = open(inputfile, mode='r', encoding='utf_8')
for line in myfile:
    stage = ((line.split(":"))[6].strip())
    arr.append(stage)
col = collections.Counter(arr).most_common()
for i in col:
    env = (i[0])
    cont = (i[1])
    print(env,"-",cont)


print("\nSecond part of the task")
user = []
group = []
names = []
groupfile = './group'
passwdfile = './passwd'
n = 0
grpfile = open(groupfile, mode='r', encoding='utf_8')
br = 0

for line in grpfile:
    stage = ((line.split(":"))[0].strip())
    user.append(stage)
    lol = ((line.split(":"))[3].strip().split(","))
    group.append(lol)
    gig = user[int(n)], group[int(n)]
    gig_list = (list(gig))
    n += 1

name = []
uid = []
b = 0
lira = {}
userfile = open(passwdfile, mode='r', encoding='utf_8')

for line in userfile:
    stg = ((line.split(":"))[0].strip())
    sip = ((line.split(":"))[3].strip())
    lira[stg] = sip
    b += 1
moon = ''

grpfile.seek(0)

i = 0
for el in grpfile:
    try:
        moon = moon + el.split(":")[0] + ":" + el.split(":")[2] + ","
        if len(el.split(":")[3]) > 1:
            for name in el.split(":")[3].split(","):
                moon = moon + lira[name] + ","
            moon = moon + " "
        else:
            moon = moon + " "
            i += 1
            continue
        i += 1
    except KeyError:
        z=1
print(moon)
