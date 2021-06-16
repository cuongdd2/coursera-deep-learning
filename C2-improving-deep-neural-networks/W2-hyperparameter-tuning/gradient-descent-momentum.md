Because in the beginning, too big learning_rate will make gradient descent moving up and down too much
but when dw is too small, learning_rate can be larger

W = W - learning_rate * dW

V-dW = beta * V-dW + (1-beta) * dW
V-db = beta * v-db + (1 - beta) * db
W = W - learning_rate * V-dW
b = b - learning_rate * V-db

beta = 0.9 is good enough


why we don't increase  learning_rate overtime
