#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number_1 = int(input('Enter a number: '))
b = ''
while number_1 > 0:
    b = str(number_1 % 2) + b
    number_1 = number_1 // 2
print(b)


