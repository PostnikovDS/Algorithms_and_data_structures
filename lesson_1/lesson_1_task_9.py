"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше
другого).
"""
print('Введите три числа:')
a_num = float(input('\tпервое число: '))
b_num = float(input('\tвторое число: '))
c_num = float(input('\tтретье число: '))

try:
    if a_num > b_num > c_num or c_num > b_num > a_num:
        middle_num = b_num
    elif b_num > a_num > c_num or c_num > a_num > b_num:
        middle_num = a_num
    elif a_num > c_num > b_num or b_num > c_num > a_num:
        middle_num = c_num

    print('Среднее число:', middle_num)
except:
    print('Что то пошло не так')
