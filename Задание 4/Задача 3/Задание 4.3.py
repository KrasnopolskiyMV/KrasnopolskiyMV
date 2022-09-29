# -- coding: utf-8 --
A = int(input('Введите число: '))
B = int(input('Введите число, которое меньше ранее введённого: '))
if A > B:
    for i in range(A, B-1, -1):
        if i % 2 != 0:
            print(i)
else:
    print('Неправильные входные данные')