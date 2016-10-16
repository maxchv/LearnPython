class A:
    def __init__(self):
        print("Init class A")
        self.init()

    @classmethod
    def init(cls):
        print("classmethod init() for " + cls.__name__)
        cls.name = "Class " + cls.__name__ # добавлебние атрибута класса!!!
        print(cls)

class B(A):
    pass

a = A()
print(A.name)
b = B()
print(B.name)