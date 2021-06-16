### learning rate : most importance to tune, ranging from 0.1 to 0.001
momentum = 0.9
Adam b1 = 0.9, b2 = 0.999, epsilon 10^-8
## #layers
## #hidden units 
learning rate decay
min-batch size: 64, 128, 256 at max 1024


Use Random sampling, not grid of values

Use Coarse to fine => when find a range, use fine details later


## Picking hyperparameters at random

number of nodes: 50 - 100
number of layers: L 2 - 4
We can chose equal distributed random samples -> linear search scale

For learning_rate alpha, log scale search is better
alpha range: 10^-4 to 10^-1

For exponentially weighted averages
beta = 0.9 .... 0.999
1 - beta = 0.1 ... 0.001
beta = 1 - 10^-r

## In practice
Pandas vs Caviar
Knowledge may not transfer between domain
Intuitions do get stale
re-evaluate occasionally

Babysitting when computing power is not enough
Training in parallel when computation poweris enough
