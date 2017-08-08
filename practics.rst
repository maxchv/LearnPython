=======================
Практическое задание 01
=======================


Задание 0
---------

Для каждого из следующих выражений, укажите возвращаемое значение. Код выполняется последовательно.

>>> 6 + 8 - 3

>>> 5 * 2.0

>>> 3 ** 2

>>> 1 + 2 ** 3

>>> (1 + 2) ** 3

>>> 12 / 5

>>> 12 / 5.0

>>> 12 // 5.0

>>> 12 // 5

>>> 14 % 5

>>> 14.0 % 5

>>> a = 3
>>> a + 2.0

>>> a = a + 0.1
>>> a

>>> a += 1; a

>>> a -= .1
>>> round(a)

>>> b = 64.00 ** (1 / 2); b

>>> c = 64.0 ** (1 / 2.00); c

Задание 1
---------

Первоначальные данные:

>>> str1 = 'hello'
>>> str2 = ','
>>> str3 = 'world'

Для каждого из следующих выше выражений укажите возвращаемое значение. Строчные данные просьба вводить в одинарных кавычках. 
Возвращаемое значение указывать для последней команды консоли.

>>>	str3

>>>	str3[0]

>>> str3[1]

>>> str3[-1]

>>> str1 + str2 + str3

>>> str3 * 3

>>> str4 = str1 + str2 + ' ' + str3; str4

>>> str4[1:9]

>>> str4[:-1]

>>> 'heLLo WORlD'.title()

>>> 'heLLo WORlD'.capitalize()

>>> 'heLLo WORlD'.count('l')

>>> 'heLLo WORlD'.index('L')

>>> 'heLLo WORlD'.isalpha()

>>> str4 = 'PyBursa'; str4[0] = 'p'; str4

>>> str4[::-1]



Задание 2
---------

Исходные данные:

>>> x = [1, 2, [3, 'John', 4], 'Hi']
>>> listA = [1, 4, 3, 0]
>>> listB = ['x', 'z', 't', 'q']

Для каждого из следующих выражений, укажите возвращаемое значение.

>>> x[0]

>>> x[2]

>>> x[-1]

>>> x[2][2]

>>> x[0] = 8
>>> x

>>> listA.sort()
>>> listA

>>> listA.insert(0, 100)
>>> listA

>>> listA.remove(3)
>>> listA

>>> listA.append(7)
>>> listA

>>> listA + listB

>>> listB.sort()
>>> listB.pop()

>>> listB

>>> listB.reverse()
>>> listB

>>> listL = [0, 1, 2, None, {}, [], ]
>>> len(listL)

>>> tupleA = (1, 4, 3, 0)
>>> tupleB = ('p', 'y', 't', 'h', 'o', 'n')
>>> tupleA[::-1]
>>> tupleA

>>> tupleC = tupleA[:-2:-2] + tupleB[2::-1]
>>> tupleC


Задание 3
---------

Первоначальные данные

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

Для каждого из следующих выражений, укажите возвращаемое значение. Если возникает ошибка, введите слово ошибка.

>>> animals['d'] = 'donkey'
>>> animals
{'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}
>>> animals['c']
'coati'
>>> animals['a'] = 'anteater'
>>> animals['a']
'anteater'
>>> animals.has_key('b')
ошибка
>>>'baboon' in animals
False
>>> 'b' in animals
True
>>> sorted(list(animals.keys()))
['a', 'b', 'c', 'd']
>>> del animals['b']
>>> 'b' in animals
False
>>> sorted(list(animals.values()))
['anteater', 'coati', 'donkey']
>>>sorted(list(animals.items()))
[('a', 'anteater'), ('c', 'coati'), ('d', 'donkey')]
>>> print(animals.get('b'))
None

Какие варианты кода вернут значение по ключу 'version' из словаря dictD = {'version': '2.7.10', 'language': 'python'} : 

a)* dictD['version']
b) dictD[0]
c)* dictD.pop('version')
d) dictD.popitem()
e) list(dictD.values())[0]
f)* dictD.get('version')

Какое значение будет записано по ключу "a" в словарь: d = {'a': 5, 'b': 3, 'a': 7} ?

a) 5
b) сгенерируется SyntaxError
c)* 7



Задание 4 
---------

Для каждого из следующих выражений, укажите возвращаемое значение. Если возникает ошибка, введите слово ошибка.

