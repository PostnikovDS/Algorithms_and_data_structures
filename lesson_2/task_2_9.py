"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
 Вывести на экран это число и сумму его цифр.
"""

def get_num_sum(num):
    result = 0
    for el in num:
        result += int(el)
    return result


user_num = input('Введите натуральные числа через пробел: ').split()
max_num_sum = 0
target_num = ''
for el in user_num:
    num_sum = get_num_sum(el)
    if num_sum > max_num_sum:
        max_num_sum = num_sum
        target_num = el

print(f'Наибольшее по сумме цифр из введёных чисел --> {target_num}\n '
      f'Сумма цифр этого числа равна --> {max_num_sum}')


# max_num_sum = 0
# num_sum = 0
# for el in user_num:
#     for num in el:
#         num_sum += int(num)
#     if num_sum > max_num_sum:
#         max_num_sum = num_sum
#
# print(max_num_sum)