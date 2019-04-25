---
layout: default
title: NLTK
published: true
parent: Tour
nav_order: 8
---

# NLTK

NLTK is a leading platform for building Python programs to work with human language data.  It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, and an active discussion forum.

Library documentation: <a>http://www.nltk.org/</a>


```python
# needed to display the graphs
%matplotlib inline
```


```python
# import the library and download sample texts
import nltk
nltk.download('gutenberg')
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('nps_chat')
nltk.download('webtext')
nltk.download('treebank')
nltk.download('stopwords')
nltk.download('words')
nltk.download('wordnet')
nltk.download('brown')
nltk.download('names')
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
```


```python
from nltk.book import *
```


```python
# examine concordances (word + context)
text1.concordance("monstrous")
```


```python
text1.similar("monstrous")
```


```python
text2.common_contexts(["monstrous", "very"])
```


```python
# see where in a text certain words are found to occur
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
```


```python
# count of all tokens (including punctuation)
len(text3)
```


```python
# number of distinct tokens
len(set(text3))
```


```python
# the texts are just lists of strings
text2[141525:]
```


```python
# build a frequency distribution
fdist1 = FreqDist(text1) 
fdist1
```


```python
fdist1.most_common(20)
```


```python
fdist1['whale']
```


```python
fdist1.plot(20, cumulative=True)
```


```python
# apply a list comprehension to get words over 15 characters
V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)
```


```python
fdist2 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist2[w] > 7)
```


```python
# word sequences that appear together unusually often
text4.collocations()
```

## Raw Text Processing


```python
# download raw text from an online repository
from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
len(raw)
```


```python
raw[:75]
```


```python
# tokenize the raw text
from nltk import word_tokenize
tokens = word_tokenize(raw)
len(tokens)
```


```python
tokens[:10]
```


```python
text = nltk.Text(tokens)
text[1024:1062]
```


```python
text.collocations()
```


```python
raw.find("PART I")
```


```python
# HTML parsing using the Beautiful Soup library
from bs4 import BeautifulSoup
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = word_tokenize(raw)
tokens[0:10]
```


```python
# isolate just the article text
tokens = tokens[110:390]
text = nltk.Text(tokens)
text.concordance('gene')
```

## Regular Expressions


```python
# regular expression library
import re
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
```


```python
# match the end of a word
[w for w in wordlist if re.search('ed$', w)][0:10]
```


```python
# wildcard matches any single character
[w for w in wordlist if re.search('^..j..t..$', w)][0:10]
```


```python
# combination of caret (start of word) and sets
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
```


```python
chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))

# plus symbol matches any number of times repeating
[w for w in chat_words if re.search('^m+i+n+e+$', w)]
```


```python
wsj = sorted(set(nltk.corpus.treebank.words()))

# more advanced regex example
[w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)][0:10]
```


```python
[w for w in wsj if re.search('^[A-Z]+\$$', w)]
```


```python
[w for w in wsj if re.search('^[0-9]{4}$', w)][0:10]
```


```python
[w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)][0:10]
```


```python
[w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)][0:10]
```


```python
[w for w in wsj if re.search('(ed|ing)$', w)][0:10]
```


```python
# using "findall" to extract partial matches from words
fd = nltk.FreqDist(vs for word in wsj 
                      for vs in re.findall(r'[aeiou]{2,}', word))
fd.most_common(12)
```

## Normalizing Text


```python
# NLTK has several word stemmers built in
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
```


```python
[porter.stem(t) for t in tokens][0:10]
```


```python
[lancaster.stem(t) for t in tokens][0:10]
```


```python
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens][0:10]
```


```python
# also has a tokenizer that takes a regular expression as a parameter
text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x)    # set flag to allow verbose regexps
     ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
   | \w+(-\w+)*        # words with optional internal hyphens
   | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
   | \.\.\.            # ellipsis
   | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
'''
nltk.regexp_tokenize(text, pattern)
```

## Tagging


```python
# Use a built-in tokenizer and tagger
text = word_tokenize("They refuse to permit us to obtain the refuse permit")
nltk.pos_tag(text)
```


```python
# Word similarity using a pre-tagged text
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')
```


```python
# Tagged words are saved as tuples
nltk.corpus.brown.tagged_words()[0:10]
```


```python
nltk.corpus.brown.tagged_words(tagset='universal')[0:10]
```


```python
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.most_common()
```


```python
# Part of speech tag count for words following "often" in a text
brown_lrnd_tagged = brown.tagged_words(categories='learned', tagset='universal')
tags = [b[1] for (a, b) in nltk.bigrams(brown_lrnd_tagged) if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()
```


```python
# Load some raw sentences to tag
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
```


```python
# Default tagger (assigns same tag to each token)
tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
nltk.FreqDist(tags).max()
raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
default_tagger.tag(tokens)
```


```python
# Evaluate the performance against a tagged corpus
default_tagger.evaluate(brown_tagged_sents)
```


```python
# Training a unigram tagger
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag(brown_sents[2007])
```


```python
# Now evaluate it
unigram_tagger.evaluate(brown_tagged_sents)
```


```python
# Combining taggers
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(brown_tagged_sents, backoff=t0)
t2 = nltk.BigramTagger(brown_tagged_sents, backoff=t1)
t2.evaluate(brown_tagged_sents)
```

## Classifying Text


```python
# Define a feature extractor
def gender_features(word):
        return {'last_letter': word[-1]}
gender_features('Shrek')
```


```python
# Prepare a list of examples
from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
    [(name, 'female') for name in names.words('female.txt')])
import random
random.shuffle(labeled_names)
```


```python
# Process the names data
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
```


```python
classifier.classify(gender_features('Neo'))
```


```python
classifier.classify(gender_features('Trinity'))
```


```python
print(nltk.classify.accuracy(classifier, test_set))
```


```python
classifier.show_most_informative_features(5)
```


```python
# Document classification
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
```


```python
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
```


```python
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
```


```python
print(nltk.classify.accuracy(classifier, test_set))
```


```python
classifier.show_most_informative_features(5)
```
