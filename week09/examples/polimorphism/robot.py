import abc

class Droid(metaclass=abc.ABCMeta):
    name = "Droid"
    id = 0

    def __init__(self):
        Droid.id += 1

    @abc.abstractmethod
    def info(self):
        pass

class R2D2(Droid):
    name = "R2D2"

    def info(self):
        print(self.name, "#", self.id)

    def __init__(self):
        R2D2.id += 1
        self.id = R2D2.id

class C3PO(Droid):
    name = "C3PO"

    def info(self):
        print(self.name, "#", self.id)

    def __init__(self):
        print("Robot is born")
        C3PO.id += 1
        self.id = C3PO.id

    def __del__(self):
        print("Robot is died")
        C3PO.id -= 1

robot1 = R2D2()
robot1.info()
robot1 = R2D2()
robot1.info()

robot3 = C3PO()
robot3.info()
del robot3
robot4 = C3PO()
robot4.info()

print(Droid.id)