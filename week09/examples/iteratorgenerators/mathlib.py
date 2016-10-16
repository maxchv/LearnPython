
def add(a, b):
    return a + b

class mylib:
    def sub(self, b):
        return self.a - b

    @staticmethod
    def add(a, b):
        print("a + b = " + str(a + b))
        return a + b

mylib.add(1, 2)
m = mylib()
m.add(1, 2)
print(add(1, 2))

m.a = 10
print(m.sub(5))