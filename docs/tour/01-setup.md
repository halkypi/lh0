---
layout: default
title: Setup
published: true
parent: Tour
nav_order: 1
---
# Setup
{: .no_toc }

* TOC
{:toc}

## IPython Magic Commands

IPython has a system of commands we call 'magics' that provide effectively a mini command language that is orthogonal to the syntax of Python and is extensible by the user with new commands. Magics are meant to be typed interactively, so they use command-line conventions, such as using whitespace for separating arguments, dashes for options and other conventions typical of a command-line environment.

Magics come in two kinds:

Line magics: these are commands prepended by one % character and whose arguments only extend to the end of the current line.

Cell magics: these use two percent characters as a marker (%%), and they receive as argument both the current line where they are declared and the whole body of the cell.


```python
# brings up a documentation pane with an overview of IPython's feature
?
```


```python
# quick reference guide
%quickref
```


```python
# use the ! operator to run system shell commands
!ping www.google.com
```


```python
# several ways to interactively access help documentation
help
```


```python
# help module for magic commands
%magic
```


```python
# list of all available magic commands
%lsmagic
```


```python
# bring up the help module for a specific command
%timeit?
```


```python
# the ? syntax also works for any generic object
x = 5
x?
```


```python
# run a python script from within the notebook
%run hello.py
```


```python
# time the execution of a statement
import numpy as np
%timeit np.linalg.eigvals(np.random.rand(100,100))
```


```python
# list all environment variables or specific variables
%env SYSTEMROOT
```


```python
# print the cache of previously executed commands
%history
```


```python
# print the call signature for any object
import turtle
t = turtle.Turtle
t?
```


```python
# print the docstring for a class/callable object
%pdoc turtle.Turtle
```


```python
# print all interactive variables
%who
```


```python
# same as who but more information
%whos
```


```python
# reset the namespace
%reset
```

## Quick tour of Python

This is a collection of various statements, features, etc. of IPython and the Python language.  Much of this content is taken from other notebooks so I can't take credit for it, I just extracted the highlights I felt were most useful.

Code cells are run by pressing shift-enter or using the play button in the toolbar.


```python
a = 10
```


```python
print(a)
```


```python
import math
```


```python
x = math.cos(2 * math.pi)
print(x)
```

Import the whole module into the current namespace instead.


```python
from math import *
x = cos(2 * pi)
print(x)
```

Several ways to look at documentation for a module.


```python
print(dir(math))
```


```python
help(math.cos)
```

### Variables


```python
x = 1.0
type(x)
```


```python
# dynamically typed
x = 1
type(x)
```

### Operators


```python
1 + 2, 1 - 2, 1 * 2, 1 / 2
```


```python
# integer division of float numbers
3.0 // 2.0
```


```python
# power operator
2 ** 2
```


```python
True and False
```


```python
not False
```


```python
True or False
```


```python
2 > 1, 2 < 1, 2 > 2, 2 < 2, 2 >= 2, 2 <= 2
```


```python
# equality
[1,2] == [1,2]
```

### Strings


```python
s = "Hello world"
type(s)
```


```python
len(s)
```


```python
s2 = s.replace("world", "test")
print(s2)
```


```python
s[0]
```


```python
s[0:5]
```


```python
s[6:]
```


```python
s[:]
```


```python
# define step size of 2
s[::2]
```


```python
# automatically adds a space
print("str1", "str2", "str3")
```


```python
# C-style formatting
print("value = %f" % 1.0) 
```


```python
# alternative, more intuitive way of formatting a string 
s3 = 'value1 = {0}, value2 = {1}'.format(3.1415, 1.5)
print(s3)
```

### Lists


```python
l = [1,2,3,4]

print(type(l))
print(l)
```


```python
print(l[1:3])
print(l[::2])
```


```python
l[0]
```


```python
# don't have to be the same type
l = [1, 'a', 1.0, 1-1j]
print(l)
```


```python
start = 10
stop = 30
step = 2
range(start, stop, step)

# consume the iterator created by range
list(range(start, stop, step))
```


```python
# create a new empty list
l = []

# add an elements using `append`
l.append("A")
l.append("d")
l.append("d")

print(l)
```


```python
l[1:3] = ["b", "c"]
print(l)
```


```python
l.insert(0, "i")
l.insert(1, "n")
l.insert(2, "s")
l.insert(3, "e")
l.insert(4, "r")
l.insert(5, "t")

print(l)
```


```python
l.remove("A")
print(l)
```


```python
del l[7]
del l[6]

print(l)
```

### Tuples


```python
point = (10, 20)
print(point, type(point))
```


```python
# unpacking
x, y = point

print("x =", x)
print("y =", y)
```

### Dictionaries


```python
params = {"parameter1" : 1.0,
          "parameter2" : 2.0,
          "parameter3" : 3.0,}

print(type(params))
print(params)
```


```python
params["parameter1"] = "A"
params["parameter2"] = "B"

# add a new entry
params["parameter4"] = "D"

print("parameter1 = " + str(params["parameter1"]))
print("parameter2 = " + str(params["parameter2"]))
print("parameter3 = " + str(params["parameter3"]))
print("parameter4 = " + str(params["parameter4"]))
```

### Control Flow


```python
statement1 = False
statement2 = False

if statement1:
    print("statement1 is True")
elif statement2:
    print("statement2 is True")
else:
    print("statement1 and statement2 are False")
```

### Loops


```python
for x in range(4):
    print(x)
```


```python
for word in ["scientific", "computing", "with", "python"]:
    print(word)
```


```python
for key, value in params.items():
    print(key + " = " + str(value))
```


```python
for idx, x in enumerate(range(-3,3)):
    print(idx, x)
```


```python
l1 = [x**2 for x in range(0,5)]
print(l1)
```


```python
i = 0
while i < 5:
    print(i)
    i = i + 1
print("done")
```

### Functions


```python
# include a docstring
def func(s):
    """
    Print a string 's' and tell how many characters it has    
    """
    
    print(s + " has " + str(len(s)) + " characters")
```


```python
help(func)
```


```python
func("test")
```


```python
def square(x):
    return x ** 2
```


```python
square(5)
```


```python
# multiple return values
def powers(x):
    return x ** 2, x ** 3, x ** 4
```


```python
powers(5)
```


```python
x2, x3, x4 = powers(5)
print(x3)
```


```python
f1 = lambda x: x**2
f1(5)
```


```python
map(lambda x: x**2, range(-3,4))
```


```python
# convert iterator to list
list(map(lambda x: x**2, range(-3,4)))
```

### Classes


```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def __str__(self):
        return("Point at [%f, %f]" % (self.x, self.y))
```


```python
p1 = Point(0, 0)
print(p1)
```


```python
p2 = Point(1, 1)

p1.translate(0.25, 1.5)

print(p1)
print(p2)
```

### Exceptions


```python
try:
    print(test)
except:
    print("Caught an expection")
```


```python
try:
    print(test)
except Exception as e:
    print("Caught an exception: " + str(e))
```
