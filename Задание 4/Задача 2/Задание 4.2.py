# -- coding: utf-8 --
A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))
if A <= B:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, B-1, -1):
        print(i)