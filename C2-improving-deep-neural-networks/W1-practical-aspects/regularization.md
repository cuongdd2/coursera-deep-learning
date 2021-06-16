## Regularization
### Regularization -->> to fix over-fitting
J(w,b) = 1/m SUM L(y^, y) + lambda/2m || w|| 2/2
L2 regularization
        2
|| W ||    = sum (j = 1 -> nx) (w(j)^2)   = wT.w
        2

L1 regularization
lambda / 2m || w ||   -> w will be sparse (lot of 0 in matrix -> easy to compress)

Frobenius norm

sum i = 1 -> n[l]
    sum j = 1 -> n[l-1]
        (W[ij]) ^ 2

dW[l] = (back-propagation) + lambda / m W[l]

W[l] = W[l] - learning_rate * dW[l]

Weight decay: 1 - learning_rate * lambda / m 

when lambda is large -> dW[l] large -> W[l] := W[l] - dW[l] is small to 0
so Z = W[l]A[l-1] + b[l]
is linear function

debug by loss function

## Dropout regularization
Only drop out in training set, not test set
Set probability to dropout nodes in layer
P = 0.8

d3 = np.random.rand(a3.shape[0], a3.shape[1]) < p

a3 = a3 * d3
a3 /= p ===>>> keep final value the same

previous layer #neuron = column
current layer #neuron = row

computer vision
 - frequent drop out
 - there's a lot of input data
 - 

## Other regularization methods
For images:
 - flip, rotate, skew images, crop, zooming, distortion... to add more training data
Early stopping:
 - loss function for both training and dev set  

## Normalizing inputs
- subtruct means x := x - mean of input (sum / m)
- normalize variance: 
 - sigma = 1 / m sum (x ^ 2)
 - x /= sigma

Do the same way normalizing in training set, dev set, test set
Why do we need to normalize input -> training rate is much faster
espicially when input scale is very different: 1 -> 1000, 0 -> 1....



Vanishing or Exploding gradients
- sometimes slopes become very small or very large -> training very difficult
- for example, deep, many level layers

## Weight initialization
W = random.rand()
ReLU : sqrt(2 / n[l-1])
tanh: sqrt(1 / n[l-1])

## Numerical approximation
2 side of derivative (+ or -) for gradient checking

