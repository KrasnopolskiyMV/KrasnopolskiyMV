# -- coding: utf-8 --
one_day = 3600 * 24
one_hour = 3600
one_minute = 60

seconds = int(input('Введите кол-во секунд: '))
days = seconds // one_day
hours = (seconds % one_day) // one_hour
minutes = (seconds % one_hour) // one_minute
seconds = seconds % one_minute
print(f"{days}:{hours}:{minutes}:{seconds}")