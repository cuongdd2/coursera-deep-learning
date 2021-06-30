### Object localization
- Step 1: classification = multi-classes : softmax
- Step 2: classification with localization  
- Find where is the object in the image
- Detect multiple objects in a image

Class label + bounding box
Return bx, by, bh, bw => bounding box of the object
- translate to (bx, by) middle point and height, width of the object

y = [p-c bx by bh bw c1 c2 c3 c4]
p-c: probability of object existing
c1 - c4: classes

if object detected:
[1 bx by bh bw 0 1 0]
if no object:
[0 ? ? ? ? ? ? ? ?]
? means "don't care"

Cost function
L(y^, y) = (y1^ - y1)**2 + (y2^ - y2)**2 + ... + (y8^ - y8)**2 if y1 == 1
(y1^ - y1)**2 if y1 == 0

logistic for 1/0 there is object or not
square error for bounding box
softmax for classes

### Landmark detection

landmark coordinator: lx, ly
for multi points: l1-x, l1-y, l2-x, l2-y
landmarks can be used as points around objects
labels of landmarks need to be consistent

### Object detection
Crop cars from images
Crop closely to the car parts
Use images as input of the ConvNet -> label 0/1 car or not

#### Sliding windows detection
- Use a small window, run over the image
- Use stride to run window 
- Sliding window size can be small to large
- Computation cost is very high

#### Convolutional implementation of sliding windows
Published 2014 OverFeat: Sermanet
`
14x14x3 -> CONV 5x5 -> 10x10x16 -> POOL 2x2 -> 5x5x16 -> FC 5x5 -> 1x1x400 -> FC 1x1 -> 1x1x400 -> FC 1x1 -> 1x1x4

28x28x3 -> CONV 5x5 -> 24x24x16 -> POOL 2x2 -> 12x12x16 -> FC 5x5 -> 8x8x400 -> FC 1x1 -> 8x8x400 -> FC 1x1 -> 8x8x4
`
- 8x8 -> number of windows to be slided
- 4: number of classes to be classified

Accuracy is not too good because of stride 5x5

### YOLO algorithm
Published Redmon 2015 You Only Look Once: Unified real-time object detection

Translate image 200x200x3 to a 3x3x8 9-cells grid of image
to avoid multiple objects in same grid cell -> 3x3 -> 19x19 grid
we only care about the center point of object

Values of bx, by, bw, bh are translated to 0 ... 1
top left (0, 0), right bottom (1, 1)
width, height are fractions of a cell square 1
bw, bh maybe > 1

### Intersection over union
- to evaluate object detection accuracy
- by calculating intersection between bounding box of object and the predicted one
- IoU  >= 0.5, it's okay
- IoU = size of joint area / size of union area

###  Non-max supperession
- to make sure algorithm detects each object once
- Pc = 0.6 or 0.7 or 0.9 -> choose the highest one and remove the smaller one which intersect with the high probability
- we discard/suppress all boxes with Pc <= 0.6
- pick the box with highest Pc
- output that as a prediction
- discard any remaining box with IoU >= with the output box

### Anchor boxes
- to detect multiple objects in a box (grid cell)
- anchor box is reference box to the ground truth
- anchor box is w > h box: car or w < h box: pedestrian  
- use highest IoU with anchor boxes, store in y 3x3x8 -> 3x3x16 in case of 2 objects
- use K-mean algorithm to choose the box for a category

### YOLO  algorithm
- y usually 3x3x2x8 or even 19x19x5x8 (19x19 cells in an image)
- run non-max suppression for each class

### Region proposals
- R-CNN Region with Convolutional Neural Network
- select few windows
- use segmentation algorithm
- Segmentation algorithm is slow  
- Fast R-CNN: use convolution implementation of sliding windows to classify to all proposed regions
- Faster R-CNN: use NN to find the regions

### Semantic Segmentation with U-Net
- to draw a boundary line around the object
- per-pixel class label
- Input 200x200x3 -> CONV -> POOL -> 16x16x128 -> T-CONV -> 200x200x[1...5] class  
- Transpose Convolution to scale out layer from small W-H, big channels to big W-H and small channels 

### Transpose Convolution
- opposite to Normal convolution
- 2x2 -> Trans Conv 3x3 -> 4x4
- Mapping 1 * 3x3 -> 3x3 on output, filter 3x3, padding = 1, stride s = 2
- In normal convolution, mapping 3x3 * 3x3 -> 1 cell on output

### U-Net architecture
- 2015 Ronnerberger : Convolutional Networks for Biomedical Image Segmentation
- we can skip from input to output to keep details from input image to output  layer
- Trans Conv + Skip Connection => new layer with same channels from prev steps
- last step CONV(1x1)

Ideas about U-like app, make-up touch-up 
