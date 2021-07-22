"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

user_num = input('Введите натуральное число: ')

even_num = []
odd_num = []

for el in user_num:
    if int(el) % 2 == 0:
        even_num.append(el)
    else:
        odd_num.append(el)

print(f'Чётные числа --> {even_num}, количество = {len(even_num)}')
print(f'Нечётные числа --> {odd_num}, количество = {len(odd_num)}')
