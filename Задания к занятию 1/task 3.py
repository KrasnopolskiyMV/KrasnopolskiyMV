age = int(input())
name = str(input())
if age > 0 and age < 75 and name != 'Иван':
    if age >= 16 :
        print('Поздравляем вы поступили в ВГУИТ')
    else:
        print('Сначала нужно окончить школу!')
        if age == 15:
            print('Учиться осталось', 16 - age, 'год')
        elif age >= 12 and age <= 14:
            print('Учиться осталось', 16 - age, 'года')
        else:
            print('Учиться осталось', 16 - age, 'лет')