### LeNet-5
Published: 1998
When training
- nH, nW smaller
- nC bigger (more features detected)

### AlexNet
Published 2012
60M parameters
CONV 11x11 s=4
### VGG-16
- CONV = 3x3 s = 1, same
- MAX-POOL = 2x2, s=2

224x224x3 -> [CONV 64] x 2 -> 224x224x64 -> [MAX-POOL] -> 112x112x64 -> [CONV 128] x 2 -> 112 x 112 x 128
-> POOL -> 56x56x128 -> [CONV 256] x3 -> 56x56x128 -> POOL -> 28x28x256 -> [CONV 512] x 3 
-> POOL -> 14x14x512 .... -> 7x7x512 -> FC [4096] -> FC [4096] -> Softmax [1000]

### ResNet Residual Networks
Published He 2015

Short cut layer 1 to layer 3
a[l+2] = g(z[l+2]) : normal way
a[l+2] = g(z[l+2] + a[l])

Plain network (multi layer straight way): training error increases
ResNets help deeper layer networks perform well 

a[l+2] ~~ a[l] when w[l+2] and b[l+2] closes to 0
----> identity function

CONV 3x3 POOL 2




