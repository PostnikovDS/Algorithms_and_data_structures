"""
8. Определить, является ли год, который ввел пользователем, високосным или не високосным.
"""

user_year = int(input('Введите год, чтобы узнать — является ли он високосным: '))

if user_year % 4 != 0:
    print(f'{user_year} год НЕ високосный')
else:
    if user_year % 100 != 0:
        print(f'{user_year} год високосный')
    else:
        if user_year % 400 == 0:
            print(f'{user_year} год високосный')
        else:
            print(f'{user_year} год НЕ високосный')
