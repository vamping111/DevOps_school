1. Составить таблицу соответствия между различными объектами основных классов: int, str и объектами класса bool.

Object     |Type|Id             |Var
-----------|----|---------------|------
Linar      |bool|9476448	|True
c          |bool|9476448	|True
a          |int |9788672	|3
Nasyrov    |int |9788672	|3
b          |str |139800609929712|'Tarelka'
Gusmanovich|str |139800609929712|'Tarelka'

Как я понял задание,я должен был показать, что разные переменные при присвоении какого-либо значения ссылаются на один и тот же объект с соответствующим id. То есть обе переменные 'Linar' и 'c' ссылаются на один и тот же объект True, имеющим булево значение и id равное 9476448.Если неправильно понял задание, просьба подсветить.

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