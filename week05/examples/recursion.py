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

    

    
