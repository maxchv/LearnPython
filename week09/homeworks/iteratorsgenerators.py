"""
Homework 18

Subject: Static methods, Class methods, Iterators
"""


class MathCls:
    """
    Задание 1

    Реализуйте статическием методы класса MathCls:
        add - возвращает сумму двух целых чисел
        sub - возвращает разность двух целых чисел
        mult - возвращает произведение двух целых чисел
        div - возвращает отношение двух читсел

    >>> MathCls.add(2, 3)
    5
    >>> MathCls.sub(5, 2)
    3
    >>> MathCls.mult(5, 2)
    10
    >>> MathCls.div(10, 2)
    5.0
    """
    pass


class SquareIterator:
    """
    Задание 2

    Реализовать итератор SquareIterator, который возвращает
    квадраты чисел от 1 до 10.

    Перегрузите методы __next__ и __iter__

    >>> it = SquareIterator()
    >>> for i in range(10):  next(it)
    1
    4
    9
    16
    25
    36
    49
    64
    81
    100
    >>> next(it)
    Traceback (most recent call last):
    ...
    StopIteration
    """
    pass


class Range:
    """
    Задание 3

    Реализовать итератор Range - аналог встроенной функции range

    Перегрузите методы __next__ и __iter__

    >>> it = Range(10)
    >>> for i in range(10):  next(it)
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>> next(it)
    Traceback (most recent call last):
    ...
    StopIteration
    >>> it = Range(2, 5)
    >>> next(it)
    2
    >>> next(it)
    3
    >>> next(it)
    4
    >>> next(it)
    Traceback (most recent call last):
    ...
    StopIteration
    >>> it = Range(2, 5, 2)
    >>> next(it)
    2
    >>> next(it)
    4
    >>> next(it)
    Traceback (most recent call last):
    ...
    StopIteration
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)