# программа запришивет кол-во сторон у пользователя и выводит название этой фигуры

figure = int(input('введите кол-во сторон цифрой от 3 до 10: '))
if figure == 3:
    print('триугольник')
if figure == 4:
    print('квадрат')
if figure == 5:
    print('пентогон')
if figure == 6:
    print('гексагон')
if figure == 7:
    print('гептагон')
if figure == 8:
    print('октогон')
if figure == 9:
    print('нонагон')
if figure == 10:
    print('декагон')
if figure < 3:
    print('МОЖНО ВВОДИТЬ ТОЛЬКО ОТ 3')
if figure > 3:
    print('МОЖНО ВВОДИТЬ ТОЛЬКО ДО 10 СТОРОН')