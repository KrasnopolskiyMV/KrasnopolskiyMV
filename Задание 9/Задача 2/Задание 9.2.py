# -- coding: utf-8 --
def minimum(exampleList):
    minElement = exampleList[0]
    for i in range(1, len(exampleList)):
        if exampleList[i] < minElement:
            minElement = exampleList[i]
    return minElement

def maximum(exampleList):
    maxElement = exampleList[0]
    for i in range(1, len(exampleList)):
        if exampleList[i] > maxElement:
            maxElement = exampleList[i]
    return maxElement

def main():
    N = int(input('Введите кол-во строк в массиве: '))
    M = int(input('Введите кол-во столбцов в массиве: '))
    matrix = []
    for i in range(N):
        currentList = []
        for j in range(M):
            currentList.append(int(input(f'Введите [{i}, {j}] элемент: ')))
        matrix.append(currentList)

    for row in matrix:
        maxElement = maximum(row)
        indexMaxElement = row.index(maxElement)
        row[0], row[indexMaxElement] = row[indexMaxElement],  row[0]
        minElement = minimum(row)
        indexMinElement = row.index(minElement)
        row[-1], row[indexMinElement] = row[indexMinElement],  row[-1]
    
    print('Изменённая матрица: ')
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end='\t')
        print()
main()