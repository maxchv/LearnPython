## [def]

def add(a, b):
    return a + b

print("10 + 20 =",add(10, 20))

## [lambda]

add = lambda a, b: a + b
print("10 + 20 =", add(10, 20))

## [default arguments]

# В lambda-выражениях можно использовать аргументы со значениями по умолчанию:
add = lambda a=1, b=2, c=3: a + b + c
print(add())
print(add(c = 5))
print(add(b = 5, c = -1))

## [sorting down]

# сортировка выбором - по убыванию
def sorting(lst):
    count = len(lst)
    for i in range(count):
        idx = i
        for j in range(i+1, count):
            if lst[j] < lst[idx]:
                idx = j
        if idx != i:
            lst[i], lst[idx] = lst[idx], lst[i]
lst = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(lst)
sorting(lst)
print(lst)

## [sorting up]

# сортировка выбором - по возрастанию
def sorting(lst):
    count = len(lst)
    for i in range(count):
        idx = i
        for j in range(i+1, count):
            if lst[j] > lst[idx]:
                idx = j
        if idx != i:
            lst[i], lst[idx] = lst[idx], lst[i]
lst = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(lst)
sorting(lst)
print(lst)

## [sorting using compare function]
# сортировка выбором - универсальный подход
def sorting(lst, cmp):
    """
    Сортиовка выбором

       lst - перечисление
       cmp - функция сравнения
    """
    count = len(lst)
    for i in range(count):
        idx = i
        for j in range(i+1, count):
            if cmp(lst[j], lst[idx]):
                idx = j
        if idx != i:
            lst[i], lst[idx] = lst[idx], lst[i]

def up(a, b):
    return a > b

def down(a, b):
    return a < b

lst = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(lst)
sorting(lst, down)
print(lst)
sorting(lst, up)
print(lst)

## [sorting using lambda]
# сортировка выбором - универсальный подход
def sorting(lst, cmp = lambda x, y: x < y):
    """
    Сортиовка выбором

       lst - перечисление
       cmp - функция сравнения
    """
    count = len(lst)
    for i in range(count):
        idx = i
        for j in range(i+1, count):
            if cmp(lst[j], lst[idx]):
                idx = j
        if idx != i:
            lst[i], lst[idx] = lst[idx], lst[i]
lst = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(lst)
sorting(lst)
print(lst)
sorting(lst, lambda x, y: x > y)
print(lst)

## [filter] 
# Позволяет фильтровать значения последовательности.
# В результирующем списке остаются только те значения,
# для которых значение функциии для элемента истинно.

l1 = list(range(-5, 5)) 
print(l1)     

l2 = filter((lambda x: x > 0), range(-5, 5)) 
print(list(l2))

# альтернативное решение - через генератор списка
l3 = [x for x in l1 if x > 0]
print(l3)

## [map]
# Отображение функций на последовательности: map
# Позволяет обрабатывать одну или несколько
# последовательностей с помощью заданной функции

l1 = [1, 2, 3, 4]
def changeList(lst, f):
    result = []
    for x in lst:
        result.append(f(x)) # изменить каждый элемент
    return result
# увеличить каждый член последовательности на 10
print(changeList(l1, lambda x: x + 10))

# через встроенную фунцию map будет короче
print(list(map((lambda x: x + 10), l1))) 

# несколько последовательностей
a = pow(3, 4) # 3 ** 4
print(a) 

b = map(pow, [1, 2, 3], [2, 3, 4]) 
print(list(b)) 

## [reduce]
# Используется для организации цепочечных вычислений

from functools import reduce 

l1 = [1, 2, 3, 4]

# найти сумму всех элементов списка
s = reduce(lambda x, y: x + y, l) # Эквивалентно ((((1+2)+3)+4)
print(s) # 10


# найти произведение всех элементов списка
p = reduce((lambda x, y: x * y), l) # Эквивалентно ((((1*2)*3)*4)

print(p) # 24

## [zip code]

def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
        
## [zip]

a = [1,2,3,4,5]
b = ['a','b','c']
print(list(zip(a, b))) # [(1, 'a'), (2, 'b'), (3, 'c')]

## [nasted functions]
# обойти все элементы списка
def walk_lists(l):
    def read_list(lst):
        for i in lst:
            if type(i) == list:
                read_list(i)
            else:
                print(i, end=" ")
    read_list(l)
    print()
walk_lists([1, 2, 3, 4])
walk_lists([1, [2, 3], 4])

## [nasted function simple]

def foo():    
    def max(*args):
        print("fake max function")
    #print(locals())
    max()
#print(globals())
foo()

print("max([1,2,3])", max([1,2,3]))

## [nasted function sum]

def summ(current):
    def add(increment):
        current += increment
        return current
    return add
s = summ(0)
print(s(10))
print(s(10))
print(s(10))

## [closure]

def summ(n):
    def add(x):
        return x + n
    return add

f = summ(10)
print(f(5))
print(f(15))
print(f(25))

## [modules]
# импорт стандартного модуля
import os

print(os.getcwd())

import math as m

print(m.sqrt(4))

from math import sqrt

print(sqrt(4))

from math import cos, sin
print(cos(3.14))

from math import *

print(pow(5,3))


## [own module]

def hello():
    print('Hello, world!')

def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

## [using module]

import mymodule

mymodule.hello()
print(mymodule.fib(10))
