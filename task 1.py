# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Введите номер дня недели: '))

if 0 < day <= 5:
    print('Это не выходной.')

elif 5 < day <= 7:
    print('Это выходной')

else:
    print('Дня недели под таким номером нет')
