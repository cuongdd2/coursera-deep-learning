
## Gradient Checking
|| d-theta-aprrox - d-theta || 2
------------------------------
|| d-theta-aprrox || 2 + || d-theta || 2

10^-7 is great, 10^-3 : something wrong. 10^-5 maybe okay

gradient checking is for debug only
if grad check is fail, look at components to identify bug
remember if using regularization
## doesn't work with dropout
run random initialization again to check