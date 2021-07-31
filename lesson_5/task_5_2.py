"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
"""

from collections import deque

HEXADECIMAL = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9,'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1',
               2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
               9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_hex(x, y):
    result = deque()
    transfer = 0
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = HEXADECIMAL[x.pop()] + HEXADECIMAL[y.pop()] + transfer
        else:
            res = HEXADECIMAL[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(HEXADECIMAL[res])
        else:
            result.appendleft(HEXADECIMAL[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')
    return list(result)


def mult_hex(x, y):
    result = deque()
    spam = deque([deque() for _ in range(len(y))])
    x, y = x.copy(), deque(y)
    for i in range(len(y)):
        m = HEXADECIMAL[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * HEXADECIMAL[x[j]])
        for _ in range(i):
            spam[i].append(0)
    transfer = 0
    for _ in range(len(spam[-1])):
        res = transfer
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res < 16:
            result.appendleft(HEXADECIMAL[res])
        else:
            result.appendleft(HEXADECIMAL[res % 16])
            transfer = res // 16
    if transfer:
            result.appendleft(HEXADECIMAL[transfer])
    return list(result)


print('Введите два шестнадцатеричных числа:')
a_num = list(input('\tВведите число a = ').upper())
b_num = list(input('\tВведите число b = ').upper())

print(*a_num, '+', *b_num, '=', *sum_hex(a_num, b_num))
print(*a_num, '*', *b_num, '=', *mult_hex(a_num, b_num))

