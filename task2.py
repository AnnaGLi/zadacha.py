#Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 # min_value = min((float(i), int(i)))

list_1 = [1.1, 1.2, 3.1, 5, 10.01]
max_value = min_value = 0
difference = 0
for i in range(len(list_1)):
    p = list_1[i] - int(list_1[i])
    print(p)
    if max_value < p:
            max_value = p
            i += 1
    if min_value > p:
            min_value = p
            i += 1
            print(max_value, min_value)
difference = max_value - min_value
print(difference)



