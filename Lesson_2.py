# FLOAT.INT и арфметические операции

from math import sqrt

a, b, c = map(float,input("Введите стороны треугольника: ").split())
# # Задание № 1 периметр 
nPerim = a + b + c
print(nPerim)

# # Задание № 2 площадь (формула Герона)
p = (a + b + c) / 2
nSquare = sqrt(p*(p-a)*(p-b)*(p-c))
print(nSquare)

