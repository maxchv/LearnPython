
class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x = {} y = {}".format(self.x, self.y)

    def __repr__(self):
        return "row data: x = {} y = {}".format(self.x, self.y)

    def __bool__(self):
        return self.x != 0 and self.y != 0

    def __gt__(self, p2):
        return self.x > p2.x and self.y > p2.y

    def __add__(self, p2):
        if isinstance(p2, Point2D):
            return Point2D(self.x + p2.x, self.y + p2.y)
        elif isinstance(p2, int):
            return Point2D(self.x + p2, self.y + p2)

p1 = Point2D(20, 30)
print(str(p1))
p2 = Point2D(5, y = 10)
print(p2)
p3 = p1 + p2
print(p3)
p4 = p1 + 10
print(p4)
if p1:
    print("Точка НЕ в начале координат")
else:
    print("Точка в начале координат")
