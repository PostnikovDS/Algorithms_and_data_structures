"""
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
 Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
"""

print(5 & 6)
print(5 | 6)
print(5 ^ 6)
print('--------------')

print(5 << 2) # 101 << 2 == 10100 --> 20
print(bin(5 << 2))
print(int('10100' , 2))
print('--------------')

print(5 >> 2) # 101 >> 2 == 1 --> 1
print(bin(5 >> 2))
print(int('1' , 2))
print('--------------')

print(bin(5)) # 101
print(int('101' , 2)) # 5
