---
layout: default
title: NumPy
published: true
parent: Data science 101 for lawyers
nav_order: 3
---

# NumPy

NumPy is the fundamental package for scientific computing with Python. It contains among other things:

- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

Library documentation: <a>http://www.numpy.org/</a>


```python
from numpy import *
```


```python
# declare a vector using a list as the argument
v = array([1,2,3,4])
v
```


```python
# declare a matrix using a nested list as the argument
M = array([[1,2],[3,4]])
M
```


```python
# still the same core type with different shapes
type(v), type(M)
```


```python
M.size
```


```python
# arguments: start, stop, step
x = arange(0, 10, 1)
x
```


```python
linspace(0, 10, 25)
```


```python
logspace(0, 10, 10, base=e)
```


```python
x, y = mgrid[0:5, 0:5]
x
```


```python
y
```


```python
from numpy import random
```


```python
random.rand(5,5)
```


```python
# normal distribution
random.randn(5,5)
```


```python
diag([1,2,3])
```


```python
M.itemsize
```


```python
M.nbytes
```


```python
M.ndim
```


```python
v[0], M[1,1]
```


```python
M[1]
```


```python
# assign new value
M[0,0] = 7
M
```


```python
M[0,:] = 0
M
```


```python
# slicing works just like with lists
A = array([1,2,3,4,5])
A[1:3]
```


```python
A = array([[n+m*10 for n in range(5)] for m in range(5)])
A
```


```python
row_indices = [1, 2, 3]
A[row_indices]
```


```python
# index masking
B = array([n for n in range(5)])
row_mask = array([True, False, True, False, False])
B[row_mask]
```

### Linear Algebra


```python
v1 = arange(0, 5)
```


```python
v1 + 2
```


```python
v1 * 2
```


```python
v1 * v1
```


```python
dot(v1, v1)
```


```python
dot(A, v1)
```


```python
# cast changes behavior of + - * etc. to use matrix algebra
M = matrix(A)
M * M
```


```python
# inner product
v.T * v
```


```python
C = matrix([[1j, 2j], [3j, 4j]])
C
```


```python
conjugate(C)
```


```python
# inverse
C.I
```

### Statistics


```python
mean(A[:,3])
```


```python
std(A[:,3]), var(A[:,3])
```


```python
A[:,3].min(), A[:,3].max()
```


```python
d = arange(1, 10)
sum(d), prod(d)
```


```python
cumsum(d)
```


```python
cumprod(d)
```


```python
# sum of diagonal
trace(A)
```


```python
m = random.rand(3, 3)
m
```


```python
# use axis parameter to specify how function behaves
m.max(), m.max(axis=0)
```


```python
A
```


```python
# reshape without copying underlying data
n, m = A.shape
B = A.reshape((1,n*m))

B
```


```python
# modify the array
B[0,0:5] = 5
B
```


```python
# also changed
A
```


```python
# creates a copy
B = A.flatten()
B
```


```python
# can insert a dimension in an array
v = array([1,2,3])
v[:, newaxis], v[:,newaxis].shape, v[newaxis,:].shape
```


```python
repeat(v, 3)
```


```python
tile(v, 3)
```


```python
w = array([5, 6])
```


```python
concatenate((v, w), axis=0)
```


```python
# deep copy
B = copy(A)
```
