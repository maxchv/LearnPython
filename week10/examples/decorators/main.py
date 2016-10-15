def generator():
    print("Started")
    x = 42
    yield x
    print("Continue")
    x += 1
    yield x
    print("Done")

print(type(generator))
g = generator()
print(type(g))
x = next(g)
print(x)
x = next(g)
print(x)
# x = next(g)
# print(x)

def unique(iterable):
    seen = []
    for item in iterable:
        if item not in seen:
            seen.append(item)
            yield item

xs = [1, 1, 2, 3]
print(unique(xs))
print(list(unique(xs)))
print(1 in unique(xs))

def enum(itertable, start = 0):
    i = start
    for item in itertable:
        yield (i, item)
        i += 1

print(list(enum([1,2,3])))

import functools

def decor(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(">>> Start function {}"
                    .format(f.__name__))
        result = f(*args, **kwargs)
        print("<<< End function {}"
                    .format(f.__name__))
        return result
    #wrapper.__name__ = f.__name__
    #wrapper.__doc__ = f.__doc__

    return wrapper
@decor
def foo():
    print("Foo")

foo()
#foo = decor(foo)
foo()

def repeater(count):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            for i in range(count):
                function(*args, **kwargs)
        return wrapper
    return decorator

@repeater(3)
def boo() -> None:
    print("boo")

boo()

def singletor(cls):
    instance = None

    @functools.wraps(cls)
    def wraper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return wraper

@singletor
class Foo():
    def __init__(self):
        self.foo = "foo"

foo = Foo()
print(foo.foo)
print(id(foo))
foo.foo = "boo"
boo = Foo()
print(id(boo))
print(boo.foo)

