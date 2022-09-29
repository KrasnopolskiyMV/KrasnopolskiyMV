# -- coding: utf-8 --
n = int(input('Введите натуральное число: '))
if n > 0:
    summ = 0
    for i in range(1, n+1):
        summ += i**3
    print(summ)
else:
    print('Неправильные входные данные')