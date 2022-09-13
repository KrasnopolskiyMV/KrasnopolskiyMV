# -- coding: utf-8 --
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
print('Числа, принадлежащие интервалу [1, 3]:')
if first >= 1 and first <= 3:
    print(first)
if second >= 1 and second <= 3:
    print(second)
if third >= 1 and third <= 3:
    print(third)
if (first < 1 or first > 3) and (second < 1 or second > 3) and (third < 1 or third > 3):
    print('Таковые отсутствуют')