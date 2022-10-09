# -- coding: utf-8 --
number = 1
summ = 0
count = 0
while True:
    try:
        number = int(input('Введите число: '))
        if number == 0:
            break
        summ += number
        count += 1
    except:
        print('Неправильные входные данные')
        break
if number == 0 and count != 0:
    middle = summ/count
    print(f'Среднее значение: {middle}')
else:
    print('Среднее значение: 0')