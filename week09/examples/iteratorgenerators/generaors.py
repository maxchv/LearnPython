class Class1(object):
    @staticmethod
    def sum1(x, y):  # Статический метод
        return x + y

    def sum2(self, x, y):  # Обычный метод в классе
        return x + y

    def sum3(self, x, y):
        return Class1.sum1(x, y)  # Вызов из метода класса


print (Class1.sum1(10, 20))  # Вызываем статический метод
c1 = Class1()
print (c1.sum2(15, 6))  # Вызываем метод класса
print (c1.sum1(50, 12))  # Вызываем статический метод
# через экземпляр класса
print (c1.sum3(23, 5))  # Вызываем статический метод
# внутри класса