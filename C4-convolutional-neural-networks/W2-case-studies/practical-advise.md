### Transfer learning

Start by using open source pre-trained

- Download weights + code for other project (ImageNet)
- replace Softmax layer by ourself
- freeze : trainable_parameters = 0 / freeze = 1: don't train earlier layers
- pre-computed activations values from layers before softmax -> save to disk
- If there are more data, we can train few more layers before softmax
- If you have a lot, a lot of data, use pre-trained weights as initialization values
- In computer vision, pre-trained models are very popular, use them can make sense

### Data augmentation
Dimensions Transformation
- mirroring
- random cropping
- rotation
- shearing (skew)
- local warping
  
Color Transformation
- color shifting (change R: +20, G: -20, B: +20)... because of sunlight effect
- PCA (Principal component analysis)

Implementing distortions during training

Harddisk    -->     CPU thread      -->     CPU/GPU training

raw images  -->     load/distortions    --> train

### State of Computer Vision
```
Little data <----------------------------------------------------> Lots of data
                object detection
                            image recognition
                                            speech recognition
more hand-engineering                                              simpler algorithms/less hand-engineering            
```

Sources of knowledge
- labeled data
- hand engineered features / network architectures / other components

Benchmarks and competitions tips
Ensembling
- train several networks independently and average their outputs Y^
- 3 to 15 networks
Multi-crop at test time
- run classifier on multiple versions of test images and average results
- 10 crop (center, 4 corners, mirror-center, mirror 4 corners)

Use open source code
- user architecture of networks published
- use open source implementations if possible
- use pre-trained models and fine-tune on your dataset