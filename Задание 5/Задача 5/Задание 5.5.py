# -- coding: utf-8 --
number = 1
count = 0
while True:
    try:
        number = int(input('Введите целое неотрицательное число: '))
        if number < 0:
            raise Exception
        if number == 0:
            break
        count += 1
    except:
        print('Неправильные входные данные')
        break
if number == 0:
    print(f'Кол-во символов в последовательности: {count}')