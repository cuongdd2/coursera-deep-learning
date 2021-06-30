The details of this ResNet-50 model are:

Zero-padding pads the input with a pad of (3,3)
Stage 1:
The 2D Convolution has 64 filters of shape (7,7) and uses a stride of (2,2).
BatchNorm is applied to the 'channels' axis of the input.
MaxPooling uses a (3,3) window and a (2,2) stride.
Stage 2:
The convolutional block uses three sets of filters of size [64,64,256], "f" is 3, and "s" is 1.
The 2 identity blocks use three sets of filters of size [64,64,256], and "f" is 3.
Stage 3:
The convolutional block uses three sets of filters of size [128,128,512], "f" is 3 and "s" is 2.
The 3 identity blocks use three sets of filters of size [128,128,512] and "f" is 3.
Stage 4:
The convolutional block uses three sets of filters of size [256, 256, 1024], "f" is 3 and "s" is 2.
The 5 identity blocks use three sets of filters of size [256, 256, 1024] and "f" is 3.
Stage 5:
The convolutional block uses three sets of filters of size [512, 512, 2048], "f" is 3 and "s" is 2.
The 2 identity blocks use three sets of filters of size [512, 512, 2048] and "f" is 3.
The 2D Average Pooling uses a window of shape (2,2).
The 'flatten' layer doesn't have any hyperparameters.
The Fully Connected (Dense) layer reduces its input to the number of classes using a softmax activation.


identity_block(X, f, filters, training=True, initializer=random_uniform):
convolutional_block(X, f, filters, s = 2, training=True, initializer=glorot_uniform):