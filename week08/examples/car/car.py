
class Car:
    """
    Класс автомобиль
    """

    #color = 'red' # атрибуты класса
    # name = 'ferrary'
    # speed = 250

    def __init__(self, color):
        self.__color = color

    def __del__(self):
        print("car is died")

    def set_color(self, value):
        self.__color = value

    @property
    def color(self):
        print("get color")
        return self.__color

    @color.setter
    def color(self, color):
        print("set color")
        self.__color = color

    def get_color(self):
        return self.__color

    def info(self):
        print(#"Название: " + self.name
             " цвет: " + self.__color)
            #+ " скорость: " + str(self.speed) )

def foo():
    ferrary = Car()
    # ferrary.set_color("red")
    ferrary.color = 'red'
    ferrary.info()

    Car.name = "cadilac"
    # Car.color = "silver"
    Car.speed = 200

    cadilac = Car()
    cadilac.color = "silver"
    cadilac.info()
    print("ferrary?")
    ferrary.info()

if __name__ == "__main__":
    ferrary = Car('black')
    #ferrary.color = "red"
    ferrary.info()
    print(ferrary.color)
    del ferrary
    print("the end")