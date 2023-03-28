# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
import random


def exponentiation(number, exponent):
    if exponent == 0:
        return 1
    return a * exponentiation(number, exponent - 1)


a = random.randint(1, 20)
b = random.randint(1, 20)
print(f'number {a} to the {b} power is {exponentiation(a, b)} \n                    (check: {a ** b})')
