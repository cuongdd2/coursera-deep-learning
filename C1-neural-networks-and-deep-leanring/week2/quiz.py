import numpy as np
import math

a = np.random.randn(3, 3, 2)
b = np.random.randn(3, 2)
# c = a.T + b
c = a * b

v = a.reshape(-1, 1)
print(v.shape)
b_norm = np.linalg.norm(b, 2, 1, True)
print(b_norm)
np.sum(b, axis=1, keepdims=True)
print(b[0].size)
np.zeros()

def sigmoid(z):
    s = 1 / (1 + np.exp(-z))
    return s

def propagate(w, b, X, Y):
    m = X.shape[1]
    A = sigmoid(np.dot(w.T, b) + b)
    cost = -1/m*np.sum(Y*np.log(A) + (1 - Y)*np.log(1 - A))
    dw = 1 / m * X * (A - Y).T
    db = 1 / m * np.sum(A - Y)
