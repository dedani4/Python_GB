# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


n = int(input('coin qty: '))
eagle, tail = 0, 0
while n > 0:
    coin = int(input())
    n -= 1
    if coin:
        eagle += 1
    else:
        tail += 1
if eagle < tail:
    print(eagle)
else:
    print(tail)
