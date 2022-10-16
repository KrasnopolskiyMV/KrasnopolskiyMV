# -- coding: utf-8 --
countElements = int(input('Введите длину массива: '))
numbersList = []
maxElement = 0
sumElements = 0
for i in range(countElements):
    print(f'Введите {i} элемент массива: ')
    numbersList.append(float(input()))
    sumElements += numbersList[i]
averageValue = sumElements / len(numbersList)
for i in range(countElements):
    if numbersList[i] == 0:
        numbersList[i] = averageValue
print(f'Полученный массив: {numbersList}')