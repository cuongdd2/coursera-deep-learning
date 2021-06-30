### Word representation
- One hot presentation can't show the relationship between similar words (orange, apple...)
- We need to embed meanings or features to word
- We featurize word, gender -> man, women, king, queen.... royal -> , age , food, human
### Word embeddings
- t-SNE algo to translate 300 features to 3D map
- words on  2D map can easily grouping together, like K-Mean
- NLP application

### Transfer learning and word embeddings
- learn embeddings from large text corpus (1-100B words) (download pre-trained)
- transfer embedding to new task with smaller training set (100k words)
- 10k dimensional one-hot vector -> 300 dense vector
- optional: continue to finetune to word embeddings with new data
- usefull for text summarization, generating but not popular for machine translation. 
  maybe okay with small set of translateion
  
Face encoding -> 128D 
word embedding -> 10k words x 300D features
e-man e-woman: embedding vector
###  Properties of Word Embeddings
e-man - e-woman = E
find e-? where e-king - e-? = E
finding analogies using word vectors
(man, woman) ->  is === (king-?) ->
find word w: argmax sim(e-w, e-king - e-man + e-woman)

t-SNE mapping no-linear 300D to 2D . won't keep the vector, parallel mapping

#### Cosine similarity
- use to calculate similarity
- cos(angle) between 2 vector
- sim(Ew, Eking - Eman + Ewoman)

### Embedding matrix
- word vocabulary: 10k words
- features: 300 dimensional
- E (embedding) matrix: (300x10000) size
- O-word = (10000, 1)
- E-word: embeded features

### Learning word embeddings
- The first algo / model is complex and use a lot of computations
- Overtime, it's improved to make it simpler but still very useful, just keep the core component
- Input: sequence of words -> map with E matrix -> sequence of e-values -> NN -> softmax (10k)
- fixed history: only use fixed n prev words for input
- predict `target` word by using `context` words (left and right)
- context words: last 4 words, left, right word, nearby 1 word

## Word2Vec model
Published 2013 Mikolov
###Skip grams:
- choose random context and target word
- context c -> target t supervised learning
- Oc -> E -> ec -> O(softmax) -> y^
- Hierarchical softmax (tree) so softmax run in log(n) time
- tree is prioritized by frequent of word
- remove frequent and less meaning word (the, of, a, and, to...)
- softmax is expensive p(c|t) = e-t / sum(e-vocab)
### Negative sampling
- pick context and target word, labelled as 1
- k times context word, pick random negative word in vocabulary -> label as 0
- k: 5-29 small dataset, 2-5 large data set
- P(y=1 | c,t) = sigmoid(theta-t * e-context)

## GloVe Word Vectors
- Global Vector for word representation: 2014 Pennington
- Xij = # times j appears in  context of i
- Xij = Xji
- Model: minimize sum(1..10k)sum(1..10k)f(Xij)(theta-i.T * ej + bi + bj' - logXij)**2
- f(Xij) weighting term. f(Xij) = 0 if Xij = 0
- weighting function to give more meaning to less frequent words and vice versa
- 

## Sentiment classification problem
- From large corpus of text, calculate matrix E of word embedding
- Use 300D vector of embedding values, feed in RNN to train with labelled sentence -> rating

## Debiasing word embeddings
- Bolukbasi 2016
- identify bias direction
- Ehe - Eshe, Emale - Efemale -> average
- try to neutralize some words, equalize pairs girl - boy