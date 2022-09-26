# -- coding: utf-8 --
def leap_year(number):
    if number % 4 == 0 and number % 100 != 0 or number % 400 == 0:
        return 'Да'
    else:
        return 'Нет'
year = int(input('Введите год: '))
print('Является ли год високосным? ', leap_year(year))