# -- coding: utf-8 --
def less_number(a, b, c):
    return(min(a, b, c))
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
print('Наименьшее число: ' ,less_number(first, second, third))