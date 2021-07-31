"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""


n = int(input('Введите количество предприятий: '))
enterprises = {}
total_income = 0
for i in range(n):
    name = input(f'Введите название {(i + 1)}-го предприятия: ')
    income = int(input('Введите прибыль предприятия: '))
    enterprises[name] = income
    total_income += income

avrg = total_income / n
print("\nСредний прибыль для всех предприятий: ", avrg)
good_ent = []
bad_ent = []

for i in enterprises:
    if enterprises[i] > avrg:
        good_ent.append(i)
    elif enterprises[i] > avrg:
        bad_ent.append(i)

print('Предприятия, чья прибыль выше среднего:')
for el in good_ent:
    print(el)

print('Предприятия, чья прибыль ниже среднего:')
for el in bad_ent:
    print(el)
