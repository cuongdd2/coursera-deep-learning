## Mini-batch gradient descent
m = 5000000 training set
break into batch of 1000 each

When input is too big

epoch ???

mini-batch leads to up and down of cost function, not smooth

min-batch size ???

m <= 2000: use batch training set

typical mini-batch size: 64, 128, 256, 512, at max 1024
power of 2 is better
make sure mini-batch fit in CPU/GPU memory


Stochastic Gradient Descent = SGD
 - when we calculate forward_propagation, cost_function, back_propagation for every single training example

Batch Gradient Descent
 - We put all input (training data and labels) into giant vector and calculate all of them together


We loop
 - iterations
 - training examples
 - layers of network
