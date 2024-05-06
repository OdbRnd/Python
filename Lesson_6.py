# РАБОТА С ДАННЫМИ 

# СТРОКИ

# Задание № 1
sStr = input("Введите строку без пробелов: ")
# sStr1 = sStr[len(sStr)::-1]
#$if sStr == sStr1:     print("Yes")
#else:     print("No")
if sStr == (sStr[len(sStr)::-1]): print("Yes")
else: print("No")

# ============================================

# Задание № 2
import re

sStr = input("Введите строку: ")

# Версия 1

print(sStr)
sStr = re.sub(r'\s+',' ', sStr)
print(sStr)

#---------------------------------------------

# Версия 2
print(sStr, " ", len(sStr))
bFl = False
i = 0
nEnd = len(sStr)-1
while i <= nEnd:
    if (ord(sStr[i]) == 32) and (not bFl):
        bFl = True
        i += 1
    elif (ord(sStr[i]) == 32) and bFl:
        sStr = sStr[:i] + sStr[i+1:]
        nEnd -= 1
    else:
        bFl = False 
        i += 1
    print(i," ", bFl," ", sStr)
            
print(sStr)
