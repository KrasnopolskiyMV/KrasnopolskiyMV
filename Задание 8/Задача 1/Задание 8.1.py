# -- coding: utf-8 --
def spaceFigures(typeFigure):
    lenghtsFigure = []
    if typeFigure == 'Треугольник':
        lenghtsFigure.append(int(input('Введите длину высоты треугольника: ')))
        lenghtsFigure.append(int(input('Введите длину стороны треугольника, к которой проведена высота: ')))
        space = 0.5 * lenghtsFigure[0] * lenghtsFigure[1]
        return f'Площадь данного треугольника равна {space}'
    elif typeFigure == 'Прямоугольник':
        lenghtsFigure.append(int(input('Введите длину прямоугольника: ')))
        lenghtsFigure.append(int(input('Введите ширину прямоугольника: ')))
        space = lenghtsFigure[0] * lenghtsFigure[1]
        return f'Площадь данного прямоугольника равна {space}'
    elif typeFigure == 'Параллелограмм':
        lenghtsFigure.append(int(input('Введите длину высоты параллелограмма: ')))
        lenghtsFigure.append(int(input('Введите длину стороны параллелограмма, к которой проведена высота: ')))
        space = lenghtsFigure[0] * lenghtsFigure[1]
        return f'Площадь данного параллелограмма равна {space}'
    elif typeFigure == 'Трапеция':
        lenghtsFigure.append(int(input('Введите длину первого основания трапеции: ')))
        lenghtsFigure.append(int(input('Введите длину второго основания трапеции: ')))
        lenghtsFigure.append(int(input('Введите длину высоты трапеции: ')))
        space = 0.5 * (lenghtsFigure[0] + lenghtsFigure[1]) * lenghtsFigure[2]
        return f'Площадь данной трапеции равна {space}'
    elif typeFigure == 'Окружность':
        pi = 3.14
        r = int(input('Введите длину радиуса окружности: '))
        space = pi * r**2
        return f'Площадь данной окружности равна равна {space}'
    else:
        return 'Неизвестный тип геометрической фигуры'
figureType = str(input('Введите тип геометрической фигуры: '))
print(spaceFigures(figureType))