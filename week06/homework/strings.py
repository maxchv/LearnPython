
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
    В директории с текущим файлом создать модуль с pyinfo.py

    В модуле реализовать функцию

    """
    pass

def count_a(text):
    """
    Задание XXX
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
