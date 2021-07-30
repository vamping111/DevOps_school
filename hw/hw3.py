#!/usr/bin/env python3
from collections import Counter
Enter = input("Enter values: ").lower()
array = Enter.split()
word=(max(set(array),key=array.count))
number=(Enter.count(max(set(array),key=array.count)))
print(word,"-",number)

