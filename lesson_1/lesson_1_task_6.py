"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

user_number = ALPHABET[int(input('Введите номер буквы в алфавите: ')) - 1]

print(f'Буква в алфавите --> {user_number}')
