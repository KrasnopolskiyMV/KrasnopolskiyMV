# -- coding: utf-8 --
def division(n, m, k):
    if k % n == 0 or k % m == 0:
        return 'Да'
    else:
        return 'Нет'
len1 = int(input('Введите длину шоколадки: '))
len2 = int(input('Введите ширину шоколадки: '))
count = int(input('Введите кол-во долек, которые нужно отломить : '))
print('Можно ли отломить от шоколадки часть с таким кол-вом долек? ', division(len1, len2, count))