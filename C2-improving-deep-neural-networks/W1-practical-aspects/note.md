## Test / dev / test sets
Idea -> Code -> Experiment

NLP, Vision, Speech
Structural data
 - Ads
 - Search
 - Security
 - Logistic

Choices from 1 field may not transferable to a new field
How cycle improve -> how efficiency of cycle

Data sets:
 - train: 
 - dev: cross validation / hold-out
 - test:

70% / 30% or 60 / 20 / 20 when data sets # is 1000-10k
With big data: 1M set -> 10k sets for test is enough

Make sure dev and test sets com from same distribution

train/dev without test set might be okay

## Bias / Variance
High bias = under-fitting
High variance = over-fitting

High bias:
 - train error large
 - dev error large

High variance:
   - train error small
   - dev error large

Based on human / optimal (Bayes) error

## Basic recipe
Ask question:
 - High bias (training data) -> try bigger network, train longer, better NN architecture
 - High variance (dev data) -> more data, regularization, better NN architecture


