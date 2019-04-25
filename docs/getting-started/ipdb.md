---
layout: default
title: Ipython Debugger 
description: The ipython debugger 
parent: Getting Started
nav_order: 3
---
# Ipython Debugger 
## Running the ipython debugger (ipbd) from the command line
* TOC
{:toc}
---
*    Download `demo.py` from: <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/halkypi/sh/blob/gh-pages/assets/code/demo.py" target="_blank">here</a>
This has been copied from the `lib/python3.6/turtle.py`, ie the main turtle module.
*    Download a text editor like [notepad++](https://notepad-plus-plus.org/) or [sublime](https://www.sublimetext.com/) and view the file
*    Open a terminal and: `pip install ipdb`
*    Navigate to the directory where `demo.py` is saved and launch the ipython debugger

```
python -m ipdb demo.py

> /Users/halkypi/Downloads/demo.py(2)<module>()
      1 # Demos taken from: lib/python3.6/turtle.py
----> 2 from turtle import *
      3 import time
```

Typing `help` or `h` will open the help topics.  A number of commands have aliases, for example:

```
ipdb> h h

h(elp)
        Without argument, print the list of available commands.
        With a command name as argument, print help about that command.
        "help pdb" shows the full pdb documentation.
        "help exec" gives help on the ! command.

ipdb> h c

c(ont(inue))
        Continue execution, only stop when a breakpoint is encountered.
```
## Commands ##

The help menu lists all the commands:

``` 
ipdb> h

Documented commands (type help <topic>):
========================================
EOF    cl         disable  interact  next    psource  rv         unt
a      clear      display  j         p       q        s          until
alias  commands   down     jump      pdef    quit     source     up
args   condition  enable   l         pdoc    r        step       w
b      cont       exit     list      pfile   restart  tbreak     whatis
break  continue   h        ll        pinfo   return   u          where
bt     d          help     longlist  pinfo2  retval   unalias
c      debug      ignore   n         pp      run      undisplay
```

The commands we need to execute the code are:

| command | description
| :--- | :--- |
| list, l | show lines around current step |
| longlist, l | show more lines than list |
| continue, cont, c | execute each line until next breakpoint |
| break, b | display or set breakpoint |
| enable, disable | enable or disable breakpoints | 
| clear, cl | clear bp |
| next, n | execute line, functions are stepped over |
| step, s | execute line, functions are stepped into |
| until, unt | run until linenumber |
| return, r | execute each line until function returns (step out) |
| restart, run | restart the program |
| exit | exit the debugger |

*    Run the `help` or `h` command on `l` and `ll` then run them in the console.

```
ipdb> h l
ipdb> h ll
ipdb> l
ipdb> ll
```

![ipdb0](/lh/assets/images/ipdb0.png?raw=true){:width="500px"}

*    Enter `c` and watch the program `continue` to the end
*    Enter `run` to `restart` the program
*    Enter `h b` and read the `break` info

```
ipdb> h b

b(reak) [ ([filename:]lineno | function) [, condition] ]
Without argument, list all breaks.

With a line number argument, set a break at this line in the
current file.  With a function name, set a break at the first
executable line of that function.  If a second argument is
present, it is a string specifying an expression which must
to true before the breakpoint is honored.

line number may be prefixed with a filename and a colon,
to specify a breakpoint in another file (probably one that
hasn't been loaded yet).  The file is searched for on
sys.path; the .py suffix may be omitted.  
```

*    Repeat this for `enable`, `disable` and `clear`
*    Set a break point for demo2()
*    `continue` to the `break`

![ipdb1](/lh/assets/images/ipdb1.png?raw=true){:width="500px"}

*    Enter `n` to execute the `next` line
*    Press `<Enter>` or `<Return>` again to execute the last command
*    Keep pressing enter and watch each line being executed until the `for` loop on line 72.
*    Enter `p _` to `print` the number stored in the `_` value 

The `_` underscore is a throwaway variable because it doesn't mean anything once the `for` loop has finished.  

*    Break out of the loop by entering `until 75`

![ipdb2](/lh/assets/images/ipdb2.png?raw=true){:width="800px"}

## Exploring methods ##

The program enters a [while](https://www.youtube.com/watch?v=885qKiiKisI&feature=youtu.be) loop on line 76.  

*    Take a look at the `help` for `pdoc` and `pinfo` which provides information on a method
*    Have a look at the docstrings for `undobufferentries` and `undo` then enter `s` to `step` into the function
*    Once the function is called enter `ll` to view the `lib/python3.6/turtle.py(2603)undobufferentries()` source code

If we `print` the value we can see it is a buffer of all the entries in the `undobuffer`.  The function returns `0` when the buffer reaches `None`, otherwise it returns the count of entries.  

![ipdb3](/lh/assets/images/ipdb3.png?raw=true){:width="500px"}

*    Enter `r` so the `undobufferentries()` function returns and `step` into the `undo()` function
*    Note the example uses a `range(8)` instead of the number of entries in the buffer

![ipdb4](/lh/assets/images/ipdb4.png?raw=true){:width="500px"}

The `while` loop iterates through entries in the buffer and executes `undo()` on them until it hits `None`.  The buffer then returns `0` or `False` which breaks the loop. 

*    Enter `return` to step out of `undo` and enter `n` to move to the next line.  Hold down the `<Enter>` key to watch it `undo()` the buffer

## Restart and explore ##

*    `restart` the program
*    `clear` the breakpoint and use `n`, `s` and `r` to step through the program and explore methods
*    Browse turtle documentation and note examples come from the docs strings in the source code:  [https://docs.python.org/3.3/library/turtle.html](https://docs.python.org/3.3/library/turtle.html)
*    Comment out `demo2()` in `demo.py` and run `demo1()` 
*    Step through `peace.py` in the turtledemo module

With these simple tools it is possible to look under the hood, explore code, run examples and become fluent in any python package.  All it takes is a curious mind and some interactive exploration! 

Next, we'll add some data wrangling tools to the lab.

