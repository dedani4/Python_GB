# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
import random

gryadka = [random.randint(1, 10) for _ in range(10)]
print(gryadka)
max_3 = 0
index_3 = []
for i in range(len(gryadka)):

    if gryadka[i] + gryadka[(i + 1) % len(gryadka)] + gryadka[(i + 2) % len(gryadka)] > max_3:
        max_3 = gryadka[i] + gryadka[(i + 1) % len(gryadka)] + gryadka[(i + 2) % len(gryadka)]
        index_3 = [k for k in range(i, (i + 3) % len(gryadka))]
print(max_3, index_3)