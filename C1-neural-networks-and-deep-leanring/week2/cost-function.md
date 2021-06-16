Cost function
 - loss function / error function is applied for single training example 
 - cost function is average loss function of entire training set
 - ground truth value y(i) : the actual value
 - i-th: training example number i
 - z-i = w(t)x-i + b: value z at i-th equals w transpose x at i-th plus b 
- loss function L(y^, y) = 1/2 (y^ - y) ^ 2
- another possible loss function:  -(y log y^ + (1 -y)log(1 - y^)) ==> good for gradient descent to find global optimal point
- Cost function: J(w, b) = 1/m SUM(L(y^, y))
