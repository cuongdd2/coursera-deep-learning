I don't think mixing up  all the RBG value is a good way to do that
we should use color value as single value, from #000000 to #FFFFFF
to reduce the value, we can quantize color value to bucket, say black, red, white, blue, green, yellow, grey, orange,
with the brightness value
maybe Y'UV is better color spectrum (Y = lumen = brightness level)
it's also good for grayscale analytics also
the shade / level of grayscale also help human brain develop a 3D sense of the world from 2D visual data

HSV: hue (color), saturation (shade), value (brightness) is a good candidate

Human eyes detect color by light electron they perceive from reflected object
- Brightness / strength of lumen on the object
- The color human eyes can perceive which reflect from object surface

https://www.sciencedirect.com/science/article/abs/pii/S1077314206001688

Li Fei-Fei has very similar approach here, with small training sets, generative visual models, incremental learning
It supports real-time learning model


What I believe is real-time, one-shot, generative learning model
classification, tagging with reinforcement learning is the future of human-level AI
low-power, small, portable, elastic neural network is the key
it's like how ARM architecture with low power dominate mobile devices market and take over x86 CPUs in datacenter or PC as well

At an average rate of 6 kcal/d per billion neurons (70), 
the average human brain, with 86 billion neurons, costs about 516 kcal/d. 
That this represents an enormous 25% of the total body energetic cost
https://en.wikipedia.org/wiki/Visual_cortex
V1 visual cortex  140 million neurons, given 6M retina visual data from eyes
V2 has spatial frequency, size, color, and shape
Object Recognition Memory as well as the conversion of short-term object memories into long-term memories
V3: coherent motion of large patterns covering extensive portions of the visual field
V4: simple geometric shapes
V5: speed and direction of moving visual stimuli
