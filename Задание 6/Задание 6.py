# -- coding: utf-8 --
txt = str(input('Введите текст: '))
countWords = 0
for i in range(len(txt)):
    if i == 0 and (txt[i] == 'е' or txt[i] == 'Е'):
        countWords += 1
    elif (txt[i] == 'е' or txt[i] == 'Е') and txt[i-1] == ' ':
        countWords += 1
print(countWords)