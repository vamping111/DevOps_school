#!/usr/bin/env python3
import itertools
import heapq
def total(a,b):
	def generatora(a):
		for i in a:
			yield i
	def generatorb(b):
		for j in b:
			yield j
	res = heapq.merge(generatora(a),generatorb(b))
	return res
