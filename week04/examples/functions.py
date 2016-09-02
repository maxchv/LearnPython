## [hw list]
line = input("Введите строку: ")
num = input("Искомое число: ")
lst = line.split()

start = 0
count = lst.count(num)
for i in range(count):
    start = lst.index(num, start)
    print(start, end=" ")
    start += 1
    
if count == 0:
    print("Отсутсвует")

## [print dict]
d = {'sun': 2, 'east': 1, 'moon': 1}
for key in d:
    print(key, ':', d[key])

#print(d['test'])
print(d.get('test', 0))

## [delete dict]
d = {1     : 1,
     2     : 1,
     3     : 2,
     'test': 1}
nd = {} # результат
for value in d.values(): # цикл по элементам словаря d
    for k in d:# цикл по ключам словаря d
        # добавление только уникальных __занчений__
        # из словаря d в словарь nd
        if d[k] == value and value not in nd.value():
            nd[k] = value

print(nd)
## [define function]

def greet():
    return "Hello"
answer = greet()
print(answer)
print(greet())

greet()

def add(a = 0, b = 0):
    """
    add(a, [b]) -> возвращает сумму двух
    числовых аргументов
    """
    print("a =", a)
    print("b =", b)
    c = a + b
    print("c =", c)
    return c

add(1, 2)
print("*"*10)
add(2, 1)
print("*"*10)
add(2)
print("*"*10)
add()
print("*"*10)
add(b = 1, a = 2)

## [return]

def void_fnct():
    pass # ничего не делать

def repeat(s, count = 10):
    if len(s) == 1:
        return None
    else:
        print("")
    print("Этот код выполнится")
    

print(void_fnct())
print(repeat("*"))

## [doctest]

def get_first_three_letter(line):
    """
    Функция возвращает строку из
    первых трех символов входной строки

    >>> get_first_three_letter("Monday")
    'Mon'
    >>> get_first_three_letter("Friday")
    'Fri'
    """
    return line[:3]

print(get_first_three_letter.__doc__)

import doctest      # пакет
doctest.testmod()   # вызов функции testmod() пакета doctest





