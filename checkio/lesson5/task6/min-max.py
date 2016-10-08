def check(kwargs, args, cmp):
    key = kwargs.get('key', None)
    
    if not key:
        key = lambda x: x
    if type(args[0]) == list or type(args[0]) == tuple:
        args = args[0]
    elif type(args[0]) == str or type(args[0]) == range:
        args = list(args[0])
        
    m = args[0]
    
    for arg in args:
        if cmp(key(arg), key(m)):
            m = arg
    return m

def min(*args, **kwargs):
    return check(kwargs, args, lambda x, y: x < y)


def max(*args, **kwargs):
    return check(kwargs, args, lambda x, y: x > y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
