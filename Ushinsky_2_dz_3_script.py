#!/usr/bin/python3

# Вводим строку, у которой будем выводить последние
# два символа наоборот:
string = str(input('Введите строку: '))

print(f'{string[-1:-3:-1]}')
