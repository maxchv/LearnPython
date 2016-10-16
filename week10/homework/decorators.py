"""
Homework 18

Subject: Generators, Decorators

Тестирование декораторов

>>> one = factorial(1)
>>> print(one)
1
>>> cached_results[1]
1
>>> len(cached_results)
1
>>> two = factorial(2)
>>> print(two)
2
>>> len(cached_results)
2
>>> 2 in cached_results
True
>>> cached_results[2]
2
>>> factorial(4)
24
>>> 4 in cached_results
True
>>> cached_results[4]
24
>>> login(username="admin")
login succeeded
True
>>> login(username="demo") is False
True
>>> login(username="user")
login succeeded
True
>>> login(username="qwerty") is False
True
"""

cached_results = {}


def cache(f):
    """
    Задание 1

    Реализуйте декоратор cache для кеширования резульатов вычисления
    факториала числа в словаре cached_results

    Назначение декоратора - сокращение времени повторного вычисления
    факториала

    Если факториал числа вычисляется впервые, то необходимо вызвать
    декорируемую функцию, вычислить факториал и сохранить результат в словаре
    cached_results (ключ - число, для которого вычисляется факториал,
    значение - факториал числа)

    Если факториал для числа уже вычислялся, то он находится в словаре
    cached_results и повторного обращения к функции не требуется - достаточно
    извлечь значение факториала по ключу из словаря

    """
    pass


@cache
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def login_required(f):
    """
    Задание 2

    Реализуйте декоратор login_required, который проверяет является ли
    имя пользователя, переданное декорируемой функции (login) в качестве аргумента
    (username) равным 'user' или 'admin'

    Если username равен 'user' или 'admin', то декорируемая функция выполняется
    и возвращается результат, иначе возвращается False

    """
    pass


@login_required
def login(username="guess"):
    print ("login succeeded")
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
