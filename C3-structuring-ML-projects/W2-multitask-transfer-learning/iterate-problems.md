## Build quickly then iterate
- set up dev/test sets, metric target
- build system quickly
- use bias/variance analysis & error analysis to prioritize next steps

## Deep learning need a lot of data
- Hunger for data
- Distribution in training and testing are different
- 100k of unrelated data, 10k of related data => 105k to training set, 2.5k/2.5k of related data to dev and test

## Bias and Variance with mismatched data distributions
when training error is 1%, dev error is 10% but not sure it's Variance or Distribution issue
- create training-dev set (same distribution as training set, but not trained)
- test on training-dev set, if it's 9% => Variance issue, overfitting
- if it's 1.5%, it's Distribution issue between Dev and Train sets

What we need to focus on
- Human-level error
- Training set error
- Training-dev set error
- Dev error
    - Different between dev and training-dev is data mismatched
    
## Addressing Data mismatch
- Carry out manual error analysis between training and dev set
- If data has noise, we can create Artificial data synthesis (clean data + noise => real data)
- Be careful with overfitting to synthesized data



