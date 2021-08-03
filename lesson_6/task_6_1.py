"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

# Версия Python: python 3.8
# ОС: Windows 10 x64

# Под переменную user_number было задействованно 638 байт памяти
# Под переменную str_num было задействованно 56 байт памяти
# Под переменную int_num было задействованно 56 байт памяти

# Под все переменные задействованно 750 байт памяти

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19     18.3 MiB     18.3 MiB           1   @profile
    20                                         def get_str_num(str_num):
    21     18.3 MiB      0.0 MiB           1       even_num = []
    22     18.3 MiB      0.0 MiB           1       odd_num = []
    23     18.3 MiB      0.0 MiB          60       for el in str_num:
    24     18.3 MiB      0.0 MiB          59           if int(el) % 2 == 0:
    25     18.3 MiB      0.0 MiB          26               even_num.append(el)
    26                                                 else:
    27     18.3 MiB      0.0 MiB          33               odd_num.append(el)
    28     18.3 MiB      0.0 MiB           1       return even_num, odd_num


Filename: E:/Courses/Algorithms_and_data_structures/lesson_6/task_6_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     18.3 MiB     18.3 MiB           1   @profile
    32                                         def get_int_num(int_num):
    33     18.3 MiB      0.0 MiB           1       even_num = []
    34     18.3 MiB      0.0 MiB           1       odd_num = []
    35     18.3 MiB      0.0 MiB          60       while int_num:
    36     18.3 MiB      0.0 MiB          59           num = int_num % 10
    37     18.3 MiB      0.0 MiB          59           if num % 2 == 0:
    38     18.3 MiB      0.0 MiB          26               even_num.append(num)
    39                                                 else:
    40     18.3 MiB      0.0 MiB          33               odd_num.append(num)
    41     18.3 MiB      0.0 MiB          59           int_num = int_num // 10
    42     18.3 MiB      0.0 MiB           1       return even_num, odd_num

ВЫВОД:
Переменная user_number, содержащая в себе строку, требует выделения наибольшего количества памяти.
Функции get_str_num и get_int_num одинаково требуют 18.3 MiB
"""

import sys
from memory_profiler import profile

# task 2-2: Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


@profile
def get_str_num(str_num):
    even_num = []
    odd_num = []
    for el in str_num:
        if int(el) % 2 == 0:
            even_num.append(el)
        else:
            odd_num.append(el)
    return even_num, odd_num


@profile
def get_int_num(int_num):
    even_num = []
    odd_num = []
    while int_num:
        num = int_num % 10
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
        int_num = int_num // 10
    return even_num, odd_num


user_number = str(3 ** 1234)
str_num = get_str_num(user_number)
int_num = get_int_num(int(user_number))

print(f'{user_number = }')
print(f'{str_num = }')
print(f'{int_num = }')
print('*' * 40)

sum_ = 0
var_lst = (user_number, str_num, int_num)
for n, i in enumerate(var_lst):
    var_lst_name = ('user_number', 'str_num', 'int_num')
    sum_ += sys.getsizeof(i)
    print(f'Под переменную {var_lst_name[n]} было задействованно {sys.getsizeof(i)} байт памяти')

print(f'\nПод все переменные задействованно {sum_} байт памяти')
