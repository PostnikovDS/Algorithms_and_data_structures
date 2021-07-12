"""
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

user_int = input('Введите два целых числа через пробел: ').split()
for idx in range(len(user_int)):
    user_int[idx] = int(user_int[idx])
print(f'Случайное целое число от {user_int[0]} до {user_int[1]}:'
      f' --> {random.randint(user_int[0], user_int[1])}')

print('*' * 25)

user_float = input('Введите два вещественных числа через пробел: ').split()
for idx in range(len(user_float)):
    user_float[idx] = float(user_float[idx])
print(f'Случайное вещественное число от {user_float[0]} до {user_float[1]}:'
      f' --> {random.random() * (user_float[1] - user_float[0]) + user_float[0]}')

print('*' * 25)

try:
    user_letters = input('Введите две буквы английского алфавита через пробел: ').lower().split()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_slice = alphabet[alphabet.index(user_letters[0]):alphabet.index(user_letters[1]) + 1]
    print(f'Случайная буква от {user_letters[0]} до {user_letters[1]} '
          f'в английском алфавите: --> "{random.choice(alphabet_slice)}"')
except IndexError:
    print('Нельзя нарушать порядок букв алфавита')
