## [local]

def f():
    x = 10
    print("x =", x)

f()
print("x =", x)

## [varargs]

def sum_nums(*nums):
    return sum(nums)
print(sum_nums(1,2,3,4,5))
