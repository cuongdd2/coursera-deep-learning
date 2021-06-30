
### One shot learning
- given just one single image of person
- learn from one example to recognize the person again
#### Learning a "similarity" function
- d(img1, img2) = degree of difference between images
- if d(img1, img2) <= T -> same person
#### Siamese network
Published 2014 Taigman DeepFace
- input: x1
- output: f(x1) of 128 nodes in the last layer
- encoding x1 -> f(x1)
- d(x1, x2) = || f(x1) - f(x2) || 2//2
### Triplet loss function
Published 2015 Schroff FaceNet
- A: anchor
- P: positive
- N: Negative

`We want || f(A) - f(P) || ^2 + alpha (margin) <= || f(A) - f(N) || ^2`

Loss function:
- given 3 images A, P, N

L(A,P,N) = max(||f(A)-f(P)||^2 - ||f(A)-f(N)||^2 + margin, 0)

J = sum(L(A,P,N))
training set: 10k pictures of 1k persons

We shouldn't choose random tuple(A,P,N) but making it hard to learn N closes to A

We can use pre-trained network with already learned features to teach new face

### Face verification and binary classification
DeepFace 2014 Taigman
calculate f(xi) and f(xj) => predict if xi and xj from same person

y^ = sigma (sum 1..128(w*|f(x-i) - f(x-j)| + b))

