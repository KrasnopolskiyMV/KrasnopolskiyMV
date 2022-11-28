# -- coding: utf-8 --
# from random import randint

def maxElement():
    # number = randint(0, 100)
    number = int(input('Введите натуральный элемент последовательности: '))
    if number == 0:
        return 0
    next_number = maxElement()
    if number > next_number:
        return number
    else:
        return next_number

print(f'Наибольшее значение числа в последовательности: {maxElement()}')