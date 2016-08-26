# Предприниматель ведет учет доходов от своей
# деятельности каждый месяц. Январь - 12345,
# Февраль - 14532, Март- 17523, Апрель - 23421, Май - 21345, Июнь - 32124, Июль - 36214, Август - 34214, Сентябрь - 31245, Октябрь - 30123, Ноябрь - 29313, Декабрь - 20235
# 
# Найти общий доход предпринимателя з год деятельности и средний доход в месяц.
# 
# Дополнительно: найти месяцы, в котором доход был наибольшим и наименьшим.
money = [12345, 14532, 17523, 23421, 21345, 32124,
         36214, 34214, 31245, 30123, 29313, 20235]
#money.append(23455)
s = 0
maxValue = 0
minValue = 0

for m in money:    
    s += m          # накопление суммы
    if m > maxValue:
        maxValue = m
    if m < minValue:
        minValue = m

maxIdx = 0
minIdx = 0
for i in range(len(money)):
    if money[i] == maxValue:
        maxIdx = i

    if money[i] == minValue:
        minIdx = i
print("Max idx:", maxIdx)
print("Min idx:", minIdx)
print("Oбщий доход предпринимателя з год", s)
print("Месяцов", len(money))
print("Cредний доход в месяц", s / len(money))

## [short solution]
money = [12345, 14532, 17523, 23421, 21345, 32124,
         36214, 34214, 31245, 30123, 29313, 20235]
s = sum(money)
print("Oбщий доход предпринимателя з год", s)
print("Cредний доход в месяц", s / len(money))
minIdx = money.index(max(money))
maxIdx = money.index(min(money))
print("Максимальный номер месяца:", maxIdx + 1)
print("Минимальный месяц:", minIdx + 1)

## [input to list]
money = []
#money = list()
print(money)
for i in range(12):
    m = float(input("Введите доход для " + str(i+1) + " месяца: "))
    money.append(m)
    print("money", money)

## [sublists]

t = [9, 41, 12, 3, 74, 15]
s = t[1:3]
s = []
for i in range(1, 3):
    s.append(t[i])
print("result", s)


    
