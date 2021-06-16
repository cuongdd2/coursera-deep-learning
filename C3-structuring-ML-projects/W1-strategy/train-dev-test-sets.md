## Ideas to try and improve
- Collect more data
- Collect more diverse training set
- Traing algorithm longer with gradient descent
- Try Adam instead of gradient descent
- Try bigger network
- Try smaller network
- Try dropout
- Add L2 regularization
- Network architecture
    - Activation functions
    - num of hidden units...
    
## Orthogonalization
- Isolation tuning options
- Each knob/tuning option has a specific effect

## 4 important assumptions
- fit training set well on cost function
    - bigger network
    - Adam
    
- fit dev sest
    - regularization
    - bigger training set
- fit test set
    - bigger dev set
- performs well in real world
    - change dev set or cost function
    
Be careful with "Early stopping"

## Single number evaluation metric
Set it when start problem
A single number to improve is easier to focus

Precision accuracy (P): % of positive successful
Recall accuracy (R): % of actual successful (positive and negative)
F1 score = 2 / (1/P + 1/R) : Harmonic mean : avg of Precision and Recall
Or average value of multiple results (different geographic)

## Satisficing and Optimizing Metric
Optimizing: to maximize
Satisficing: to meet threshold

N metrics: 1 optimizing, N-1 satisficing

## Train/Dev/Test Sets Distributions
Dev and Test sets should be from same distribution
If there are multiple regions, shuffle data

Dev/Test set should relfect data expected in the future, important ...

Test set big enough to give high confidence

Big enough dev set (no overfitting), may not have test set

## Change Dev/Test sets and Metrics
Error rate = 1 / m sum(y-pred != y)

Adding weight w to prevent some un-prefer use cases

W = 1: non-cat
W = 10: porn image

1/sum(W) * sum ( W * (y-pred ~= y)) 

Stop coding when prefer option not showing, change metrics


2 steps:
 - how to define a metric to evaluate classifier (set target)
 - how to do well on this metric (how to shoot the target)

