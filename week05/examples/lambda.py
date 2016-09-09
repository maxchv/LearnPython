## [def]

def add(a, b):
    return a + b

print("10 + 20 =",add(10, 20))

## [lambda]

add = lambda a, b: a + b
print("10 + 20 =", add(10, 20))

## [zip]

def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
