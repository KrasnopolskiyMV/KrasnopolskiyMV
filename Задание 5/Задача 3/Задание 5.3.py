# -- coding: utf-8 --
N = int(input('Введите натуральное число: '))
if N > 0:
    num = 1
    step = 0
    space = 1
    while num < N and N - num >= space:
        num *= 2
        step += 1
        space *= 2
    if N == 1:
        num = 0
    print(num, step)
else:
    print('Неправильные входные данные')