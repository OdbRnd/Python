# Работа с данными

# Циклы While & For

# Задание 1 цикл While & For
nCol = int(input("Введите количество чисел: "))
nCnt = 0
while nCol > 0: # / for i in range(nCol):
    nDig = int(input("Введите число: "))
    if nDig == 0:
        nCnt += 1
    nCol -= 1   # отсутствует данная строка
print("Количество чисел, равных нулю: ", nCnt)

# Задание № 2
nDig = int(input("Введите число: "))
nCnt = 0
i = 1
while i <= nDig: # for i in range(1, nDig)
    if  ((nDig / i) - int (nDig / i) ) == 0:
        nCnt +=1
    i += 1        # отсутствует данная строка
print("Количество натуральных делителей: ", nCnt)

# Задание № 3
nA = int(input("Введите 1-е число: "))
nB = int(input("Введите 2-е число: "))
if nA <= nB:
    for i in range(nA, nB):
        if ( i % 2 ) == 0:
            print(i, end = " ")


