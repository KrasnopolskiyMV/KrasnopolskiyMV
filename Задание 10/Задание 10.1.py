# -- coding: utf-8 --
matrix = []
with open('Задание 10/Краснопольский_Максим_Викторович_У-222_vvod.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line[:-1].split(' ')
        for i in range(len(line)):
            line[i] = int(line[i])
        matrix.append(line)
                       
countElem = 0
summElem = 0
for i in range(len(matrix)):
    row = matrix[i]
    for j in range(len(row)):
        if i < j and row[j] > 0:
            countElem += 1
            summElem += row[j]

answers = [str(summElem), ' ', str(countElem)]
with open('Задание 10/Краснопольский_Максим_Викторович_У-222_vivod.txt', 'w') as file:
    file.writelines(answers)