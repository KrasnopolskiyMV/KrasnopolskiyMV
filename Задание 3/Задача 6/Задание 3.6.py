
# -- coding: utf-8 --
def colors(a1, a2, b1, b2):
    if (((a1 % 2 == 0 and a2 % 2 == 0) or (a1 % 2 != 0 and a2 % 2 != 0)) and 
    ((b1 % 2 == 0 and b2 % 2 == 0) or (b1 % 2 != 0 and b2 % 2 != 0))):
        return 'Да'
    else:
        return 'Нет'
firstX = int(input('Введите номер строки первой клетки шахматной доски: '))
firstY = int(input('Введите номер cтолбца шахматной первой клетки доски: '))
secondX = int(input('Введите номер строки шахматной второй клетки доски: '))
secondY = int(input('Введите номер столбца шахматной второй клетки доски: '))
print('Покрашены ли клетки в один цвет? ', colors(firstX, firstY, secondX, secondY))