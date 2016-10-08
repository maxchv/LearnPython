import math

class Circle:
    """
    Задание 1

    Реализуйте конструктор с одним параметром - диаметром окружности

    Добавте свойства radius и diameter и area (только геттеры)
    Свойство area возвращает площать окуржности

    Перегрузите следующие операторы класса Circle (окружность)
        ==
        >
        <
        >=
        <=
        __str__
        __repr__
        += и -= - пропорциональное изменение размеров окружности, путем изменения ее радиуса
        (методы __iadd__ и __isub__)

    >>> c = Circle(2)
    >>> c.radius
    1.0
    >>> c.diameter
    2
    >>> c.area
    3.141592653589793
    >>> c.radius = 5
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> c.area = 5
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> c.diameter = 5
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> c1 = Circle(1)
    >>> c3 = Circle(3)
    >>> c > c1
    True
    >>> c >= c1
    True
    >>> c >= c
    True
    >>> c == c1
    False
    >>> c == c
    True
    >>> c < c3
    True
    >>> c <= c3
    True
    >>> c <= c
    True
    >>> c != c3
    True
    >>> c != c
    False
    >>> c += 1
    >>> c.radius
    2.0
    >>> c += 3
    >>> c.radius
    5.0
    >>> c.diameter
    10
    >>> c.area
    78.53981633974483
    >>> c -= 1
    >>> c.radius
    4.0
    >>> c.area
    50.26548245743669
    """
    def __init__(self, d):
        self.__diameter = d

    @property
    def diameter(self):
        return self.__diameter

    @property
    def radius(self):
        return self.diameter/2

    @property
    def area(self):
        return self.radius * self.radius * math.pi

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __iadd__(self, other):
        self.__diameter += 2*other
        return self

    def __isub__(self, other):
        self.__diameter -= 2*other
        return self

    def __str__(self):
        return "circle r = {}".format(self.radius)

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    import doctest
    doctest.testmod()