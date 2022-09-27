# -- coding: utf-8 --
def less_number(a, b, c):
    if a < b and b < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
print('Наименьшее число: ' ,less_number(first, second, third))