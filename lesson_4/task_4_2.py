"""
2. "Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом."

>> ВЫВОД:
Обычный алгоритм отработал за 8.734 сек,
а с использованием решета Эратосфена всего за 0.021 сек!!!

        11942 function calls in 8.757 seconds
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.757    8.757 <string>:1(<module>)
        1    8.734    8.734    8.735    8.735 task_4_2.py:12(without_eratosten)
        1    0.021    0.021    0.021    0.021 task_4_2.py:23(with_eratosten)
        1    0.000    0.000    8.757    8.757 task_4_2.py:47(main)
        1    0.000    0.000    8.757    8.757 {built-in method builtins.exec}
    11936    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


>> Использование модуля timeit показало, что время исполнения функции without_eratosten
растёт в логарифметической прогрессии, значит сложность алгоритма = O(log n):

nums = 1
i = 1 || 0.24357449999999936
nums = 4
i = 2 || 1.0319325
nums = 9
i = 3 || 2.5527289
nums = 16
i = 4 || 4.9920445
nums = 25
i = 5 || 9.2252185
nums = 36
i = 6 || 13.932104599999999
nums = 49
i = 7 || 22.776520400000003

0.24357 / 1 = 0.244 сек
1.03193 / 4 = 0,258 сек
2.55272 / 9 = 0,284 сек
4.99204 / 16 = 0,312 сек
9.22521 / 25 = 0,369 сек

>> Соответсвующие расчёты в отношении функции with_eratosten показали, что время увеличивается пропорционально,
линейно с увеличением значения аргумента. Следовательно, сложность алгоритма O(n).

nums = 1
i = 1 || 0.48365999999999865
nums = 4
i = 2 || 1.0473448999999988
nums = 9
i = 3 || 2.041521300000001
nums = 16
i = 4 || 3.5980556999999997
nums = 25
i = 5 || 5.7065418
nums = 36
i = 6 || 8.305732500000001
nums = 49
i = 7 || 11.163666199999998

"""
import cProfile
from timeit import timeit


def without_eratosten(n):
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return (lst)


def with_eratosten(n):
    a = [0] * n
    for i in range(n):
        a[i] = i

    # a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return(b)


def main():
    numbers = 3 ** 10
    without_eratosten(numbers)
    with_eratosten(numbers)
    # print(without_eratosten(numbers))
    # print(without_eratosten(numbers))


if __name__ == '__main__':
    cProfile.run('main()')


for i in range(1, 8):
    nums = i ** 2
    print(f'{nums = }')
    print(f'{i = } ||', timeit(f'without_eratosten({nums})', setup='from __main__ import without_eratosten'))
    print('*' * 40)


for i in range(1, 8):
    nums = i ** 2
    print(f'{nums = }')
    print(f'{i = } ||', timeit(f'with_eratosten({nums})', setup='from __main__ import with_eratosten'))
