# -- coding: utf-8 --
n = int(input('Введите натуральное число: '))
if n > 0:
    summ = 0
    factor = 1
    for i in range (1, n+1):
        factor *= i
        summ += factor
    print(summ)
else:
    print('Неправильные входные данные')