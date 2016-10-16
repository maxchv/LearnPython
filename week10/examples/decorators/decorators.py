
from datetime import datetime
import functools

def counter(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print("Start")
        start = datetime.now()
        result = function(*args, **kwargs)
        end = datetime.now()
        print("End")
        print( "deltatime: {} ms".format((end-start).microseconds) )
    #wrapper.__name__ = function.__name__
    #wrapper.__doc__ = function.__doc__

    return wrapper

@counter
def iterate():
    """
    Some work
    :return:
    """
    #start = datetime.now()
    for i in range(10000000):
        pass
    #end = datetime.now()
    #print( (end-start).microseconds )

#iterate = counter(iterate)
print(iterate.__doc__)
iterate()

@counter
def foo():
    for i in range(100):
        print("Hello decorator")

foo()