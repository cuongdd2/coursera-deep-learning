## Multi-task learning
For example, 4 labels in same images (car, stop sign, traffic light, pedestrian...)
Loss function = 1/m sum(i = 1 ... m) sum(j=1..4) L(y-i, y)

We can train 4 NNs or 1 NN with 4 output labels
- If they share same low-level features
- Amount data of each task is similar
- NN needs to big enough to do well on all task

If the image missing some labels, it's fine to train

#### Computer vision / object detection is good case to applied multi-task learning