"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
 Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
import random

num_count = int(input('Введите количество чисел: '))
target_num = input('Введите цифру, которую нужно посчитать: ')

sequence = []
for _ in range(num_count):
    sequence.append(str(random.randint(0,9)))

print('Число =', ''.join(sequence))

n = 0
for el in sequence:
    if el == target_num:
        n += 1

print(f'Количество цифр {target_num} в числе = {n}')

