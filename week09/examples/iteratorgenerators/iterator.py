
l = [1, 2, 3]
it = iter(l) # l.__iter__()
while True:
    try:
        x = next(it) # it.__next__()
    except StopIteration:
        break
    print(x)

class Droid:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Droid " + self.__name

    def __repr__(self):
        return "Droid " + self.__name

class Shop:
    def __init__(self):
                     #     0                1            2
        self.droids = [Droid("R2D2"), Droid("C3PO"), Droid("BB8")]

    def __getitem__(self, idx):
        if idx < len(self.droids):
            return self.droids[idx]
        else:
            raise IndexError

    # def __iter__(self):
    #     self.idx = 0
    #     return self
    #
    # def __next__(self):
    #     if self.idx < len(self.droids):
    #         droid = self.droids[self.idx]
    #         self.idx += 1
    #         return droid
    #     else:
    #         raise StopIteration


shop = Shop()

for droid in shop:
    print(droid)

droids = list(shop)
print(droids)

import random
class RandomGenerator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < self.count:
            rnd = random.randint(1, 100)
            self.idx += 1
            return rnd
        else:
            raise StopIteration

r = RandomGenerator(5)
for rnd in r:
    print(rnd)


