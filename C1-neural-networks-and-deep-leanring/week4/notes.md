L = number of layers
n[l] number of nodes in layer l
X = a[0]
Y^ = a[L]

Z[l] = W[l].A[l-1] + b[l]

A[l-1] = (n[l-1], 1)  with m training examples => (n[l-1], m)
W[l] := (n[l], n[l-1]) == dW[l]
b[l] := (n[l], 1) == db[l]

broadcasting help make b[l] (n, 1) -> (n, m)

Deep networks
- output of previous layer is input of next layer
  - in case of face recognition
- first layer can detect some edges
- second layer can form face part (node, eyes, ears...)
- next layer form part of face

baseline:
- logistic regression
- 1 hidden layer
- hypertuning



##Backward propagation
- input: da[l]
- output: da[l-1], dW[l], db[l]
- z[l] = W[l].a[l-1] + b[l] => dW[l] = a[l] / a[l-1]
- a[l] = g[l] (z[l])
- da[l] = a - y  
- dz[l] = da[l] / dg[l] = da[l] * g'
- dw[l] = dz[l] / a[l-1] = dz[l] . a[l-1].T ===>>>> dW[l] =>> 1 / m * ....
- db[l] = dz[l]   =>>>> 1/m * np.sum()
- da[l-1] = dz[l] / w[l]


Parameters: W, b
Hyperparameters: learning rate, iterations, #hidden layer, #hidden unit, choice of activation function

momentum, minibatch size, regulations