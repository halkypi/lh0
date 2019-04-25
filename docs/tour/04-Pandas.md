---
layout: default
title: Pandas
published: true
parent: Tour
nav_order: 4
---

# Pandas
{: .no_toc }

* TOC
{:toc}

Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

Library documentation: <a>http://pandas.pydata.org/</a>

### General


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
# create a series
s = pd.Series([1,3,5,np.nan,6,8])
s
```


```python
# create a data frame
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df
```


```python
# another way to create a data frame
df2 = pd.DataFrame(
    { 'A' : 1.,
      'B' : pd.Timestamp('20130102'),
      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
      'D' : np.array([3] * 4,dtype='int32'),
      'E' : 'foo' })
df2
```


```python
df2.dtypes
```


```python
df.head()
```


```python
df.index
```


```python
df.columns
```


```python
df.values
```


```python
# quick data summary
df.describe()
```


```python
df.T
```


```python
# axis 0 is index, axis 1 is columns
df.sort_index(axis=1, ascending=False)
```


```python
# can sort by values too
df.sort_values(by=['B'])
```

### Selection


```python
# select a column (yields a series)
df['A']
```


```python
# column names also attached to the object
df.A
```


```python
# slicing works
df[0:3]
```


```python
df['20130102':'20130104']
```


```python
# cross-section using a label
df.loc[dates[0]]
```


```python
# getting a scalar value
df.loc[dates[0], 'A']
```


```python
# select via position
df.iloc[3]
```


```python
df.iloc[3:5,0:2]
```


```python
# column slicing
df.iloc[:,1:3]
```


```python
# get a value by index
df.iloc[1,1]
```


```python
# boolean indexing
df[df.A > 0]
```


```python
df[df > 0]
```


```python
# filtering
df3 = df.copy()
df3['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df3[df3['E'].isin(['two', 'four'])]
```


```python
# setting examples
df.at[dates[0],'A'] = 0
df.iat[0,1] = 0
df.loc[:, 'D'] = np.array([5] * len(df))
df
```


```python
# dealing with missing data
df4 = df.reindex(index=dates[0:4],columns=list(df.columns) + ['E'])
df4.loc[dates[0]:dates[1],'E'] = 1
df4
```


```python
# drop rows with missing data
df4.dropna(how='any')
```


```python
# fill missing data
df4.fillna(value=5)
```


```python
# boolean mask for nan values
pd.isnull(df4)
```

### Operations


```python
df.mean()
```


```python
# pivot the mean calculation
df.mean(1)
```


```python
# aligning objects with different dimensions
s = pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
df.sub(s,axis='index')
```


```python
# applying functions
df.apply(np.cumsum)
```


```python
df.apply(lambda x: x.max() - x.min())
```


```python
# simple count aggregation
s = pd.Series(np.random.randint(0,7,size=10))
s.value_counts()
```

### Merging / Grouping / Shaping


```python
# concatenation
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
```


```python
# SQL-style join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key')
```


```python
# append
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
s = df.iloc[3]
df.append(s, ignore_index=True)
```


```python
df = pd.DataFrame(
    { 'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
      'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
      'C' : np.random.randn(8),
      'D' : np.random.randn(8) })
df
```


```python
# group by
df.groupby('A').sum()
```


```python
# group by multiple columns
df.groupby(['A','B']).sum()
```


```python
df = pd.DataFrame(
    { 'A' : ['one', 'one', 'two', 'three'] * 3,
      'B' : ['A', 'B', 'C'] * 4,
      'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
      'D' : np.random.randn(12),
      'E' : np.random.randn(12)} )
df
```


```python
# pivot table
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
```

### Time Series


```python
# time period resampling
rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample('5Min').sum()
```


```python
rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
```


```python
ps = ts.to_period()
ps.to_timestamp()
```

### Plotting


```python
# time series plot
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
```


```python
# plot with a data frame
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure(); df.plot(); plt.legend(loc='best')
```

### Input / Output


```python
# write to a csv file
df.to_csv('foo.csv', index=False)
```


```python
# read file back in
path = r'foo.csv'
newDf = pd.read_csv(path)
newDf.head()
```


```python
# remove the file
import os
os.remove(path)
```


```python
# can also do Excel
df.to_excel('foo.xlsx', sheet_name='Sheet1')
```


```python
newDf2 = pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
newDf2.head()
```


```python
os.remove('foo.xlsx')
```


```python

```
