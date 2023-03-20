# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

array_size = int(input('input size of array: '))
array = [int(input(f"input element {i} to array: ")) for i in range(array_size)]
number = int(input('input number for check: '))

check = abs(array[0] - number)
i_check = 0

for i in range(1, array_size):
    if abs(array[i] - number) < check:
        check = abs(array[i] - number)
        i_check = i

print(array[i_check])
