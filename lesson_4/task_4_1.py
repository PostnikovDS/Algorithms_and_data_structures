"""
1. "Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их."

>> ВЫВОД:
Имеем две функции, которые выводят списки чётных и нечётных цифр из числа — аргумента функции,
а также считает количество этих цифр.

При этом функция get_str_num преобразует число-аргумент в строку и
проходится по нему как по строке. А функция get_int_num решает задачу с помощью математических операций.

Использовав профайлер cProfile можно сделать вывод, что работа функции get_str_num заняла 0.015 секунд,
а функции get_int_num 0.950 секунд, в 63 раза дольше. Получается, скорость реализации get_str_num гораздо выше.

         95443 function calls in 1.067 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.067    1.067 <string>:1(<module>)
        1    0.015    0.015    0.019    0.019 task_4_1.py:25(get_str_num)
        1    0.950    0.950    0.954    0.954 task_4_1.py:36(get_int_num)
        1    0.045    0.045    1.067    1.067 task_4_1.py:49(main)
        1    0.000    0.000    1.067    1.067 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        7    0.048    0.007    0.048    0.007 {built-in method builtins.print}
    95426    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

>> Использовав модуль timeit, я сделал вывод о том, что с увеличением передоваемого значения в качестве аргумента внутрь
функции get_int_num, незначительно, но линейно растёт время её исполнения.
Поэтому сложность данного алгоритма можно оценить как O(n).

nums = 1
i = 1 || 0.2684054
nums = 1024
i = 2 || 0.6834933999999997
nums = 59049
i = 3 || 0.8083567
nums = 1048576
i = 4 || 1.0381900000000002
nums = 9765625
i = 5 || 1.0595963
nums = 60466176
i = 6 || 1.2502889999999995
nums = 282475249
i = 7 || 1.2811626
nums = 1073741824
i = 8 || 1.4796289000000007
nums = 3486784401
i = 9 || 1.5462783000000009
nums = 10000000000
i = 10 || 1.7686408

"""
import cProfile
from timeit import timeit


def get_str_num(str_num):
    even_num = []
    odd_num = []
    for el in str_num:
        if int(el) % 2 == 0:
            even_num.append(el)
        else:
            odd_num.append(el)
    return even_num, odd_num


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


def main():
    numbers = 3 ** 100000
    str_num = get_str_num(str(numbers))
    int_num = get_int_num(numbers)
    print('*' * 40)
    print(f'Чётные числа --> {str_num[0]}, количество = {len(str_num[0])}')
    print(f'Нечётные числа --> {str_num[1]}, количество = {len(str_num[1])}')
    print('*' * 40)

    print(f'Чётные числа --> {int_num[0]}, количество = {len(int_num[0])}')
    print(f'Нечётные числа --> {int_num[1]}, количество = {len(int_num[1])}')
    print('*' * 40)


if __name__ == '__main__':
    cProfile.run('main()')


for i in range(1, 11):
    nums = i ** 10
    print(f'{nums = }')
    print(f'{i = } ||', timeit(f'get_int_num({nums})', setup='from __main__ import get_int_num'))

