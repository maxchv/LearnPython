import re

def get_column(m, j):
    """
    Вспомогательный метод, который возвращает строку,
    составленную из j-го символа списка строк m

    :param m: список строк
    :param j: номер извлекаемого символа
    :return:  строку
    """
    return "".join([m[i][j] for i in range(len(m))])

# Задание 0. Пройти курс Знакомство с HTML на сайте https://htmlacademy.ru/continue/category/welcome

def puzzle_1():
	"""
	Задание 1.

    Решить кроссворд 1
    https://regexcrossword.com/challenges/beginner/puzzles/1

    Как решать: https://regexcrossword.com/howtoplay

    Результат кроссворда представить в виде кортежа из двух строк.
    Функция puzzle_1 должна возвращать этот кортеж.

    Для примера https://regexcrossword.com/howtoplay результат
    должен быть: ('AA', 'BC')


    >>> re.match(r'HE|LL|O+', puzzle_1()[0]) != None
    True
    >>> re.match(r'[PLEASE]+', puzzle_1()[1]) != None
    True
    >>> re.match(r'[^SPEAK]+', get_column(puzzle_1(), 0)) != None
    True
    >>> re.match(r'EP|IP|EF', get_column(puzzle_1(), 1)) != None
    True
	"""
	return ("??",
            "??")

def puzzle_2():
	"""
	Задание 2.

    Решить кроссворд 3
    https://regexcrossword.com/challenges/beginner/puzzles/3

    Результат кроссворда представить в виде кортежа из двух строк.
    Функция puzzle_2 должна возвращать этот кортеж.

    >>> re.search(r'(.)+\\1', puzzle_2()[0]) != None
    True
    >>> re.match(r'[^ABRC]+', puzzle_2()[1]) != None
    True
    >>> re.match(r'[COBRA]+', get_column(puzzle_2(), 0)) != None
    True
    >>> re.match(r'(AB|O|OR)+', get_column(puzzle_2(), 1)) != None
    True
	"""
	return ("??",
            "??")

def puzzle_3():
	"""
	Задание 3.

    Решить кроссворд 5
    https://regexcrossword.com/challenges/beginner/puzzles/5

    Результат кроссворда представить в виде кортежа из двух строк.
    Функция puzzle_3 должна возвращать этот кортеж.

    >>> re.search(r'18|19|20', puzzle_3()[0]) != None
    True
    >>> re.match(r'[6789]\d', puzzle_3()[1]) != None
    True
    >>> re.match(r'\d[2480]', get_column(puzzle_3(), 0)) != None
    True
    >>> re.match(r'56|94|73', get_column(puzzle_3(), 1)) != None
    True
	"""
	return ("??",
            "??")

def parse_itstep():
    """
    Задание X.

    Распарсить новости на сайте http://itstep.dp.ua/category/news/
    Вернуть список кортежей - url и заголовок новости

    :return:
    """
    pass

if __name__ == "__main__":
    import doctest

    doctest.testmod()


