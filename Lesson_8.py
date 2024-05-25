# Задание № 1

# def StrAge(age):
   
#     if (age > 4) and (age < 21):
#        sStr =' лет.'
#     else:
#        i = age % 10
#        if i==1:
#           sStr =' год.'
#        elif i < 5:
#           sStr = ' года.'
#        else:
#           sStr = ' лет.'
#     return(sStr)
   
pets = dict()
lFl = True
while lFl:
    sName = str(input("Введите имя питомца (Enter - выход): "))
    if sName:
        pets[sName] = {}
        sStr = str(input("Введите вид питомца: "))
        pets[sName]["Вид_питомца"] = sStr
        nVoz = int(input("Введите возраст питомца: "))
        pets[sName]["Возраст_питомца"] = nVoz
        sChar = str(input("Введите имя владельца: "))
        pets[sName]["Имя_владельца"] = sChar
    else:
        lFl = False

# версия 1 с функцией
# for i in pets.keys():
#    dData = list(pets[i].values())
#    print("Это", dData[0].strip(), 'по кличке "', i.strip(), '". Возраст питомца:', dData[1], 
#          StrAge(dData[1]), "Имя владельца:", dData[2].strip() )

# версия 2 без функции
for i in pets.keys():
   sStr = ""
   dData = list(pets[i].values())
   if (dData[1] > 4) and (dData[1] < 21):
      sStr =' лет.'
   else:
      age = dData[1] % 10
      if age==1:
         sStr =' год.'
      elif age < 5:
         sStr = ' года.'
      else:
         sStr = ' лет.'

   print("Это", dData[0].strip(), 'по кличке "', i.strip(), '". Возраст питомца:', dData[1], 
         sStr+" Имя владельца:", dData[2].strip() )

# --------------------------------------------------------------------------------------------------------
# Задание № 2

nNum1, nNum2 = map(int, input("Начальное и конечное целые числа в строке: ").split())
nDic = dict()
if nNum1 < nNum2:  nStep = 1
else: nStep = -1
for i in range(nNum1, nNum2+nStep, nStep):
    nDic[i] = i**i
print(nDic)
