## [subcode]

class Cat:
    def __init__(self, name, color, age):
        self.__name = name
        self.__color = color
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def age(self):
        return self.__age

class Cow:
    def __init__(self, name, color, age):
        self.__name = name
        self.__color = color
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def age(self):
        return self.__age

class Dog:
    def __init__(self, name, color, age):
        self.__name = name
        self.__color = color
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def age(self):
        return self.__age
## [subcode]

class Animal:
    def __init__(self, name, color, age):
        self.__name = name
        self.__color = color
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return "{} {} {}".format(self.name, self.color, self.age)
class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Cow(Animal):
    pass

cat = Cat('Васька', 'Белый', 1.5)
print(cat)

dog = Dog("Бобик", "Черный", 2.5)
print(dog)
## [subcode]

class A(object):
    def method1(self):
        print("methdo1 class A")

class B(A):
    def method1(self):
        super().method1()
        print("method1 class B")

a = A()
b = B()
a.method1()
b.method1()

## [subcode]

class A(object):
    @staticmethod
    def f():
        print('f')

    @classmethod
    def cm(cls):
        print("it is called for class: ", cls)

a = A()
a.f()
A.cm()

## [subcode]

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

class Dog(Animal):

    def __init__(self):
        self.__name = 'dog'
        
    #@property
    def name(self):
        return self.__name
#animal = Animal()
dog = Dog()
print(dog.name())

