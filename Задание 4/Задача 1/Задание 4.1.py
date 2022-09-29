# -- coding: utf-8 --
A = int(input('Введите число: '))
B = int(input('Введите число, которое больше или равно ранее введённому: '))
if A <= B:
    for i in range(A, B+1):
        print(i)
else:
    print('Неправильные входные данные')