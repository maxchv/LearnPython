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
    Задание 2

    Реализовать итератор SquareIterator, который возвращает
    квадраты чисел от 1 до 10.

    Перегрузите методы __next__ и __iter__

    >>> it = Range()
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
    """
    pass

class Vehicle:
    """

    """
    highestVIN = 0
    def __init__(self, owner):
        self.__current_speed = 0
        self.__current_direction = 0
        self.__owner = owner
        self.highestVIN += 1
        self.__VIN = self.highestVIN

    @property
    def current_direction(self):
        return self.__current_direction

    @property
    def owner(self):
        return self.__owner

    @property
    def current_speed(self):
        return self.__current_speed


# Write a simple Vehicle class that has fields for (at least)
# current speed, current direction in degrees, and owner name.
# class Vehicle {
#   int currentSpeed;
#   int currentDirection;
#   String owner;
# }
# Add a static field to your Vehicle class for the highest Vehicle
# Identification Number issued, and a non-static field that holds each
# vehicle's ID number.
# class Vehicle {
#   int currentSpeed;
#   int currentDirection;
#   String owner;
#   static int highestVIN;
#   int VIN;
# }
# Write a main method for your Vehicle class that creates a
# few vehicles and prints out their field values. Note that
# you can also write a separate tester program as well.
# class Vehicle {
#
#   int currentSpeed;
#   int currentDirection;
#   String owner;
#   static int highestVIN;
#   int VIN;
#
#   public static void main(String[] args) {
#
#     Vehicle a = new Vehicle();
#     a.VIN = highestVIN++;
#     a.owner = "Larry Bird";
#
#     Vehicle b = new Vehicle();
#     b.VIN = highestVIN++;
#     b.owner = "Mark Jackson";
#
#     System.out.println("VIN: " + a.VIN + " belongs to " + a.owner);
#
#     System.out.println("VIN: " + b.VIN + " belongs to " + b.owner);
#
#     // Note that both cars are stopped, and facing East.
#
#   }
# }

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)