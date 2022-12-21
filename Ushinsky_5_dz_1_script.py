#!/usr/bin/python3

def func(password):
    """Проверка пароля в соответсвии с условиями

    Принимает:
        password - строка (пароль)
    Возвращает:
        True - если пароль прошёл по условиям
        False - если пароль не прошёл по условиям
    """
    x = True
    # Cчётчик цифр в пароле:
    numbers = 0

    for i in password:
        if i.isdigit():
            # Если оператор находит цифру в пароле
            # счётчик растёт на 1:
            numbers += 1
    # Переводим значение строки password в нижний регистр:
    password = password.lower()
    # Ищем первый индекс начала полного совпадения
    # с вхождением 'password':
    result = password.find(f'password')

    # Проверяем условия у пароля:
    try:
        if len(password) < 6:
            # Длина пароля должна быть 6 символов или более:
            x = False
            raise ValueError(f'Недостаточная длина пароля')
        if numbers == len(password):
            # Пароль не может состоять из цифр:
            x = False
            raise ValueError(f'Ваш пароль состоит из цифр')
        if numbers < 1:
            # В пароле должна быть хоть одна цифра:
            x = False
            raise ValueError(f'В пароле должна быть хотя бы одна цифра')
        if result > -1:
            # Пароль не должен содержать слово 'password':
            x = False
            raise ValueError(f'Пароль не может содержать слово "password"')

    except ValueError as message:
        print(f'{message}')
    return x


print(f'{func(input())}')
