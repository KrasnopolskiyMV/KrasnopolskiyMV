# -- coding: utf-8 --
N = int(input('Введите число, не меньшее 2: '))
if N >= 2:
    for div in range(2, N):
        if N % div == 0:
            print(div)
            break
    else:
        print(N)
else:
    print('Неправильные входные данные')