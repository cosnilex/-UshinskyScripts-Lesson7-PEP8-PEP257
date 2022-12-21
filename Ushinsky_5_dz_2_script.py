#!/usr/bin/python3

import functools


def func(*args):
    """Сумма произвольного количества параметров

        Принимает:
            *args - число, строка, список в произвольном количестве.
        Возвращает:
            Сумму параметров
    """
    # В функции можно суммировать int, float, string, list, tuple
    # с помощью модуля functools и его функции reduce
    # которая принимает функцию, которую требуется применить
    # к элементам последовательности
    # и последовательность, элементы которой
    # требуется свести к единственному значению
    return functools.reduce((lambda x, y: x + y), args)


try:
    print(f'{func("abc","def","ghi")} ')

except UnboundLocalError:
    print(f'Введено ноль значений')

except TypeError:
    print(f'Введено ноль значений')
