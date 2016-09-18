import mymodule
import random
import os.path

#print(dir(mymodule))

def hi():
    print("Hi")
mymodule.hello()

hi()
print(mymodule.test)

## [shortname module]

import mymodule as m
m.hello()

## [from]

from mymodule import hello
print(globals().keys())
print(test)

## [import all attributes]
from random import *
print(randint(10, 100))

## [subcode]

import mm
mm.hello()

