# -- coding: utf-8 --
number = 1
count = 0
previousNumber = 0
while True:
    try:
        number = int(input('Введите натуральное число: '))
        if number < 0:
            raise Exception
        if number == 0:
            print(count)
            break
        if number == previousNumber:
            count += 1
        previousNumber = number
    except:
        print('Неправильные входные данные')
        break