>>> bool(0.1)
True
>>> bool(0.0)
False
>>> bool([0])
True
>>> bool('0')
True
>>> 4 > 4
False
>>> '4' > 4
ошибка
>>> 1 < 2 and 7 > 8
False
>>> 4 > 5 or 3 < 4 and 9 < 8
False
>>> not(4 > 3 and 100 > 6)
False
>>> 'ab' > 'ba'
False
>>> 'abd' > 'abc'
True
>>> 'ab' > 'abc'
False
>>> 'first' and 'second'
'second'
>>> 'first' or 'second'
'first'
>>> 'first' or ''
'first'
>>> 'first' and ''
''
>>> '' or 'str' and 1
1
>>> 'a' and 'b'
'a'
>>> 'a' or 'b'
'b'



Задание 5
---------

Для каждого из следующих условий, укажите возвращаемое значение, если возвращаемого значения не будет введите слово ничего.

>>> if 6 > 7:
>>>    print('Да')


>>> if 6 > 7:
>>>     print('Да')
>>> else:
>>>     print ('Нет')


>>> temp = 38
>>> if temp > 25:
>>>    print( 'Hot')
>>> elif temp > 35:
>>>   print('REALLY HOT!')
>>> elif temp > 20:
>>>    print('Comfortable')
>>> else:
>>>    print('Cold')


>>> num = 5
>>> if num > 2:
>>>    num -= 1
>>> print(num)



>>> var = None
>>> if not var:
>>>     var = 'something'
>>> print(var)


>>> a = 3
>>> b = ord('\x03')
>>> c = a == b
>>> if c:
>>>     print(c)


>>> number = 10
>>> if number.isdigit():
>>>     if type(number) == int:
>>>         print(True)
>>>     else:
>>>         print(False)
      
	  
>>> a = 'python'
>>> b = 'django'
>>> if a > b:
>>>     pass
>>> elif a == b:
>>>     print('equal')   
>>> else:
>>>     print('not equal') 


>>> a = 'Только в уме!'
>>> if a == 'Код тестов просто запускал в консоли':
>>>     k = 'not good'
>>> elif a == 'Сначала прикидывал в уме, потом проверял в консоли':
>>>     k = 'good'  
>>> elif a == 'Только в уме!':
>>>     k = 'very good'        
>>> print('Реальный результат: %s' % k)


Какие пояснения следующего кода правильны:

>>> a = 'julie'
>>> b = 'JULIE'
>>> c = 'Julie'
>>> 
>>> if a == c or b:
>>>     print(True)
>>> else:
>>>     print(False) 

a) проверка a == c не будет выдержана (сама по себе вернет False), т.к. при сравнении строк учитывается регистр: заглавные буквы имеют код ASCII таблицы, отличный от кода строчных букв; 
b) в результате исполнения кода получим False, потому что a не равно c и a не равно b, ведь учитывается регистр; 
c) в любом случае (при любом регистре значимых значений a, b и c) в результате выполнения кода получим True; 
d) только при преобразовании c.lower() или b.lower() до запуска оператора if в результате получили бы True. 


Задание 6
---------

Для каждого из следующих выражений укажите возвращаемое значение.

>>> numbers = []
>>> for num in [1, 5, 2, 8, 11, 14]:
>>>     if num % 2 == 0:
>>>         numbers.append(num)
>>> print(numbers)


>>> squares = []
>>> for x in [1, 8, 2, 23]:
>>>     for y in [6, 1, 5, 1, 2]:
>>>         if x == y:
>>>            squares.append(x*y)
>>> print(squares)


>>> L1 = ['a', 'an', 'ba', 'ac', 'ca']
>>> L2 = ['ab', 'na', 'an', 'ac']
>>> L3 = []
>>> for x in L1:
>>>     if x  in L2:
>>>         L3.append(x)
>>> print(L3)


>>> total = 0
>>> x = 10
>>> for i in range(100):
>>>     total += 1
>>> 
>>> while x > 0:
>>>     x -= 1
>>>    total += 1
>>> 
>>> print(total)


>>> s = 'iterate'       
>>> for i, k in enumerate(s, 1):
>>>     if not i % 2:
>>>         print(k, end=' ')


Разработчику поставлена задача найти первый элемент максимальной длины списка box, содержащего только строковые элементы. 
Искомый элемент необходимо записать в переменную longest. Разработчик при написании кода допустил ошибку: какого оператора 
недостает во втором цикле for кода? (все переменные определены) 

>>> for i in box:
>>>     if len(i) > maximum:
>>>         maximum = len(i)
>>>        
>>> for i in box:
>>>     if len(i) == maximum:
>>>         longest = i

Какие инструкции условия и инструкции цикла реализованы в Python?

a) while 
b) do... while 
c) if 
d) switch 
e) for 
