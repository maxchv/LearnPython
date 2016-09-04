# -*- coding: utf-8 -*-

def square(num):
	"""
	Задание 1. Напишите функцию, которая возвращает
	квадрат числа num
	
	>>> square(1)
	1
	>>> square(2)
	4
	>>> square(0)
	0
	>>> square(-1)
	1
	>>> square(5)
	25
	"""
	return num * num

def cube(num):
	"""
	Задание 2. Напишите функцию, которая возвращает
	куб числа num
	
	>>> cube(1)
	1
	>>> cube(2)
	8
	>>> cube(0)
	0
	>>> cube(-1)
	-1
	>>> cube(5)
	125
	"""
	pass

def listOfSquare(lst):
	"""
	Задание 3. Напишите функцию, которая принимает
	список чисел и возвращает список квадратов этих чисел
	
	>>> listOfSquare([1])
	[1]
	>>> listOfSquare([1, 2])
	[1, 4]
	>>> listOfSquare([0, 5, 3])
	[0, 25, 3]
	>>> listOfSquare([-1, 1, 2])
	[1, 1, 4]
	>>> listOfSquare([5, 6, 7])
	[25, 36, 49]
	"""
	pass

<<<<<<< HEAD

def filterEvenNumbers(lst):
	"""
	Задание 4. Напишите функцию, список из чисел 
	и возвращает список четных чисел
=======
def filterEvenNumbers(lst):
	"""
	Задание 4. Напишите функцию, которая принимает
	список чисел и возвращает список из четных чисел
>>>>>>> origin/master
	
	>>> filterEvenNumbers([1])
	[]
	>>> filterEvenNumbers([1, 2])
	[2]
<<<<<<< HEAD
	>>> filterEvenNumbers([2, 6, 8])
	[2, 6, 8]
	>>> filterEvenNumbers([10, 11, 5])
	[10]
	"""
	pass

def fizzbuzz(num):
	"""
	Напишите программу для возврата строк Fizz, Buzz или FizzBuzz при следующих условиях.
	
	Если передается аргумент кратный 3, возвратить Fizz; если кратно 5, возвратить Buzz;
	и если кратно как 3 так и 5, возвратить FizzBuzz.
	
	>>> fizzbuzz(3)
	'Fizz'
	>>> fizzbuzz(9)
	'Fizz'
	>>> fizzbuzz(25)
	'Buzz'
	>>> fizzbuzz(15)
	'FizzBuzz'
	>>> fizzbuzz(1)
	None
	
	"""
	pass

=======
	>>> filterEvenNumbers([0, 5, 3])
	[0]
	>>> filterEvenNumbers([-1, 1, 2])
	[2]
	>>> filterEvenNumbers([5, 6, 7, 8, 10])
	[6, 8, 10]
	"""
	pass
>>>>>>> origin/master

def fizzbuzz(num):
	"""
	Напишите программу для печати Fizz, Buzz или FizzBuzz, если выполняется одно из условий.
	Если число кратно 3, печать Fizz; если кратно 5, печать Buzz;
	и если одновременно кратно 3 и 5 - печать FizzBuzz.
	
	>>> fizzbuzz(6)
	Fizz
	>>> fizzbuzz(10)
	Buzz
	>>> fizzbuzz(15)
	FizzBuzz
	>>> fizzbuzz()
	None
	"""
	pass
	
def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()
