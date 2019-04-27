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
