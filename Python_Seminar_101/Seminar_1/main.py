# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# n = int(input('km per day: '))
# m = int(input('total km: '))
#
# print(m / n)
#
#
# print(ord('a'), ord('z'))
# print(ord('A'), ord('Z'))
# print(ord('?'))
#
# list1 = [2, 5, 9, 7, 8, 6]
# list1.sort(reverse=True)
#
# print(''.join(map(str, list1)))

# num = 123558
# list12 = [int(item) for item in str(num)]
# for i in range(len(list12)):
#         list12[i] = list12[i]*list12[i]
#
# print(int(''.join(map(str, list12))))

# def same_case(a, b):
#     check
#     if (97<ord(a)<122 and 97<ord(b)<122) or (65<ord(a)<90 and 65<ord(b)<90):
#         check = 1
#     elif (97<ord(a)<122 and 65<ord(b)<90) or (65<ord(a)<90 and 97<ord(b)<122):
#         check = 1
#     else:
#         check = -1
#     # your code here
#     return check

# n = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# string = "(012) 345-6789"
# for i in range(10):
#     string = string.replace(str(i), str(n[i]))
#     print(n[i])
# print(string)
#
# print(ord('a'))
#
# print('Anvar')
import re


# text = "The sunset sets at twelve o' clock."
# lower_text = list(re.sub(r'[ .,"\'-?:!;]', '', text.lower()))
# for i in range(len(lower_text)):
#     lower_text[i] = str(ord(lower_text[i])-96)
#     print(lower_text[i])
# print(lower_text)
# print(' '.join(lower_text))
# for i in lower_text:
#     i = odr(i)-96

from urllib.parse import urlparse
from urllib.parse import urlsplit

url = "http://www.xakep.ru"

domain = re.split(",", urlparse(url).netloc.replace('.', ','))


print(domain)



# url = url.replace('.', ',')
# url = url.replace('/', ';')
# print(url)
# pars_url = re.split(";|,|\n", url)
# print(pars_url)
# for i in range(len(pars_url)):
#     if i == '':
#         if
#
# my_st = "Я\nучу; язык,программирования\nPython"
# print(re.split(";|,|\n", my_st))
