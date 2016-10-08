
def foo(x):
    print (x)
    x = int(x)
    print (x + 4)
    y = str(x)
    print (y + "5")
    return (y)
z = foo(6.5)

## [subcode]

lst = ["open", "close", "in", "out", "up", "down" ]
for i in range(0,6,2):
    print (lst[i])

    
## [subcode]

_____ oddOrEven( number ):
    in number _____ 2 == 0:
        _______ "even"
    _____ :
        _______ "odd"

## [subcode]

if (0 + 1 == True):
    print("false")
if(5/2 > 2):
    print ("banana")
else:
    print("pear")
if(type("2") == int):
    print("apple")
elif 23 % 7 == 2:
    print("peach")
if(int(3.1) == float(3.0)):
    print "watermelon"

    
## [subcode]

if 5<5:
    print ("A")
if 5+5:
    print ("B")
elif 5==5:
    print ("C")
if "D":
    print ("D")
if 0:
    print ("E")
else:
    print ("F")

    
## [subcode]


def greetingCard():
    name = input("please enter your name:")
    age = input("please enter your age:")
    if (age <= 12)
        message = "new toys"
    elif (age > 12) and (age <= 20):
        message = "angst and trendy stuff"
    elif (age >= 21) and (age < 40):
        message = "drinks"
    Else:
        message = "time to turn 40 again"
    print ("Happy birthday {} Hope you get lots of {}" name message)
    
## [question 7]

def countUp(start, end):
    while(start < end - 1):
        start += 1
        print(start)
        
## [question 8]
        
def smallestOfThree(a, b, c):
    if a <= b:
        return a if a < c else c
    else:
        return b if b < c else c
   
## [question 9]

def longWords(*args):
    for w in filter(lambda w: len(w)>5, args):
        print(w)





