# Создать 2 многочлена разной длины и сложить
import random


def create_polinom(n):
    polynom = str(random.randint(-15, 15))
    for i in range(1, n + 1):
        sign = ' + ' if random.randint(0, 1) else ' - '
        polynom += sign + str(random.randint(1, 15)) + (('x**' + str(i)) if i != 1 else 'x')
    return polynom


def parse_to_dic(polynom):
    polynom_list = polynom.split()
    polynom_dic = {}
    polynom_dic['0'] = int(polynom_list[0])
    for i in range(len(polynom_list)):
        if 'x' in polynom_list[i]:
            num_str = ''
            while '0' <= polynom_list[i][0] <= '9':
                num_str += polynom_list[i][0]
                polynom_list[i] = polynom_list[i][1:]
            polynom_dic[polynom_list[i]] = int(polynom_list[i - 1] + num_str)
    return polynom_dic


def sum_polynoms(polynom1_dic, polynom2_dic):
    result_dic = {}
    for key in polynom1_dic if n1 > n2 else polynom2_dic:
        result_dic[key] = polynom1_dic.get(key, 0) + polynom2_dic.get(key, 0)
    result = str(result_dic['0']) if result_dic['0'] != 0 else ''
    if result_dic['x'] < 0:
        result += ' - ' + str(abs(result_dic['x'])) + 'x'
    else:
        result += (' + ' if result_dic['0'] != 0 else '') + str(result_dic['x']) + 'x'

    for i in range(2, n1 + 1 if n1 > n2 else n2 + 1):
        if result_dic[f'x**{i}'] < 0:
            result += ' - ' + str(abs(result_dic[f'x**{i}'])) + f'x**{i}'
        else:
            result += ' + ' + str(result_dic[f'x**{i}']) + f'x**{i}'
    return result


n1 = int(input('Input max exponent for 1st polynom: '))
n2 = int(input('Input max exponent for 2nd polynom: '))
polynom1 = create_polinom(n1)
polynom2 = create_polinom(n2)
print(polynom1)
print(polynom2)
polynom1_dic = parse_to_dic(polynom1)
polynom2_dic = parse_to_dic(polynom2)
print(sum_polynoms(polynom1_dic, polynom2_dic))