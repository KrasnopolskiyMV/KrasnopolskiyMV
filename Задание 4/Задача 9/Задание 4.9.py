# -- coding: utf-8 --
N = int(input('Введите кол-во чисел в ряде Фибоначчи: '))
if N == 0:
    print(0)
elif N == 1:
    print(1)
elif N == 2:
    print(2)
elif N > 2:
    fib1 = 1
    fib2 = 1
    summ = 2
    for i in range(N-2):
        new_elem = fib1 + fib2
        fib1 = fib2
        fib2 = new_elem
        summ += new_elem
    print(summ)
else:
    print('Неправильные входные данные')