Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> a
10
>>> arr = [10, 20, 30, 'python', 1.2, True]
>>> arr
[10, 20, 30, 'python', 1.2, True]
>>> arr1 = 10
>>> arr2 = 20
>>> arr1 * 5
50
>>> arr[0]
10
>>> arr[3]
'python'
>>> i = 0
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> len(arr)
6
>>> ar
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ar
NameError: name 'ar' is not defined
>>> arr
[10, 20, 30, 'python', 1.2, True]
>>> size = len(arr)
>>> i = 0
>>> while i < size:
	print(arr[i])
	i += 1

	
10
20
30
python
1.2
True
>>> while i < size:
	print(arr[i])
	i += 1
KeyboardInterrupt
>>> n = 0
>>> while n < size:
	i = arr[n]
	print(i)
	n += 1

	
10
20
30
python
1.2
True
>>> for item in arr:
	print(item)

	
10
20
30
python
1.2
True
>>> arr[0] = -100
>>> arr
[-100, 20, 30, 'python', 1.2, True]
>>> arr.append(False)
>>> arrr
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    arrr
NameError: name 'arrr' is not defined
>>> arr
[-100, 20, 30, 'python', 1.2, True, False]
>>> len(arr)
7
>>> text = "python"
>>> text[0]
'p'
>>> text[0] = 'P'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    text[0] = 'P'
TypeError: 'str' object does not support item assignment
>>> arr = ['p', 'y', 't', 'h', 'o', 'n']
>>> py = ['p', 'y', 't', 'h', 'o', 'n']
>>> py
['p', 'y', 't', 'h', 'o', 'n']
>>> py[0] = 'P'
>>> py
['P', 'y', 't', 'h', 'o', 'n']
>>> spy = "python"
>>> spy
'python'
>>> spy[0]
'p'
>>> spy[0] = 'P'
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    spy[0] = 'P'
TypeError: 'str' object does not support item assignment
>>> spy.
SyntaxError: invalid syntax
>>> spy.capitalize()
'Python'
>>> spy
'python'
>>> newPy = spy.capitalize()
>>> newPy
'Python'
>>> spy
'python'
>>> lst = [1, 2, 3]
>>> len(lst)
3
>>> lst = [1, 2, [1, 2, 3]]
>>> len(lst)
3
>>> lst[0]
1
>>> lst[1]
2
>>> lst[2]
[1, 2, 3]
>>> inner = lst[2]
>>> inner
[1, 2, 3]
>>> inner[1]
2
>>> lst[2][1]
2
>>> lst[1][1]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    lst[1][1]
TypeError: 'int' object is not subscriptable
>>> lst.append('test')
>>> lst
[1, 2, [1, 2, 3], 'test']
>>> len(lst)
4
>>> lst[3]
'test'
>>> lst[3][1]
'e'
>>> r = [1,2,3,4,5,6,7,8,9,10]
>>> r
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in r:
	print (i)

	
1
2
3
4
5
6
7
8
9
10
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> friends
['Joseph', 'Glenn', 'Sally']
>>> for friend in friends:
	print("My frend No" + firend)

	
Traceback (most recent call last):
  File "<pyshell#77>", line 2, in <module>
    print("My frend No" + firend)
NameError: name 'firend' is not defined
>>> for friend in friends:
	print("My frend No" + friend)

	
My frend NoJoseph
My frend NoGlenn
My frend NoSally
>>> for no in [0, 1, 2]:
	print("My friend No " + (no + 1) + " is " + friend)

	
Traceback (most recent call last):
  File "<pyshell#82>", line 2, in <module>
    print("My friend No " + (no + 1) + " is " + friend)
TypeError: Can't convert 'int' object to str implicitly
>>> for no in [0, 1, 2]:
	print("My friend No " + str(no + 1) + " is " + friend)

	
My friend No 1 is Sally
My friend No 2 is Sally
My friend No 3 is Sally
>>> for no in [0, 1, 2]:
	print("My friend No " + str(no + 1) + " is " + friends[no])

	
My friend No 1 is Joseph
My friend No 2 is Glenn
My friend No 3 is Sally
>>> for no in [0, 1, 2]:
	print("My friend No " + str(no + 1) + " is " + friends[no])

	
My friend No 1 is Joseph
My friend No 2 is Glenn
My friend No 3 is Sally
>>> friends.append("Bob")
>>> friends
['Joseph', 'Glenn', 'Sally', 'Bob']
>>> for no in [0, 1, 2]:
	print("My friend No " + str(no + 1) + " is " + friends[no])

	
My friend No 1 is Joseph
My friend No 2 is Glenn
My friend No 3 is Sally
>>> type(range)
<class 'type'>
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in range(4):
	print("My friend No " + str(i + 1) + " is " + friends[i])

	
My friend No 1 is Joseph
My friend No 2 is Glenn
My friend No 3 is Sally
My friend No 4 is Bob
>>> friends.re
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    friends.re
AttributeError: 'list' object has no attribute 're'
>>> friends.remove('Sally')
>>> friends
['Joseph', 'Glenn', 'Bob']
>>> for i in range(4):
	print("My friend No " + str(i + 1) + " is " + friends[i])

	
My friend No 1 is Joseph
My friend No 2 is Glenn
My friend No 3 is Bob
Traceback (most recent call last):
  File "<pyshell#103>", line 2, in <module>
    print("My friend No " + str(i + 1) + " is " + friends[i])
IndexError: list index out of range
>>> for i in range(len(friends)):
	print("My friend No " + str(i + 1) + " is " + friends[i])

	
My friend No 1 is Joseph
My friend No 2 is Glenn
My friend No 3 is Bob
>>> for i in range(len(friends)):
	print("My friend No", str(i + 1), " is ", friends[i])

	
My friend No 1  is  Joseph
My friend No 2  is  Glenn
My friend No 3  is  Bob
>>> lst = []
>>> lst.append('first')
>>> len(lst)
1
>>> 
