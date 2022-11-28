# -- coding: utf-8 --
# from random import randint

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

# X = randint(-10, 100)
# N = randint(-10, 100)
X = int(input('Введите натуральное число X: '))
N = int(input('Введите натуральное число N: '))
if X > 0 and N > 0:
    print(X**N / factorial(N))
else:
    print('Неправильные входные данные')