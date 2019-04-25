---
layout: default
title: Turtle Objects
description: Everything in Python is an object
parent: Getting Started
nav_order: 2
---
# Turtle Objects
## Introduction to python objects through Turtle graphics
Everything in Python is an object.  We'll explore basic object types using the turtle [demo](https://docs.python.org/3/library/turtle.html#module-turtledemo) because it:
*   can be boring to learn building blocks without making anything
*   helps to visualize abstract concepts with concrete examples

It is also good to reinforce the principle that it is possible to learn topics of interest through python packages.  Again, we'll use IDLE, not because it is the best development environment in the world, but because it's written in python and cross platform.  

## Resources

*    [Turtle Geometry: The Computer as a Medium for Exploring Mathematics - Artificial Intelligence](https://www.amazon.com/gp/product/0262510375)
*    [MIT AI Lab - Logo Turtle Graphics for the Lisp Machine](https://dspace.mit.edu/bitstream/handle/1721.1/41158/AI_WP_214.pdf?sequence=4)
*    [Turtle docs](https://docs.python.org/3.3/library/turtle.html?highlight=turtle)

## Importing the Zen of python

Python modules or programs are also objects and can imported.  Try:

```
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Import turtle

Importing turtle can be done in the same way.  The module is written using the gui package [tkinter](https://docs.python.org/3/library/tkinter.html).  Let's view and interact with a turtle object through IDLE.

```py
from turtle import *
mode('logo')
showturtle()
```

This opens a window and shows the turtle in logo mode.  The motion and drawing commands are:

| command | alias |
| :--- | :--- |
|showturtle()| st() |
|hideturtle()| ht() |
| forward()  | fd() |
| backward() | bk() |
|rightturn() | rt() |
|leftturn()  | lt() |
|penup()  | pu() |
|pendown()  | pd() |

*    Try this simple example in the Shell

![0](/lh/assets/images/turtle0.png?raw=true)

```
from turtle import *
mode('logo')
st()
fd(100)
rt(90)
fd(150)
lt(45)
bk(100)
lt(45)
pu()
fd(100)
```

*    Copy shapes.py below into a new file and run through the examples

```py
# shapes.py
from turtle import *
mode('logo')
reset()

# This is a comment
""" This is
a multi line
comment
"""
## see Format for comment toggling options

# Make a square

##fd(100)
##rt(90)
##fd(100)
##rt(90)
##fd(100)
##rt(90)
##fd(100)
##rt(90)

# Defining a Function

def square():           # indentation matters in python
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
    rt(90)

## square()

# Iterating with the range() function

## help(range)
## range(4)
## for i in range(4): print(i)
## for spam in range(4): print(spam)
## for spam in range(4): print("eggs!")
## for spam in "eggs": print(spam)

def square():
    for i in range(4):  
        fd(100)         # nested indentation
        rt(90)

# square()

# Pass in an argument

def square(size):
    for i in range(4):  
        fd(size)         
        rt(90)

##square(200)

def triangle(size):
    for i in range(3):
        fd(size)
        rt(120)

##triangle(100)

def polygon(size, sides):
    for i in range(sides):
        fd(size)
        rt(360 / sides)

##polygon(100, 5)

def house(size):
    square(size)
    fd(size)
    rt(30)
    triangle(size)

##house(100)

def boxes(size):
    for i in range(6):
        for j in range(6):
            fd(size)
            rt(60)
        rt(60)

##boxes(100)

def star(size):
    for i in range(5):
        fd(size)
        rt(144)
        fd(size)
        lt(72)

##star(100)

def star_group(size):
    for i in range(6):
        star(size / 4.0)
        pu()
        fd(size)
        pd()
        rt(60)

##speed(0) # 1 = slow, 10 = fast, 0 = fastest
##star_group(100)

def super_star_group(size):
    for i in range(4):
        star_group(size)
        pu()
        fd(size / 2.0)
        pd()
        rt(90)

##speed(0)  
##super_star_group(100)
```
## Turtle demo

In the IDLE shell go to: `Help > Turtle Demo` and run through the examples.

![1](/lh/assets/images/turtle1.png?raw=true)

## Debug yinyang.py

*    copy the script from the final example to the clipboard
*    paste into a `File > New File`
*    save in the code directory
*    turn on `Debug > Debugger`
*    check the Source and Globals boxes

| button | description
| :--- | :--- |
| Go | execute each line until next breakpoint |
| Step | execute line, functions are called |
| Over | execute line, functions are stepped over |
| Out | execute each line until next return |

*    run the program, set a breakpoint and click Go
*    clear breakpoint, run the program, and continue to click `over` until the program completes 
*    run the program again but this time `step` into the `main()` function on line 48
*    step into the reset() call on line 41

Notice the reset() function is not defined in yinyang.py but turtle.py instead.  To view this file go to `File > Open Module`.

![open-module](/lh/assets/images/open-module.png?raw=true)

![open-module2](/lh/assets/images/open-module2.png?raw=true)

![open-module3](/lh/assets/images/open-module3.png?raw=true)

*    continue to `step` through the code until the __init__.py file within the tkinter module opens.
*    use the step `out` button to return to the reset() call and `step` into it again.  

This time the debugger goes to the turtle.reset() call.
*    read through the reset() documentation in the comments

This is where python documentation is mastered, right there in the code.
*    browse through turtle.py, locate other key yinyang functions and browse the documentation 

This exercise is meant to be iterative, it will involve interacting with the `step`, `over` and `out` buttons in the debugger.  Step through all the yingyang code and get a sense for how it is working.  
```
backward()
begin_fill()
circle()
color()
down()
end_fill()
forward()
left()
right()
up()
width()
```
*    Read through [Al's description](http://inventwithpython.com/invent4thed/chapter6.html) of the debugger.

## Next Steps

There are many, many [excellent books](https://wiki.python.org/moin/PythonBooks) written on python.  One of the quickest ways to become fluent is to read well written code (ie the standard library) and interact with it.  Next we'll look at the command line and the [ipython debugger idpb...](https://github.com/gotcha/ipdb)

*    Do not fear the command line, there is no avoiding it in the open source world
*    Get into Linux too, there is no avoiding that either
*    Check out the Software Carpentry Foundation: [https://swcarpentry.github.io/shell-novice/](https://swcarpentry.github.io/shell-novice/)

![command-line](https://img.photobucket.com/albums/v647/vtel57/NSBLog/cli-fear_shot.jpg)


