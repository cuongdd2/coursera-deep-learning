Root mean square prop

Sdw = beta *  Sdw * (1 - beta) dW^2 (multiply-element-wise)
Sdb = beta * Sdb + (1 - beta) db^2

W := W - learning_rate * dW / sqrt(Sdw)
b := b - learning_rate * db / sqrt(Sdb)


#Adam optimization

Momentum b1     Vdw = b1 * vdw + (1 - b1)dW         vdb = b1*Vdb + (1 - b1) db
RMSProp  b2     Sdw = b2 * Sdw + (1 - b2)dW**2      Sdb = b2*Sdb + (1 - b2) db**2

V-dw = V-dw / (1 - b1-t)

S-dw = S-dw / (1 - b2-t)

W := W - alpha V-dw / (sqrt(Sdw) + epsilon)
b := b - alhpa V-db / (sqrt(Sdb) + epsilon)


b1 0.9      dw
b2 0.999    dw**2
epsilon  10^-8

## Learning rate decay

1 epoch = 1 pass through data

alpha = 1 / (1 + decay-rate * epoch-num) * alpha-0
alpha-0 = 0.2 initial learning rate
decay-rate = 1

alpha = 0.95 ^ epoch-num * alpha-0
alpha = k /  sqrt(epoch-num)
alpha = alpha / 2

## Local Optima
Saddle point is local

Plateaus is the problem where gradient descent is 0
Plateaus can make learning slow

