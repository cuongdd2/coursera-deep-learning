import numpy as np
import tensorflow as tf
import tensorflow.keras.layers as tfl

a = np.random.randn(3, 3)
a2 = np.zeros((3,3))
print(a)
b = a2.sum() + float(2)
a2.mean()
print(b)
tf.keras.losses.BinaryCrossentropy(from_logits=True)
tf.keras.metrics.Accuracy()
tf.keras.optimizers.Adam()
base_model = tf.keras.applications.MobileNetV2(input_shape=(64,64,3),
                                               include_top=False, # <== Important!!!!
                                               weights='imagenet') # From imageNet
print(base_model.input_shape)

