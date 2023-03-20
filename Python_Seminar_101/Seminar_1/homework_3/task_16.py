# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

array_size = int(input('input size of array: '))
array = [int(input(f"input element {i} to array: ")) for i in range(array_size)]
number = int(input('input number for check: '))

print(array.count(number))
