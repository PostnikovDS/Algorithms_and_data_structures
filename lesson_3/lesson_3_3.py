"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

my_list = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {my_list}')

max_num = my_list[0]
min_num = my_list[0]

for i in my_list:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i

min_index = my_list.index(min_num)
max_index = my_list.index(max_num)
my_list[min_index], my_list[max_index] = my_list[max_index], my_list[min_index]
print(f'Массив после изменения элементов {min_index} и {max_index}: {my_list}')
