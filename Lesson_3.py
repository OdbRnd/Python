# Логические и условные операторы

# a = int(input("Введите число: "))

# Задание № 1

if  ( (a%2) == 0 ) and (a < 0):
    print("Отрицательное чётное число")
elif ((a%2) != 0 ) and (a > 0):
    print("Положителое нечётное число")
elif (a==0):
    print("Нулевое число")
else:
    print("Не отвечает условию задания")

# Задание № 2

sStr = list(input("Введите строку: "))

# определяем количество гласных букв
count1 = 0
counta = 0
counte = 0
counti = 0
counto = 0
countu = 0
sGlas = "aeiou"
for char in sStr:
    if char in sGlas:
        if char == "a":
            counta += 1
        elif char =="e":
            counte += 1
        elif char  == "i":
            counti += 1
        elif char =="o":
            counto += 1
        else:
            countu += 1
        count1 +=1
# определяем количество согласных букв
count2 = 0
#sGlas = "qwrtypsdfghjklzxcvbnm"
for char in sStr:
    if not (char in sGlas):
        count2 +=1
if (count1 > 0) and (count2 > 0):
    print("Гласных букв:", count1," Согласных букв: ",count2)
elif (count1 > 0) and (count2 == 0):
    print("Гласных букв: ", count1)
elif (count1 == 0) and (count2 > 0):
    print("Согласных букв: ", count2)
else:
    print("False")

if (counta == 0) or (counte == 0) or  (counti == 0) or  (counto == 0) or (countu == 0):
    print("False")
print("Количество буквы \"a\": ", counta)
print("Количество буквы \"e\": ", counte)
print("Количество буквы \"i\": ", counti)
print("Количество буквы \"o\": ", counto)
print("Количество буквы \"u\": ", countu)


# Задание № 3

fInv = float(input("Введите мин. сумму инвестиций: "))
fMike = float(input("Сумма для инвестиций у Майкла: "))
fIvan = float(input("Сумма для инвестиций у Ивана: "))

if (fMike >= fInv) and (fIvan >= fInv):
    print("2")
elif (fMike >= fInv) and (fIvan < fInv):
    print("Mike")
elif (fMike < fInv) and (fIvan >= fInv):
    print("Ivan")
elif (fMike < fInv) and (fIvan < fInv) and ((fMike+fIvan) > fInv):
    print("1")
else:
    print("0")


 