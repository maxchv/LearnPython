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
