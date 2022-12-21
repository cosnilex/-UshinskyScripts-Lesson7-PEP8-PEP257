#!/usr/bin/python3

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
operation = str(input('операция: '))


def calc(a, b,
            operation):
    """Калькулятор чисел

    Принимает:
        a - первое число
        b - второе число
        operation - действие над числами
    Возвращает:
        Результат операции над числами
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == '**':
        return a ** b
    elif operation == '%':
        return a % b
    elif operation == '//':
        return a // b
    else:
        return (f'wrong operator')


print(f'{calc(a,b,operation)}')
