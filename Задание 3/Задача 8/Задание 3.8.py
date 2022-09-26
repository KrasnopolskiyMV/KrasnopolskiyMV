# -- coding: utf-8 --
def numbers(a, b, c):
    if a == b and b == c:
        return 3
    elif (a == b and b != c) or (b == c and c != a) or (a == c and c != b):
        return 2
    else:
        return 0
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
print('Кол-во совпадающих чисел: ', numbers(first, second, third))