# -- coding: utf-8 --
N = int(input('Введите кол-во строк и столбцов в массиве: '))
matrix = []
for i in range(N):
    currentList = []
    for j in range(N):
        currentList.append(int(input(f'Введите [{i}, {j}] элемент: ')))
    matrix.append(currentList)

countElem = 0
summElem = 0
for i in range(N):
    for j in range(N):
        if i < j and matrix[i][j] > 0:
            countElem += 1
            summElem += matrix[i][j]

print(f'Сумма положительных элементов матрицы, находящихся над главной диагональю: {summElem}')
print(f'Число положительных элементов матрицы, находящихся над главной диагональю: {countElem}')