from functools import reduce

def checkio(number):
    up = 1e6
    na = []
    while up > 1:
        na.append(number//up)
        number -= na[-1]*up
        up/=10
    na.append(number)    
    return  int(reduce(lambda x, y: x*y, filter(lambda x: x>0, na)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
