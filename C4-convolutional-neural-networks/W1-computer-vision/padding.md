- image size nxn
- filter size fxf, f is odd number
- output n-f+1 x n-f+1
- padding size 2p

Output image is shrinking, to prevent that, we add border pixel of 0 values

#### Valid convolutions:
- Valid: no-padding
- Same: output size same as input size: p = (f-1)/2

