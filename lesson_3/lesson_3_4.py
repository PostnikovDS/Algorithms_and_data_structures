'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random

my_list = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {my_list}')

max_index = 0
for i in my_list:
    if my_list.count(max_index) < my_list.count(i):
        max_index = my_list.index(i)

print(f'Число {my_list[max_index]}, встречается {my_list.count(max_index)} раза')
