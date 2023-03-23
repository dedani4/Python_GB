# Создать 2 многочлена разной длины и сложить
import random


def create_polinom(n):  # Создаем строку-полином
    polynom = str(random.randint(-15, 15)) # разброс коэффициента для х**0(1) от -15 до 15 (еще требуется исключить 0)
    for i in range(1, n + 1):
        sign = ' + ' if random.randint(0, 1) else ' - '  # закладываем пробелы до и после знаков, чтобы
        # потом сплитовать (можно доделать чтобы без пробелов было)
        polynom += sign + str(random.randint(1, 15)) + (('x**' + str(i)) if i != 1 else 'x')
    return polynom


def parse_to_dic(polynom):  # разбиваем строку в словарь, где ключом будут 'х**[]'
    polynom_list = polynom.split()  # сначала строку в список
    polynom_dic = {'0': int(polynom_list[0])}  # создаем словарь и под ключом '0' заносим коэффициент для x**0(1)
    for i in range(len(polynom_list)):
        if 'x' in polynom_list[i]:  # проходим по списку и все элементы с 'х' разбиваем на ключ 'x**[]'
            # и значение - коэффициент
            num_str = ''
            while '0' <= polynom_list[i][0] <= '9':
                num_str += polynom_list[i][0]
                polynom_list[i] = polynom_list[i][1:]
            polynom_dic[polynom_list[i]] = int(
                polynom_list[i - 1] + num_str)  # вносим значение под соответствующим ключом,
            # учитывая знак перед элементом
    return polynom_dic


def sum_polynoms(polynom1_dic, polynom2_dic):  #
    result_dic = {}
    for key in polynom1_dic if n1 > n2 else polynom2_dic:  # суммирование значений по ключам
        result_dic[key] = polynom1_dic.get(key, 0) + polynom2_dic.get(key, 0)

    result = str(result_dic['0']) if result_dic['0'] != 0 else ''  # создание строки-результата и добавление в нее
    # значения для ключа '0'
    if result_dic['x'] < 0:  # добавление значение для ключа 'x' с учетом знака и самого ключа 'x'
        result += ' - ' + (str(abs(result_dic['x'])) if abs(result_dic['x']) != 1 else '') + 'x'
    else:
        result += (' + ' if result_dic['0'] != 0 else '') + (str(result_dic['x']) if result_dic['x'] != 1 else '') + 'x'
    for i in range(2, n1 + 1 if n1 > n2 else n2 + 1):  # добавление остальных ключей и значений с учетом знака
        if result_dic[f'x**{i}'] < 0:
            result += ' - ' + (str(abs(result_dic[f'x**{i}'])) if abs(result_dic[f'x**{i}']) != 1 else '') + f'x**{i}'
        elif result_dic[f'x**{i}'] > 0:
            result += ' + ' + (str(result_dic[f'x**{i}']) if result_dic[f'x**{i}'] != 1 else '') + f'x**{i}'
    return result


n1 = int(input('Input max exponent for 1st polynom: '))
n2 = int(input('Input max exponent for 2nd polynom: '))
polynom1 = create_polinom(n1)
polynom2 = create_polinom(n2)
print(polynom1)
print(polynom2)

print(sum_polynoms(parse_to_dic(polynom1), parse_to_dic(polynom2)))
