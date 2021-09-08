#!/usr/bin/env python3

def sor(a,b):
	def merge(a,b):
		for i,j in zip(a,b):
			yield i
			yield j
		res = merge(a,b)
		return res
	total = merge(a,b)
	return sorted(total)


print(list(sor((a for a in (1,2,3)),(b for b in (6,7,8)))))
print(list(sor((a for a in range(1,4)),(b for b in range(2,5)))))

#[1, 2, 3, 6, 7, 8]
#[1, 2, 2, 3, 3, 4]
