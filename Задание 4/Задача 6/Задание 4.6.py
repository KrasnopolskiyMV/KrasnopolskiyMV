# -- coding: utf-8 --
n = int(input('Введите натуральное число: '))
if n > 0:
    factorial = 1
    for i in range (2, n+1):
        factorial *= i
    print(factorial)
else:
    print('Неправильные входные данные')