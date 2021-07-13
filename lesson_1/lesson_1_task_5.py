"""
5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

user_letters = input('Введите две буквы английского алфавита через пробел: ').lower().split()
letter_1 = ALPHABET.index(user_letters[0])
letter_2 = ALPHABET.index(user_letters[1])

if letter_1 > letter_2:
      letters_between_slice = ALPHABET[letter_2 + 1:letter_1]
else:
      letters_between_slice = ALPHABET[letter_1 + 1:letter_2]

print(f'Буква "{user_letters[0]}" стоит на {letter_1 + 1}-м месте в алфавите,'
      f' а буква "{user_letters[1]}" – на {letter_2 + 1}-м.\n'
      f'Между ними находится {len(letters_between_slice)} букв.')


