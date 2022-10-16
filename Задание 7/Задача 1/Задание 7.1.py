# -- coding: utf-8 --
def isMaxElement(someList):
    maxElem = someList[0]
    for elem in someList:
        if elem > maxElem:
            maxElem = elem
    return maxElem

countElements = int(input('Введите длину массива: '))
numbersList = []
maxElement = 0
for i in range(countElements):
    print(f'Введите {i} элемент массива: ')
    numbersList.append(int(input()))
maxElement = isMaxElement(numbersList)
reversedList = numbersList[::-1]
print(f'Максимальный элемент массива: {maxElement}')
print(f'Полученный массив: {reversedList}')