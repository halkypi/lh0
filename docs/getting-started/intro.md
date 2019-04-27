---
layout: default
title: Intro to Python
parent: Getting Started
has_children: true
nav_order: 1
---
# Intro to Python
{: .no_toc }
* TOC
{:toc}

We'll be using Python 3 because it's free, powerful, full stack ([Python is the second-best language for everything](https://twitter.com/jakevdp/status/994934052091318272?lang=en)) and the [lingua franca of data science](https://www.kaggle.com/learn/python).  There may also be a little [SQL](https://www.kaggle.com/learn/sql).

## Installation

### Download

There are different installations out there, Anaconda is awesome but a bit bloated for what we need to get started.  So let's install standard Python 3 (Python 2 is being deprecated in 2020) and then use python to install the packages we need as we go (some miniconda stuff).  Navigate to [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest version for your operating system.  Launch the executable, check the `Add Python to Path` box and accept the default settings.

![](https://github.com/halkypi/lh/blob/gh-pages/assets/images/install.gif?raw=true)

### Test installation
Open a [terminal](https://www.google.com/search?q=how+do+i+open+a+terminal), type in `python` and press enter.  You  should see three chevrons `>>>`, see below.  If this doesn't work you probably missed the `Add Python to Path` box, just reinstall. 

### First program

Type `print("Hello!")` at the interactive prompt.  You could also do some basic maths and then `exit()` when you're ready to move on.

```
$ python
>>> print("Hello!")
Hello!
>>> (3 + 2) * 3
15

```
*    Why doesn't it print 9?  
*    What would the output from these be?

```py
>>> 2 + 3 * 3
>>> 3 + 2 * 3
>>> exit()
exit
```

![](https://github.com/halkypi/lh/blob/gh-pages/assets/images/test-install.gif?raw=true)

### Some good 'getting started' guides

* [https://automatetheboringstuff.com/](https://automatetheboringstuff.com/)  This is arguably the best resource out there for getting started.  It's free to read online and there are some youtube videos.  Al is also a good egg.
* [https://docs.python.org/3/](https://docs.python.org/3/)  The docs!  Have a browse, the great thing about python is that everything is in python, the website, even the documentation is maintained with python - see [sphinx](http://www.sphinx-doc.org/).  
* [https://docs.python.org/3.3/library/turtle.html?highlight=turtle](https://docs.python.org/3.3/library/turtle.html?highlight=turtle)  Everything in python is an object, moving a turtle around makes it much easier to grasp the concept of [object oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming).  The turtle tutorial has also stood the test of time and is a quick way to learn the data types and the standard library.  Turtle graphics may have its roots in [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) but it is [not just for children](https://mitpress.mit.edu/books/turtle-geometry)!

![](https://mitpress.mit.edu/sites/default/files/styles/large_book_cover/http/mitp-content-server.mit.edu%3A18180/books/covers/cover/%3Fcollid%3Dbooks_covers_0%26isbn%3D9780262510370%26type%3D.jpg?itok=mTm47Oaz)

## Introduction to [IDLE](https://docs.python.org/3/library/idle.html)

Python is named after the 70's comedy show Monty Python so there are many references to famous sketches in 'the docs' and code.  For example, the package manager or [pip](https://packaging.python.org/tutorials/installing-packages/), is commonly referred to as the ['cheese shop'](https://www.youtube.com/results?search_query=cheese+shop+sketch+monty+python).  Most languages have an integrated development environment, or IDE, which programmers use to write and maintain their code.  **Id**l**e** (after [Eric Idle](https://en.wikipedia.org/wiki/Eric_Idle)) is the python one that comes with the standard installation.  Some people prefer [PyCharm](https://www.jetbrains.com/pycharm/) but a text editor (like [notepad++](https://notepad-plus-plus.org/download/v7.6.4.html), [sublime](https://www.sublimetext.com/3) or [vim](https://www.vim.org/download.php)) and the terminal also work well.  [Jupyter notebooks](https://jupyter.org/) are extremely popular with the data science community.  [Amazon SageMaker](https://aws.amazon.com/sagemaker/) comes with Notebooks, machine learning libraries and everything a developer would need to train, build and deploy a solution.

We'll stick with [IDLE](https://docs.python.org/3/library/idle.html) for now.  It has a decent debugger which means we can step through code, even [IDLE](https://docs.python.org/3/library/idle.html)'s, which is part of the [TKinter module](https://docs.python.org/3/library/tkinter.html#module-tkinter).  Reading or stepping through well written code is one of the quickest ways to gain fluency.

As we look at these different tools it will soon become apparent that there is a python module for just about everything.  So if you are curious about a technology, say web development, try learning [flask](http://flask.pocoo.org/).  

### Open [IDLE](https://docs.python.org/3/library/idle.html)

Earlier we ran a program through the python intepreter using the terminal.  Let's do the same with [IDLE](https://docs.python.org/3/library/idle.html).  The main appeal of python is this interactive, experimental approach.  It is possible to run complicated programs, load various data structures and then enter _interactive mode_ and explore from there.   Try this out:

```py
name = input("Enter your name\n> ")
print("Hello", name)
```
### First script

Click `File > New File`.  You should now have the interpreter (or shell) next to an untitled text file.  Put them side by side and rename the `File > Save As` `hello` in a new directory named `code` in your home directory.  You'll notice [IDLE](https://docs.python.org/3/library/idle.html) automatically adds the .py extension.  Save the file and `Run > Run Module` or `F5` to execute.  You should see:

![img0](/lh/assets/images/img0.png?raw=true)
[view](/lh/assets/images/img0.png)

### Next Steps

*    Read and complete the exercises in chapters 1 through 6 of [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
*    Review the [accompanying playlist](https://youtu.be/1F_OgqRuSdI)
*    Move on to [Turtle - an intro to python objects](https://halkypi.github.io/lh/turtle-objects/)
