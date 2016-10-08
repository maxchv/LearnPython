

# >>> mylist = [1, 2, 3]
# >>> for i in mylist :
# ... print(i)
# 1
# 2
# 3
# Mylist

class mylist(object):
    __slots__ = ("lst", "idx")

    def __init__(self, lst = []):
        self.lst = lst.copy()
        self.idx = 0

    def __str__(self):
        return ", ".join(map(str, self.lst))

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < len(self.lst):
            item = self.lst[self.idx]
            self.idx += 1
            return item
        else:
            raise StopIteration()

l = mylist(list(range(3)))
print(l)

it = iter(l)
item = next(it)
print(item)

item = next(it)
print(item)

item = next(it)
print(item)

for item in l:
    print(item)

print(10 in l)
import random
def foo():
    if random.randint(0, 1):
        return 1
    else:
        return 2

#print(next(iter(foo, 1)))

class Cotainer:
    def __contains__(self, item):
        return True

c = Cotainer()
print(10 in c )

class MyRange:
    def __getitem__(self, item):
        if item < 5:
            return item
        else:
            raise IndexError(item)


print(list(MyRange()))

