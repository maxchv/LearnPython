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

Функции и модули
================

Задание 7
---------

Определены функции

def a(x):
    return x + 1

def b(x):
    return x + 1.0
  
def c(x, y):
    return x + y
  
def d(x, y):
    return x > y
  
def e(x, y, z):
    return x >= y and x <= z
    
def f(x, y):
  x + y - 2
  
Для каждой вызванной функции укажите возвращаемое значение и тип. 
Если нет возвращаемого значения , указываем None
  
>>> a(1)
  
>>> a(-3.5)
  
>>> a(a(a(6)))
  
>>> c(a(1), b(1))
  
>>> c('monty', 'python')
  
>>> d('monty', 'python')
  
>>> e(a(3), b(2), c(1, 3))
  
>>> f(4, 8)
  
  
Задание 8
---------

Определена функция:

def show_full_name(name, surname, patronymic = None):
    return 'Fullname: {} {} {}'.format(name, patronymic, surname)


Для каждого фрагмента кода укажите возвращаемое значение:

1. 	record = {'name': 'anna', 'patronymic': 'petrovna', 'surname': 'polosatova'}	
	show_full_name(**record, 'ivanovna')
	
	a) 'Fullname: anna ivanovna polosatova' 
	b) 'Fullname: anna petrovna polosatova' 
	c) SyntaxError 
	d) 'Fullname: anna petrovna ivanovna polosatova' 
	e) 'Fullname: anna ivanovna petrovna polosatova' 
	
2. 	record = {'name': 'anna', 'patronymic': 'petrovna', 'surname': 'polosatova'}
	show_full_name('ivanovna', **record)
	
	a) 'Fullname: anna ivanovna polosatova' 
	b) 'Fullname: anna petrovna polosatova' 
	c) TypeError 
	d) 'Fullname: anna petrovna ivanovna polosatova' 
	e) 'Fullname: anna ivanovna petrovna polosatova' 

3. 	record = {'surname': 'ivanko', 'name': 'kolya', 'age': 15}        
	show_full_name(**record)

	a) TypeError 
	b) 'Fullname: kolya ivanko' 
	c) 'Fullname: kolya None ivanko' 
	
4. 	record1 = {'surname': 'ivanko', 'name': 'kolya'}  
	record2 = ['petrovich']        
	show_full_name(**record1, *record2)
	
	a) SyntaxError 
	b) 'Fullname: kolya ivanko' 
	c) 'Fullname: kolya None ivanko' 
	d) 'Fullname: kolya petrovich ivanko' 
	
5. 	record = {'surname': 'ivanko', 'name': 'kolya'} 
	show_full_name(**record)
	
	a) TypeError 
	b) 'Fullname: kolya ivanko' 
	c) 'Fullname: kolya None ivanko' 
	d) 'Fullname: kolya petrovich ivanko' 
	

Задание 9
---------

Определены функции

def a(x, y, z):
    if x:
        return y
    else:
        return z

def b(q, r):
    return a(q>r, q, r)


Для каждой вызванной функции укажите возвращаемое значение и тип.

>>> a(False, 2, 3)

>>> b(3, 2)

>>> a(3>2, 'a', 'b')

>>> b('a', 'b')

Задание 10
----------

Для каждого фрагмента кода укажите возвращаемое значение и тип данных. Если генерируется ошибка - в выпадающем списке выберите "ошибка", в поле для ввода введите текст "ошибка" (без кавычек)

a = 10
            
def f(x):
    return x + a
            
a = 3
            
>>> f(1)

x = 12
        
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
        
>>> g(x)

def foo(x):
    def bar(x):
        return x + 1.0
    return bar(x * 2)
        
>>> foo(3)

def foo (x):
    def bar (z):
        return z + x
    return bar(3)

>>> foo(2)

def foo (numbers_list = []):
    if numbers_list:
        numbers_list.append(1)
    else:
        numbers_list.append(2)
    return numbers_list

foo()
>>> foo() # Примечание: в ответе указывать результат второго вызова функции

numbers_list = [3, 6, 1, 8]
        
def foo (ls):
    return ls.sort()

>>> foo(numbers_list)


Задание 11
----------

Какое значение вернет вызов следующей функции:

def outer_function(a):
    a += 1
    def inner_function(b):
        a += b
        return a
    return inner_function(1)  
    
outer_function(1)

	a) 1
	b) 2
	c) 3
	d) UnboundLocalError 
	
Задание 12
----------

Какое значениие вернет вызов следующей функции:

a = 1

def foo(b):
    global a
    a += b
    return a
    
foo(1)

	a) 1
	b) 2
	c) UnboundLocalError 
	
Задание 13
----------

Выполнение какого выражения возвращает список четных чисел последовательности чисел от 1 до 20?

	a) [x for x in range(1, 21) if x % 2]
	b) [x for x in range(1, 21) if not x % 3]
	c) [x for x in range(1, 21) if not x % 2]
	d) [x for x in range(1, 20) if not x % 2]
	e) (x for x in range(1, 20) if not x % 2)
	
Задание 14
----------

Какие варианты кода возвращают список целых чисел, взятых по квадратному корню элементов из исходного списка?

Объявленные функции и переменные:

from math import pow

def get_numbers(x):
    lst = []
    for i in x:
        lst.append(int(pow(i, 1/2.0)))
    return lst
    
my_list = [81, 9, 64]

	a) list(map(lambda x: int(pow(x, 1/2.0)), my_list))
	b) list(map(get_numbers, my_list))
	c) get_numbers(my_list)
	
