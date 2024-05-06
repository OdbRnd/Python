# РАБОТА С ДАННЫМИ 

# Множества

# Задание № 1

nCnt = int(input("Введите кол-во чисел: ")) # сколько чисел вводить
lFl = True
while lFl:
    nTmp = list(map(int, input("Введите чисела строкой: ").split())) # список чисел при вводе
    if nCnt != len(nTmp):
        print("Кол-во введённых чисел не соотвествует ", nCnt, "! Введите заново !")
        nTmp.clear()
    else:
        lFl = False
nLen =  len(nTmp)
for i in range(nLen):
    if nTmp[i] < 0:
        nTmp[i] *= -1
mnTmp = set(nTmp) # множество

nLen1 = len(mnTmp)

if nLen != nLen1:
    print("Количество различных чисел: ", nLen1)
else:
    print("Все различные числа !")

# Задание № 2

# вводим 1-й список
lFl = True
Spisok = [] 
print("Числа 1-го списка.")
while lFl:
    sTmp = input("Введите число (закочить ввод \"@\"): ")
    if sTmp != "@":
        Spisok.append(int(sTmp))
    else:
        lFl = False
Dorens1 = set(Spisok)

#  вводим 2-й список
lFl = True
Spisok = [] 
print("Числа 2-го списка.")
while lFl:
    sTmp = input("Введите число (закочить ввод \"@\"): ")
    if sTmp != "@":
        Spisok.append(int(sTmp))
    else:
        lFl = False
Dorens2 = set(Spisok)
Dorens3 = Dorens1.intersection(Dorens2)  # или можно использовать данную кострукцию: Dorens3 = Dorens1 & Dorens2

print(Dorens1)
print(Dorens2)
print("Кол-во чисел в 1-м и во 2-м списках, содержащихся одновременно: ", len(Dorens3))

# Задание № 3

nSpisok = list(map(int, input("Введите чисела строкой: ").split())) # список чисел при вводе
msFind = set()
for i in nSpisok:
    if i in msFind:
        print("YES")
    else:
        print("NO")
        msFind.add(i)



