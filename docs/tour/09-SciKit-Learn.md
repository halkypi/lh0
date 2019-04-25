---
layout: default
title: Scikit-learn
published: true
parent: Tour
nav_order: 9
---

# SciKit-Learn

Scikit-learn contains simple and efficient tools for data mining and data analysis.  It implements a wide variety of machine learning algorithms and processes to conduct advanced analytics.

Library documentation: <a>http://scikit-learn.org/stable/</a>

#### Classification with a Naive Bayes

- 2 classes of headlines "upworthy" (1) and "not upworthy" (0) 
- Load the data
- Featurize the data
- Train and Test the classifier the *right* way
- Use the model to predict new headlines

#### Let's start with a helper function for loading the raw data


```python
def import_titles(filename):
    #Imports text file
    titles = open(filename, 'rb').read()
    # Handles unicode encode/decode
    titles = titles.decode('utf-8')
    titles = titles.encode('ascii', 'ignore')

    return titles.splitlines()
```


```python
upworthy_titles = import_titles('./data/upworthy_titles.txt')

print(len(upworthy_titles))
upworthy_titles[:5] # first five

```


```python
times_titles = import_titles('./data/not_upworthy_titles.txt')

print(len(times_titles))
times_titles[:5] # first five
```

### What we want the data to look like next

| upworthy | titles
|:-----------|:------------|
| 1 | He Was About To Take His Own Life — Until A Man Stopped Him. Here He Meets Him Face To Face Again     
| 0 | CVS Pharmacy to Stop Selling Tobacco Goods by October  
| 0 | Twitter’s Share Price Falls After It Reports a Loss 
| 1 | A 16-Year-Old Explains Why Everything You Thought You Knew About Beauty May Be Wrong. With Math.



```python
#Set up placehold lists
upworthy = []
titles   = []

#Go through all the upworthy articles
for title in upworthy_titles:
    #add title to title list
    titles.append(title)
    #add 1 to Y list
    upworthy.append(1) # Upworthy = 1

for title in times_titles:
    titles.append(title)
    upworthy.append(0) # Upworthy = 0  
```

### What the machine wants the data to look like next

| upworthy | stop   | man  | obama  | explain  | everything  | you  | nato  | debate | industry | believe  
|:-----------|:----:| :----:| :----:| :----:| :----:| :----:| :----:| :----:| :----:| :----:| :----:| 
| 1       | 0 | 1  | 0 | 0  | 0 | 2  | 0 | 0  | 0 | 1  
| 0       | 1 | 0  | 0 | 0  | 0 | 0  | 1| 1 | 0 | 0  
| 0       | 0 | 0  |1 | 1  | 0 | 0  | 0 | 0  | 1 | 0  
| 1       | 0 | 0  | 0 | 0  | 0 | 1  | 0 | 1   | 0 | 0  



```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(lowercase     = True ,
                             min_df        = 2 ,
                             max_df        = .5 ,
                             ngram_range   = (1, 1),
                             stop_words    = 'english', 
                             strip_accents = 'unicode')
vectorizer.fit(titles)
X = vectorizer.transform(titles)
```

### Fit a Multinomial Naive Bayes Classifier


```python
from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(X,upworthy)

# Predict on the same data used for training (don't do this at home)
y_hat = clf.predict(X) 

# Print out some predictions
y_hat[:20]
```

### What % were correctly predicted?


```python
clf.score(X, upworthy)
```

### Use better fit statistics (a confusion matrix)


```python
# A helper function to plot the matrix
import itertools
import numpy as np
import matplotlib.pyplot as plt

def plot_confusion_matrix(cm):
    plt.matshow(cm,cmap=plt.cm.Blues)
    classes = ['not upworthy','upworthy']
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    # Plot Values
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center", color="black")

    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.show()

# Create and plot confusion matrix
from sklearn import metrics
cm = metrics.confusion_matrix(upworthy, y_hat)

plot_confusion_matrix(cm)
```

### Data scientists care about over fitting...so should we


```python
from sklearn.model_selection import train_test_split

# Split Test / Train
X_train, X_test, y_train, y_test = train_test_split(X, upworthy, test_size=0.3)
```


```python
clf.fit(X_train, y_train)
y_test_pred = clf.predict(X_test)

print("classification accuracy:", metrics.accuracy_score(y_test, y_test_pred))
cm = metrics.confusion_matrix(y_test, y_test_pred)
plot_confusion_matrix(cm)
```

This is unstable for some reason (skip for now):
```
from sklearn import cross_validation

cross_validation.cross_val_score(clf, X, np.array(upworthy),  cv=10)

np.mean(cross_validation.cross_val_score(clf, X, np.array(upworthy),  cv=10))
```

### What about for predicting new headlines?


```python
soc_title = 'Educational Assortative Mating and Earnings Inequality in the United States'
soc_title_vector = vectorizer.transform([soc_title])
clf.predict_proba(soc_title_vector)
```


```python
gawker_title = 'Shocking Footage Aired of Police Shooting Face-Eating Nude Man'
gawker_title_vector = vectorizer.transform([gawker_title])
clf.predict_proba(gawker_title_vector)
```


```python

```