Задание 15
----------

Какие выражения возвращают список целых чисел, кратных 3, из исходного списка my_list = [81, 9, 64]?

	a) list(filter(lambda x: not x % 3, my_list))
	b) list(map(lambda x: not x % 3, my_list))
	c) [i for i in my_list if not i % 3]
	


Библиотеки и пакетный менеджер
==============================

Задание 16
----------

Какие необходимо предпринять действия, чтобы стали доступны для импорта стандартные модули питона (stdlib)?
	
	a) Установить python-stdlibs (apt-get install python-stdlib) 
	b) Добавить специальный путь в sys.path (sys.path.append(“/usr/bin/python/stdlib”)) 
	c) Ничего не нужно делать, стандартные модули доступны сразу после установки python 
	d) Выполнить from __future__ import stdlib 
	
Интерфейс к какой базе данных содержиться в stdlib?

	a) MySQL 
	b) sqlite3 
	c) MSSQL 
	d) Oracle 
	
Какой модуль из stdlib используется для работы с датой и временем?

	a) alldata 
	b) date 
	c) datetime 
	d) timedelta 
	
Какой модуль из stdlib появился в Python 3 и отсутствует в этом виде в Python 2?

	a) urllib
	b) urllib2 
	c) httplib 
	d) urllib.request 
	
Какой модуль из stdlib используется для работы с регулярными выражениями?

	a) regexp 
	b) re 
	c) random
	d) math 
	
Какой тип данных (объект) не находится во встроенных функциях __builtins__ и его необходимо импортировать перед использованием?

	a) set 
	b) array 
	c) tuple 
	d) unicode 
	
В каких директориях происходит поиск модулей для импорта?
	
	a) в директориях, которые содержатся в списке os.path модуля os 
	b) в директории, откуда был запущен интерпретатор python (т.е. в текущей директории) 
	c) в директориях, которые содержатся в списке sys.path модуля sys 
	d) во всех директориях файловой системы
	
Какая из перечисленных сторонних библиотек не является фреймвоком для web-разработки?

	a) flask
	b) django 
	c) tornado 
	d) pillow 
	
При помощи какого атрибута можно узнать физическое местонахождение модуля?
	
	a) __file__ 
	b) __doc__ 
	c) __name__
	d) __dict__ 
	e) __path__ 
	
Что делает следующий код: sys.path.append('/root/modules')?

	a) изменяет текущую рабочую директорию 
	b) добавляет директорию для поиска импортируемых модулей 
	c) перемещает директорию modules 
	d) создает новую директорию. 
 
Задание 17
----------

Как называется каталог питоновских пакетов?
	
	a) pip
	b) pypi
	c) pipi
	d) pypug
	
Какой файл внутри питоновского пакета используется для инсталляции пакета в систему?

	a) setup.py 
	b) install.py 
	c) pip
	d) pypy 
	
Откуда можно скачать питоновкий пакет?

	a) только из каталога пакетов https://pypi.python.org/pypi 
	b) только из каталога пакетов https://pypi.python.org/pypi и http://github.com
	c) только из каталога пакетов https://pypi.python.org/pypi, http://github.com и официального сайта python https://www.python.org/ 
	d) из любого локального и глобального источника: кто угодно может создать python пакет и выложить на любом сайте 
	
Что считается питоновским пакетом?

	a) Любая директория с файлами с расширением *.py 
	b) Любой питоновский модуль, который содержит файл __init__.py 
	c) Любая директория с файлом setup.py 
	d) Любая директория с файлом install.py 
	e) Только директории, которые созданы согласно документации Python Packaging User Guide (PyPUG): https://packaging.python.org/en/latest/ 
	
Что можно сделать при помощи пакетного менеджера PIP?
	
	a) Скачать и установить пакет 
	b) Удалить пакет 
	c) Установить пакет определенной версии 
	d) Все вышеперечисленное 
	
Что есть правильным указанием версии пакета, для PIP (несколько вариантов ответа)

	a) django=1.7.5 
	b) django>1.7 
	c) django 1.7.5 
	d) django==1.7.5 
	e) django version 1.7.5 
	
Для чего используются виртуальные окружения?

	a) Для изоляции устанавливаемых версий пакетов согласно зависимостей конкретного проекта.
	b) Для запуска Linux 
	c) Для подключения модулей не входящих в stdlibs 
	d) Для запуска питона в безопасном режиме 
	
Что необходимо учитывать при установке зависимостей согласно файлу регистрации зависимостей requirements.txt? 
Выберите наиболее полный правильный ответ из представленных.
 
	a) файл должен содержать перечень модулей обязательно с указанием их версий 
	b) файл должен содержать перечень модулей, желательно с указанием версий 
	c) файл должен содержать перечень модулей, желательно с указанием версий, директория файла должна быть текущей директорией 
	d) файл должен содержать перечень модулей, желательно с указанием версий, команда установки должна учитывать путь к файлу

Что нужно сделать, чтобы работала следующая строка кода: foo.bar.foobar() (при условии, что необходимый импорт осуществлен)? 
Выберите наиболее полный правильный ответ.

	a) создать файлы __init__.py и bar.py в директории foo, объявить функцию foobar() в bar.py 
	b) создать файлы __init__.py и и foo.py в директории bar, объявить функцию foobar() в foo.py 
	c) создать файл bar.py в директории foo, объявить в нем функцию foobar() 
	d) создать пакет bar в директории foo 
	

 