# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4
import random


def sum(a, b):
    if b == 0:
        return a
    a += 1
    return sum(a, b - 1)


a = random.randint(1, 20)
b = random.randint(1, 20)
print(f'sum of number {a} and {b} is {sum(a, b)}')
