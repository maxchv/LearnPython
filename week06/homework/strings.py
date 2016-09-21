"""
Домашнее задание 12

Тема: модули, сторки
"""

def upperFirst(string, length):
    """
    Задание 1
    ---------
    Реализовать функцию upperFirst, которая принимает два аргумента - строковый
    и числовой.

    Функция возвращает строку string, первые length символов которой приведены
    к верхнему регистру, остальная часть строки - в нижнем регистре.

    >>> upperFirst('hello world', 7)
    'HELLO World'
    >>> upperFirst('abcd', 4)
    'ABCD'
    >>> upperFirst('abcd', 0)
    'abcd'
    """
    pass

def reverse_all(text):
    """
    Задание 2
    ---------
    Реализовать функцию, которая принимает в качестве аргумента строку текста
    и изменяет в тексте порядок следования букв в словах
    Вернуть модифицированный текст.

    >>> reverse_all('abc')
    'cba'
    >>> reverse_all('abc def')
    'cba fed'
    """
    pass

def module():
    """
    Задание 3
    ---------
    В директории с текущим файлом создать модуль с mymodule.py

    В модуле реализовать функцию вычисления факториала числа n factorial(n)

    >>> import mymodule
    >>> mymodule.factorial(5)
    120
    >>> mymodule.factorial(4)
    24
    >>> mymodule.factorial(20)
    2432902008176640000
    """
    pass

def count_a(text):
    """
    Задание X
    -----------
    Посчитать в тексте количество букв "a" при условии что она окружена согласными
    ("car") и она не является первой или последней буквой слова.

    >>> count_a('Cras ultricies ligula sed magna dictum porta.')
    7
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
