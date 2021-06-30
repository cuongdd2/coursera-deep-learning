### Layers

- Convolution layer (CONV)
- Pooling layer (POOL)
- Fully connected (FC)

### Pooling
Matrix 4x4 -> 2x2
- Max pooling: each 2x2 square, get the max value
- f= 2 (filter size)
- s = 2 (stride)
- operation = max (min/avg/count/sum)
- ####parameters: 0, no learning, no weights
- padding = 0 , always
Max pooling is much more popular than avg pooling

Avg is used for reduce dimensions

Conv layer + pool layer = layer 1


Input -> Conv-1 -> Maxpool-1 -> Conv-2 -> maxpool-2 -> FC-3 -> FC-4 -> softmax(0..9)

Matrix sizes reduce, channels increase when training
 
## Why convolutions work
- Parameter sharing: feature detector (edge, color...) is useful in all part of the image
- Sparsity of connections: output is related to a part of input
- Translation invariance: pixels shifted work well