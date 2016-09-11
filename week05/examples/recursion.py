## [итеративная функция]

def square(lst):
    l = []
    for i in lst:
        #l += [i*i]
        l.append(i*i)

    return l

print(square(list(range(1, 11))))

## [функция с рекурсией]

lst = [1, 2, 3]
def rsquare(lst):    
    if len(lst) > 0:
        last = lst.pop()
        return rsquare(lst) + (last**2,) # рекурсия
    else:
        return ()

print("sq =",square(lst))
print("lst =", lst)

## [Фиббоначи]

def phib(n):
    lst = [1, 1]    
    for i in range(2, n):        
        lst.append(sum(lst[-2:]))
    return lst[:n]

print(phib(0))
print(phib(1))
print(phib(2))
print(phib(3))
print(phib(4))
print(phib(10))
