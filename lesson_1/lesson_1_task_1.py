"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

while True:
    try:
        user_number = int(input('Введите трёхзначное число: '))
        if len(str(user_number)) != 3:
            print('Пожалуйста, введите ТРЁХЗНАЧНОЕ число')
        elif user_number <= 0:
            print('Пожалуйста, введите ПОЛОЖИТЕЛЬНОЕ трёхзначное число')
        else:
            break
    except ValueError:
        print('Пожалуйста, введите трёхзначное ЧИСЛО')

number_sum = 0
for el in str(user_number):
    number_sum += int(el)
print(f'Сумма цифр введённого числа равна: {number_sum}')

number_multiply = 1
for el in str(user_number):
    number_multiply *= int(el)
print(f'Произведение цифр введённого числа равна: {number_multiply}')

