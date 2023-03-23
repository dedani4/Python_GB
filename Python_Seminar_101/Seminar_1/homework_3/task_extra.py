# Создать 2 многочлена разной длины и сложить
import random


def polin(n):
    polynom = str(random.randint(-15, 15))
    for i in range(1, n + 1):
        sign = ' + ' if random.randint(0, 1) else ' - '
        polynom += sign + str(random.randint(1, 15)) + (('x**' + str(i)) if i != 1 else 'x')
    return polynom


def parse_to_dic(polynom):
    polynom_list = polynom.split()
    polynom_dic = {}
    for i in range(len(polynom_list)):
        if 'x**' in polynom_list[i] or 'x' in polynom_list[i]:
            num_str = ''
            while '0' <= polynom_list[i][0] <= '9':
                num_str += polynom_list[i][0]
                polynom_list[i] = polynom_list[i][1:]
            polynom_dic[polynom_list[i]] = int(polynom_list[i - 1] + num_str)

    return polynom_dic


n1 = int(input('Input exponent 1st polynomial: '))
n2 = int(input('Input exponent 2nd polynomial: '))
polynom1 = polin(n1)
polynom2 = polin(n2)
print(polynom1)
print(polynom2)

polynom1_dic = parse_to_dic(polynom1)
polynom2_dic = parse_to_dic(polynom2)
print(polynom1_dic)

result_dic = {}
for key in polynom1_dic if n1 > n2 else polynom2_dic:
    result_dic[key] = polynom1_dic.get(key, 0) + polynom2_dic.get(key, 0)

print(result_dic)
