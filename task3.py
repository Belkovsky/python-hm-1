# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

def CoordinateCheck(a, b):
    if a and b > 0:
        result = 1
    if a < 0 and b > 0:
        result = 2
    if a and b < 0:
        result = 3
    if a > 0 and b < 0:
        result = 4
    return result


x = int(input('Введите значение X: '))
while x == 0:
    x = int(input('Значение X не должно быть 0, введите другое значение: '))

y = int(input('Введите значение Y: '))
while y == 0:
    y = int(input('Значение Y не должно быть равно 0, введите другое значение: '))

print(f'Точка находится в {CoordinateCheck(x,y)} четверти')
