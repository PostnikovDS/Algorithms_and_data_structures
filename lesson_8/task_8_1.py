"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

S = 'brenoritvrezorkre'


def search_strings(s):
    n = len(s)
    arr_str = []
    for i in range(1, n):
        for j in range(n - i + 1):
            k = hash(s[j:j+i])
            if k not in arr_str:
                arr_str.append(k)
    return arr_str


N = len(search_strings(S))
print(f'Количество подстрок: {N}')
