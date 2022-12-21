#!/usr/bin/python3
"""Создать словарь цветов,
в котором ключ - название или кодировка цвета;
значение - кортеж из rgb этого цвета"""

# Создаём кортеж из rgb цветов:
rgb = (
    (255, 0, 0), (255, 165, 0), (255, 255, 0),
    (0, 128, 0), (0, 255, 255), (0, 0, 255),
    (128, 0, 128)
)

# Создаём словарь из цветов и их rgb из кортежа:
colours_dict = {
    'red': rgb[0], 'orange': rgb[1], 'yellow': rgb[2],
    'green': rgb[3], 'aqua': rgb[4], 'blue': rgb[5],
    'purple': rgb[6]
}
# Выводим словарь цветов:
print(f'Словарь цветов: {colours_dict}')
