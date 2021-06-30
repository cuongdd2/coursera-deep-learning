# Convolution

Convolution = combination = summation  of matrix * matrix (filter)

1000x1000 pixels image create very big parameter networks



## Edge detection

### Vertical edge detection
- Filter 3x3 matrix name filter, kernel
|   1   0   -1  |  
|   1   0   -1  |
|   1   0   -1  |  

Horizontal filter
|   1       1       1  |  
|   0       0       0  |
|   -1      -1      -1 |

Moving filter matrix by 1 pixel left to right, top to down

Python: conv_forward
tensorflow: tf.nn.conv2d

Sobel filter
1 0 -1
2 0 -2
1 0 -1

Schass filter
3 0 -3
10 0 -10
3 0 -3

We can learn the filter matrix also