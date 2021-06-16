## Bayes vs Human-level error
Bayes optimal error: the best possible error mapping X -> Y
 - no way to surpass
Human level error: 
   
Performance is slow when surpass human-level 

Humans are quite good at a lot of tasks
When ML is worse than humans
- get labeled data from humans
- gain insight from manual error analysis. Why did a person get this right?
- better analysis of bias/variance

Human-level error is a proxy for Bayes error

The diff between Bayes error and Training error: Avoidable bias
Diff between Training error and Dev error: Variance

## Definition of Human-level
- Typical human: 3%
- Typical doctor: 1%
- Expert: 0.7%
- Group of Experts: 0.5%

- Because human-level is a proxy, a way to talk about Bayes error
- So Human level error is the best possible outcome/error human can achieve >>> 0.5%

- A different human-level definition: a typical doctor, not group of experts >>> 1%

Focus on bias and variance first

## Surpassing human-level performance
Problems where ML better than human
- Online ads
- Product recommendation
- Logistics (predict)
- Loan approvals

All above examples from structured data, not nature perception problems and lots of data where human can't process

Other problems where human better
- Speech recognition
- Image recognition
- Medical

## Improving performance

Human-level -> Training error: avoidable error
- bigger model
- train longer/ better optimization algo (Adam)
- NN architecture/hyperparameter search (RNN/CNN)

Training error -> Dev error: variance
- Regularization
    - Dropout
    - L2
    - Data augmentation (skew, scale, rotate...)
- More training data

Flight simulator help pilot
Simulator help learn faster


