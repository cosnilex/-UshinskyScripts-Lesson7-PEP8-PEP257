#!/usr/bin/python3

from math import pi, pow

# Вводим радиус круга по которому будем вычислять площадь:
r = float(input('Введите радиус круга: '))

S = pi * pow(r, 2)
print(f'Площадь круга равна: {S}')
