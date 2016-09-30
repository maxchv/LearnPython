
class Human:

    def set_money(self, money):
        self.__money = money

    def get_money(self, pin, money):
        if pin == self.__pin:
            if self.__money >= money:
                self.__money -= money
                return money
            else:
                print("Не достаточно денег на счету. Положи немного")
                return None
        else:
            print("Неверно введенный пин код. Ты трезв?")
            return None

    def set_data(self, name, age, pin):
        self.name = name
        self.age = age
        self.__pin = pin # закрытый атрибут

    def info(self):
        print(self.name, self.age, "$"+str(self.__money))

if __name__ == "__main__":
    vasja = Human()
    vasja.set_data("Вася", 34, 1234)
    #Human.set_data(vasja, "Вася", 34, 1234)
    vasja.set_money(10000)
    #print(vasja.__pin)
    vasja.info()

    m = vasja.get_money(2134, 1000)
    print(m)
    vasja.info()
    m = vasja.get_money(1234, 1000)
    print(m)
    vasja.info()
    m = vasja.get_money(1234, 10000)
    print(m)
    vasja.info()
    vasja.__money = 0
    vasja.info()