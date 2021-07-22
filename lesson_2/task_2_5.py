"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
 Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

result = {chr(n): ord(chr(n)) for n in range(32, 128)}

for num, val in enumerate(result.items(), 1):
    if num % 10:
        print(f'| {num}-й код {val[1]}, значение "{val[0]}"', end=' | ')
    else:
        print(f'| {num}-й код {val[1]}, значение "{val[0]}"', end=' | ')
        print('\n', '-' * 300)
