# -- coding: utf-8 --
n = int(input('Введите натуральное число меньше 9: '))
if n > 0 and n < 9:
    stair = ''
    for i in range(1, n+1):
        stair += str(i)
        print(stair)
else:
    print('Неправильные входные данные')