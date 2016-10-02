class Human:
    def work(self):
        print("Human works")

class Horse:
    def work(self):
        print("Horse works")

    def age(self):
        print("age = 10")

class Kentavr(Horse, Human):
    # скрывает метод заового класса
    def work(self):
        self.age()
        print("Kentavr works")

kentavr = Kentavr()
kentavr.work()
print(Kentavr.mro())

from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty

# абстрактный базовы класс
class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    @abstractproperty
    def name(self):
        pass

    def get_name(self):
        return self.__name

class Dog(Animal):
    @property
    def name(self):
        return self.get_name()


#animal = Animal("???")
#print(animal.name)

bobik = Dog("Бобик")
print(bobik.name)