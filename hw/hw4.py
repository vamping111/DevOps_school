#!/usr/bin/env python3
import re
a = input("Введите ваши значения: ")
neg_dig=re.findall("-\d+",a)
tot_neg_dig=[i*2 for i in neg_dig]
pos_dig=re.findall("\d+",a)
for i in neg_dig*2:
    pos_dig.append(i)
total=0
for b in pos_dig:
    total=total+int(b)
print(total)
