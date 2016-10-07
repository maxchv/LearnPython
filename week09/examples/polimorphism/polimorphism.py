a = 2
b = 2
print(a * b)    # 4

a = "2"
print(a * b)    # '22'




class A:
    name = "A"
    def __init__(self):
        print("Init class A")


class B(A):
    name = "B"
    def __init__(self):
        super().__init__()
        print("Init class B")

b = B()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self):
        return "x: {} y: {}".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



p1 = Point(1, 2)
p2 = Point(2, 3)

p3 = p1 + p2
p3 += p2
print(p3)
print(p1 == p2)

class A:
    def oper(self, x, y):
        num = x + y
        return num


class B(A):  # Наследуем класс "А"
    def oper(self, x, y):  # <-----
        num = x / y
        return num

obj1 = A()
obj2 = B()

print(obj1.oper(2, 4))
print(obj2.oper(2, 4))

class A:
    def foo(self):
        print("foo")


class B(A):  # Наследуем класс "А"
    def foo(self):
        super().foo()
        print("boo")

obj1 = A()
obj2 = B()

obj1.foo()
obj2.foo()

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    def __init__(self, x, y, z):
        Point2D.__init__(self, x, y)
        self.z = z

p = Point3D(10, 10, 20)
print(p.x, p.y, p.z)