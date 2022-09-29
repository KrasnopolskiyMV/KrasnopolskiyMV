# -- coding: utf-8 --
N = int(input('Введите кол-во чисел в сумме: '))
summ = 0
for i in range(N):
    num = int(input('Введите число: '))
    summ += num
print(summ)