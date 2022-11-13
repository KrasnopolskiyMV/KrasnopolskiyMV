# -- coding: utf-8 --
def summElements(exampleList):
    summElem = 0
    for i in range(len(exampleList)):
        summElem += exampleList[i]
    return summElem
def averageNumber(exampleList):
    averageNum = summElements(exampleList) / len(exampleList)
    return averageNum

for i in range(1, 4):
    massive = []
    lenght = int(input(f'Введите длину {i} массива: '))
    for j in range(lenght):
        massive.append(int(input(f'Введите {j} элемент массива: ')))
    print(f'Сумма элементов {i} массива: {summElements(massive)}')
    print(f'Среднеарифметическое значение {i} массива: {averageNumber(massive)}', '\n')