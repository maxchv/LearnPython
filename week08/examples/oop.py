
## [class Car]

class Car(object): 
    color = "red"  # свойство класса (атрибут)

    def info(self): # метод класса
        print (self.color + "!")

ferrary = Car()        # создание объекта

print (ferrary.color)  # red

ferrary.info()         # red!

print (Car.color)      # red

## [class attributes]

class Car(object): 
    color = "red"  # свойство класса (атрибут)

    def info(self): # метод класса
        print (self.color + "!")

ferrary = Car()        # создание объекта
cadilac = Car()

ferrary.info()
cadilac.info()

Car.color = 'silver'

ferrary.info()
cadilac.info()

## [object attributes]

class Car(object): 

    def set_color(self, color):
        self.color = color

    def info(self): # метод класса
        print (self.color + "!")

ferrary = Car()
ferrary.set_color("red")
cadilac = Car()
cadilac.set_color("silver")

ferrary.info()
cadilac.info()
print(ferrary.color)

## [private attributes]

class Car(object): 

    def set_color(self, color):
        self.__color = color

    def info(self): # метод класса
        print (self.__color + "!")

ferrary = Car()
ferrary.set_color("red")

ferrary.info()
print(ferrary.__color)

## [proerties]

class Car(object):
    
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @color.deleter
    def color(self):
        del self.__color

ferrary = Car()
ferrary.color = "red"
del ferrary.color
print(ferrary.color)

## [constructor]

class Car(object): 

    def __init__(self, color):
        self.__color = color

    def info(self): # метод класса
        print (self.__color + "!")

ferrary = Car("red")

ferrary.info()

## [destructor]

class Car(object): 
    """
    Это класс машины
    """
    def __init__(self, color):
        self.__color = color
        print("Создали машинку")

    def __del__(self): # метод класса
        print ("В утилизацию")

ferrary = Car("red")

del ferrary

## [magic number]

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

a = Number(10)
b = Number(5)
c = a + b
print(c.value)
