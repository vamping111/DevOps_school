1. Составить таблицу соответствия между различными объектами основных классов: int, str и объектами класса bool.
>>> bool(1)
True
>>> bool(500)
True
>>> bool(0)
False
>>> bool(-1)
True
>>> bool('1')
True
>>> bool('privet')
True
>>> bool('-1')
True
>>> bool('')
False
>>> bool('0')
True

Вывод для int: все значения, кроме 0 являются значением True.
Вывод для str: все значения, кроме пустой строки являются True.

2. Разобраться с различиями между input() и raw_input(). Также в контексте разных версий python: 2 и 3.

Разница между input() и raw_input() в том, что input() есть в python3, а raw_input()в python2. По сути это та же функция для ввода строки.

Пример input() в python3:

name = input("Введите ваше имя: ")
print("Ваше имя: " ,name)

Введите ваше имя: Linar
Ваше имя:  Linar

Пример raw_input() в python2:

name = raw_input("Введите ваше имя: ")
print "Ваше имя: " ,name

Введите ваше имя: Linar
Ваше имя:  Linar

3. Найти и прочитать PEP про изменение print между python2 и python3.

Главным различием между print в python3 и python2 является добавление скобок.
В python3 print(), а в python2 просто print.

Пример:
    python2:
        >>> a=3
        >>> print a
        3

    python3:
        >>> a=3
        >>> print(a)
        3
