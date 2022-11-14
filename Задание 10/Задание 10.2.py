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

matrix = []
with open('Задание 10/Краснопольский_Максим_Викторович_У-222_vvod.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line[:-1].split(' ')
        for i in range(len(line)):
            line[i] = int(line[i])
        matrix.append(line)

for row in matrix:
    maxElement = maximum(row)
    indexMaxElement = row.index(maxElement)
    row[0], row[indexMaxElement] = row[indexMaxElement],  row[0]
    minElement = minimum(row)
    indexMinElement = row.index(minElement)
    row[-1], row[indexMinElement] = row[indexMinElement],  row[-1]

with open('Задание 10/Краснопольский_Максим_Викторович_У-222_vivod.txt', 'w') as file:
    for row in matrix:
        line = ''
        for num in row:
            line = line + str(num) + '\t'
        line += '\n'
        file.write(line)