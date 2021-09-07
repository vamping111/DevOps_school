1. Составить таблицу соответствия между различными объектами основных классов: int, str и объектами класса bool.

Object|Type|Bool_value
------|----|----------
a     | str| False
Linar | str| False
7     | int| False
1     | int| True

По умолчанию, все объекты, кроме 1 равны False, это касается int.
Но можно явно указать, чтобы определенная переменная обращалась к True.
Например:
    >>1==True
    True
    >>7==True
    False
    >>Linar==True
    False
    >>str('True')==True
    False
    >>Linar=True
    >>Linar==True
    True
    >>> a=bool('Linar') - Если присвоить НЕпустой строке тип bool, то она так же соот-ет True
    >>> a==True
    True
    >>> a=bool('') - Если присвоить пустой строке тип bool, то она также соот-ет False
    >>> a==True
    False

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
