# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


args = input('first element, step and qty of elements with space: ').split()
array = [i for i in range(int(args[0]), int(args[2])*int(args[1]) + int(args[0]), int(args[1]))]

print(array)