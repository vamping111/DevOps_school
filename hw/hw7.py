#!/usr/bin/env python3
print("First part of the task")
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

print("\nSecond part of the task")
user=[]
group=[]
groupfile='/etc/group'
passwdfile='/etc/passwd'
n=0
grpfile=open(groupfile,mode='r',encoding='utf_8')
for line in grpfile:
    stage=((line.split(":"))[0].strip())
    user.append(stage)
    lol=((line.split(":"))[3].strip())
    group.append(lol)
    gig=user[int(n)],group[int(n)]
    gig_list=(list(gig))
    n+=1
name=[]
uid=[]
b=0
lira={}
userfile=open(passwdfile,mode='r',encoding='utf_8')
for line in userfile:
    stg=((line.split(":"))[0].strip())
    sip=((line.split(":"))[3].strip())
    lira[stg]=sip   
    b+=1
lun=0
val=0
for i in user:
    if group[int(lun)]!='':
        print(user[int(val)],"-",lira[group[int(lun)]])
    lun+=1
    val+=1
