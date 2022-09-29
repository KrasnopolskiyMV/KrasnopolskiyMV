# -- coding: utf-8 --
def line_fib(n):
    if n == 1 or n == 2:
        return 1
    return line_fib(n - 1) + line_fib(n - 2)
N = int(input('Введите кол-во чисел виз ряда Фибоначчи: '))
K = int(input('Введите номер элемента ряда: '))
if N > 0 and K > 0:
    summ = 0
    for i in range(K, N+1):
        summ += line_fib(i)
    print(summ)
else:
    print('Неправильные входные данные')