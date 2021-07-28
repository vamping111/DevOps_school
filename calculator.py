#!/usr/bin/env python3

a = int(input("Введите число: "))
symb = input("Введите символ: ")
b = int(input("Введите второе число: "))


if symb == '+':
	result = a + b
	print(result)
	print("Результат: ")
elif symb == '-':
	result = a - b
	print("Результат: ")
	print(result)
elif symb == '*':
	result = a * b
	print("Результат: ")
	print(result)
elif symb == '/':
	result = a / b
	print("Результат: ")
	print(result)
