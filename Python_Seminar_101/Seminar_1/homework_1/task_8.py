# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input('input first side slice qty: '))
length = int(input('input second side slice qty: '))
k = int(input('input number to check: '))

if (k % width == 0 or k % length == 0) and k < width * length:
    print('yes')
else:
    print('no')
