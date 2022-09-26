# -- coding: utf-8 --
def time(n):
    day = 60*24
    n = n % day
    hours = n // 60
    return hours, n % 60
count_minutes = int(input('Введите кол-во минут: '))
hours, minutes = time(count_minutes)
print(f'Текущее время: {hours}:{minutes}')