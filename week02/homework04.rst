===================
Домшанее задание 04
===================

Материалы занятия: https://github.com/maxchv/LearnPython/tree/master/week02

Домашнее задание: https://github.com/maxchv/LearnPython/blob/master/week02/homework04.rst

Видео: 

Задание 1
---------

Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, 
которая выводит все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" 
(без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

Пример экрана вывода:

>>> 5 8 2 7 8 8 2 4
>>> 8
1 4 5

>>> 5 8 2 7 8 8 2 4
>>> 10
Отсутствует


Задание 2
---------

write the program that prompts the user for a list of numbers and prints out the maximum and minimum 
of the numbers at the end when the user enters "done". 

Write the program to store the numbers the user enters in a list and use the max() and min() 
functions to compute the maximum and minimum numbers after the loop completes.

>>> Enter a number: 6
>>> Enter a number: 2
>>> Enter a number: 9
>>> Enter a number: 3
>>> Enter a number: 5
>>> Enter a number: done
>>> Maximum: 9.0
>>> Minimum: 2.0

Задание 3
---------

"""But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief"""

For each line, split the line into a list of words using the split function.

For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical order.

['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

Задание 4
---------

https://ru.wikipedia.org/wiki/Палиндром

Задание X
---------

Выведите таблицу размером N x N, заполненную числами от 1 до N**2 по спирали, 
выходящей из левого верхнего угла и закрученной по часовой стрелке, 
как показано в примере (здесь n=5):

Пример экрана вывода:

>>> 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9