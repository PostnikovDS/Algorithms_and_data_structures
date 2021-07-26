"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

my_list = [random.randint(-99, 99) for _ in range(100)]
print(f'Массив: {my_list}')

min_index = 0

for i in my_list:
    if my_list[min_index] > i:
        min_index = my_list.index(i)

if my_list[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: "{my_list[min_index]}".',
            f'Находится в массиве на позиции {min_index}.')
