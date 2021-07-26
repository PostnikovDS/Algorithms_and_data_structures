'''
6. В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать.
'''

import random

my_list = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {my_list}')

min_index = 0
max_index = 0
step = 1
sum = 0

for i in my_list:
    if my_list[min_index] > i:
        min_index = my_list.index(i)
    elif my_list[max_index] < i:
        max_index = my_list.index(i)

if max_index - min_index < 0:
    step = -1

for i in my_list[min_index + step:max_index:step]:
    sum += i

print(
    f'Сумма элементов между минимальным ({my_list[min_index]})',
    f' и максимальным ({my_list[max_index]}) элементами: {sum}'
)