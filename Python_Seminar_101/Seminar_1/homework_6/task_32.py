# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

args = input('input min amd max: ').split()

list1 = [random.randint(1, 100) for _ in range(20)]
print(list1)
print(f'from {args[0]} to {args[1]}')
indexes = []
for i in range(len(list1)):
    if int(args[0]) <= list1[i] <= int(args[1]):
        indexes.append(i)
print(indexes)
