# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

a = int(input('Input number > 0: '))
fib1 = 0
fib2 = 1
n = 1
while fib2 < a:
    fib2 += fib1
    fib1 = fib2 - fib1
    n += 1
if fib2 == a:
    print(n)
else:
    print(-1)