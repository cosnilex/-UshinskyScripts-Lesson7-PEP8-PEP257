#!/usr/bin/python3

"""Сколько молекул спирта?"""

# Минимальные значения каждого атома:
minC = 2
minH = 6
minO = 1


with open('Input.txt', 'r') as file_input:
    try:
        # Считываем и записываем в переменные
        # значения из файла 'Input.txt':
        C = int(f'{file_input.readline()}')
        H = int(f'{file_input.readline()}')
        O = int(f'{file_input.readline()}')
    except (ValueError, TypeError):
        print('Только целые натуральные числа')
file_input.close()
# Значение молекулы по-умолчанию:
molekula = 0
try:
    if (C <= 0 or
        H <= 0 or
        O <= 0
        ):
        # Если условие истинно, молекул - 0:
        molekula = 0
        with open('Output.txt', 'w') as file_output:
            file_output.write(f'{str(molekula)}')
    while (C >= minC and
           H >= minH and
           O >= minO):
        # Если условие истинно,
        # выполняем следующие действия:
        C -= minC
        H -= minH
        O -= minO
        # Пока условие явялется истинным,
        # прибавляем к молекуле еденицу:
        molekula += 1
except NameError:
    print('Ошибка значений')

with open('Output.txt', 'w') as file_output:
    file_output.write(f'{str(molekula)}')

with open('Output.txt', 'r') as file_output:
    print(f'{file_output.read()}')
