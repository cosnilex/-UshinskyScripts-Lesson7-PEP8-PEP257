#!/usr/bin/python3

"""Написать скрипт для движения персонажа влево, вправо, вверх и вниз
по координатам x и y по координатной оси,
начальная позиция персонажа (0;0)
"""

x = 0
y = 0

# Куда мы можем двигаться:
moves = [
    "up", "down",
    "left", "right"
]

print(f'*up, down, left, right*')

# Вводим сторону в которую мы будем двигаться:
move = str(input(f'В какую сторону вы хотите двигаться? '))

if move not in moves:
    # Если сторона не найдена в списке
    # доступных сторон - программа завершается с ошибкой
    # и происходит следующий вывод:
    print('wrong move')
    exit(1)

# Вводим шаг движения в выбранную сторону:
step = int(input(f'На сколько шагов вы хотите сдвинуться? '))

# В зависимости от стороны введённой пользователем
# происходит одно из следующих действий:
if move == 'left':
    y = 0
    if step > 0:
        # шаг должен быть обязательно больше нуля
        x = -step
    else:
        print(f'wrong step, try to change your step')
    print(f'Вы в точке ({x},{y})')
elif move == 'right':
    y = 0
    if step > 0:
        x = step
    else:
        print(f'wrong step, try to change your step')
    print(f'Вы в точке ({x},{y})')
elif move == 'up':
    x = 0
    if step > 0:
        y = step
    else:
        print(f'wrong step, try to change your step')
    print(f'Вы в точке ({x},{y})')
elif move == 'down':
    x = 0
    if step > 0:
        y = -step
    else:
        print(f'wrong step, try to change your step')
    print(f'Вы в точке ({x},{y})')
else:
    print(f'Несуществующий вектор движения, доступные: up, down, left, right')
