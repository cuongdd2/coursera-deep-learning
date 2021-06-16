mean = 1 / m sum(z)

variance^2 = 1/m sum (z - mean)^2

z-norm = (z - mean) / (sqrt(variance^2) + epsilon)

z-tilde = gamma * z-norm + beta

Batch norm to a network

X -> Z
Z~ = Z / Batch_Norm
A = g(Z~)

gradient descent === derivative dW, db

In Tensorflow => tf.nn.batch_normalization

Z-norm => 1/m *sum(Z)

Z~ = gamma * Z-norm + beta

With beta param, we don't need bias value anymore
shape of gamma, beta = (n[l], 1)

for t = 1 ... # mini-batch
    compute forward prop on Xt
        each hidden layer, use BN to Z[l] to Z~[l]
    use back prop to compute dW, d-beta, d-gamma
    update parameters

covariate shift
X -> Y
X distribution changes/shift

small mini-batch: 64 has slight regularization effect
512 batch size will cancel it out

keeping micro, sigma-squared to use later at test time


