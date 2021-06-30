### Motivation
Published 2017 Howard
- Low computational cost at deployment
- Useful for mobile / embedded vision applications
- Key idea: Normal vs depthwise-separable convolutions


6x6x3 -> CONV 3x3x3 5 -> 4x4x5
total: 2340 operations

#### MobileNetv1

6x6x3 -> CONV 3x3x3 -> 4x4x1 -> CONV 1x1x3 5 -> 4x4x5
           Depthwise      ->     Projection (Pointwise)

total: 432 + 240 = 672 steps

saving: 1/(n-c') + 1/(f^2) = 1/(32...512) + 1/9 = 0.111...

#### MobileNet v2
Publish 2019 Sandler: adding Expansion layer to make learning more but using less memory by projection down layer

nxnx3 -> CONV 1x1x3 18 -> nxnx18 -> CONV 3x3x3 same -> nxnx18 -> CONV 1x1x3 5 -> nxnx4

### EfficientNet
Published 2019 Le & Tan
R: Input resolution
D: Depth of network
W: output width

prototext: file format for Neural Network config

