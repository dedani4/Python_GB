# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

list1 = [random.randint(1, 20) for i in range(int(input("Введите кол-во элементов первого множества: ")))]
list2 = [random.randint(1, 20) for i in range(int(input("Введите кол-во элементов второго множества: ")))]
print(list1)
print(list2)

print(sorted(list(set(list1) & set(list2))))
