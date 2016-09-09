## [subcode]

def square(lst):
    l = []
    for i in lst:
        #l += [i*i]
        l.append(i*i)

    return l

print(square(list(range(1, 11))))

## [subcode]
lst = [1, 2, 3]

def rsquare(lst):
    # рекурсия
    if len(lst) > 0:
        last = lst.pop()
        return rsquare(lst) + (last**2,)
    else:
        return ()

print("sq =",square(lst))
print("lst =", lst)

while True:
    

    
