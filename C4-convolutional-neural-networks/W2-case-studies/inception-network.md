### CONV 1x1
Published 2013

CONV 1x1xnC (channel) -> ReLU -> single value

group values in all channels

plus with # filters

To shrink channels
28x28x192 -> [CONV 1x1 32] -> 28x28x32

### Inception network
Published 2014
```
Using 1x1 3x3 5x5 MAX-POOL 3x3 same s=1
=>> 28x28x192 -> 28x28x256
```
Cons: computational cost is huge, 120M operations

`28x28x192 -> CONV 1x1x192 16 -> 28x28x16 -> CONV 5x5x16 32 -> 28x28x32`

The CONV 1x1 calls bottleneck layer
- No performance hurting
- Save computational cost
```
        -------------> CONV 1x1   || 
Input   -> CONV 1x1 -> CONV 3x3   || ===> Concat all
        -> CONV 1x1 -> CONV 5x5   ||
        -> POOL 3x3 -> CONV 1x1   ||
```
### There is a softmax layer at each block of Inception ===> validate the output not overfitting