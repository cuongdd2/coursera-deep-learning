- We usually move the filter matrix by 1 pixel each time
- We can move filter by 2 pixels each time also

stride step = s = 2

new output size = floor((n + 2p - f)/s + 1)

- in technical, it calls cross-correlation
- convolution needs flipping (vertically and horizontally) filter matrix
- in ML, no flipping in convolution

###  Convolutions over volume
- image 6x6x3
- filter 3x3x3
- output: 4x4x1
- number of filters: f = 2
- => output: 4x4x2
- channel of images: 3, calls depth

### Neural network layers
f = filter size
p = padding
s = stride
input = n-h (height) x n-w (width) x n-c (channel/depth)

output m = floor((n + 2p - f)/s + 1) 
output of layer l-1 is input of layer l

n-c = number of filters
