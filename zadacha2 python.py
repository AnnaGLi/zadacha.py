#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

x1 = int(input('enter x1'))
y1 = int(input('enter y1'))
point1 = [x1, y1]

x2 = int(input('enter x2'))
y2 = int(input('enter y2'))
point2 = [x2, y2]

distance = math.sqrt((((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2)))
print(distance)




