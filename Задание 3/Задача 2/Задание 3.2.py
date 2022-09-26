# -- coding: utf-8 --
def square(a, b):
    return(0.5 * a*b)
first = int(input('Введите длину первого катета: '))
second = int(input('Введите длину второго катета: '))
print('Площадь прямоугольного треугольника: ', square(first, second))