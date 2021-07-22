"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

user_num = int(input('Введите количество n элементов: '))
num_row = [1]
el = 1

while user_num != len(num_row):
    if len(num_row) % 2 == 0:
        el = el / 2 * -1
        num_row.append(el)
    else:
        el = el / 2
        num_row.append(el)

result_sum = sum(num_row)
print(f'элементы: {num_row}')
print(f'сумма элементов: {result_sum}')
