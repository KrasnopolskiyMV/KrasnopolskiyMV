# -- coding: utf-8 --
N = int(input('Введите натуральное число: '))
num = 1
step = 0
space = 1
while num < N and N - num >= space:
    num *= 2
    step += 1
    space *= 2
print(num, step)