# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input('Input number'))
n = 0
while 2 ** n < num:
    print(2 ** n)
    n += 1
