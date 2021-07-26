'''
7. В одномерном массиве целых чисел определить два наименьших
элемента. Они могут быть как равны между собой (оба являться
минимальными), так и различаться.
'''

import random

my_list = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {my_list}')

min_index_1 = 0
min_index_2 = 1

for i in my_list:
    if my_list[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = my_list.index(i)
    elif my_list[min_index_2] > i:
        min_index_2 = my_list.index(i)

print(f'Два наименьших элемента: {my_list[min_index_1]} и {my_list[min_index_2]}')
