#!/usr/bin/python3

# Ключ по которому будем шифровать
# текст из файла (представленный в байтах):
key = str.encode(input())

try:
    with open('text.txt', 'rb') as file:
        text = file.read()
except IOError:
    print(f'Файла не существует')

print(f'Исходный текст в байтах: {text}\n')

crypt = bytearray()
count = len(key)
for abc, c in enumerate(text):
    # Цикл XOR шифрования
    crypt.append(c ^ key[abc % count])
text = bytes(crypt)

try:
    with open('decoding.txt', 'wb') as file:
        file.write(text)
        file.write(b"\n")
except IOError:
    print(f'Файла не существует')

try:
    with open('decoding.txt', 'rb') as file:
        text = file.read()
except IOError:
    print(f'Файла не существует')

print(f'Зашифрованный текст: {text}\n')

crypt = bytearray()
for abc, c in enumerate(text):
    # Цикл XOR расшифрования
    crypt.append(c ^ key[abc % count])
text = bytes(crypt)

try:
    with open('decoding.txt', 'ab') as file:
        file.write(text)
except IOError:
    print(f'Файла не существует')

try:
    with open('decoding.txt', 'rb') as file:
        file.read()
except IOError:
    print(f'Файла не существует')

print(f'Расшифрованный текст:\n{text.decode("utf-8")}')
