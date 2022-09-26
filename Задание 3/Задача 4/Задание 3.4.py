# -- coding: utf-8 --
def shoes(a, b, l, N):
    lenght = a*(N-1) + b*(N-1) + l*2
    return lenght
count = int(input('Введите кол-во дырочек для шнуровки в ботинке в одном ряду: '))
len1 = int(input('Введите расстояние между рядами дырочек для шнуровки: '))
len2 = int(input('Введите расстояние между дырочками для шнуровки: '))
len3 = int(input('Введите длину свободного конца шнурка: '))
print(shoes(len1, len2, len3, count))