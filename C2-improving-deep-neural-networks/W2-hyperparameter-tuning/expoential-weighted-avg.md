v-t = beta * v-(t-1) + (1 - beta) * theta-t

beta: moving avg window
v-(t-1): previous value
theta-t: current value

beta = 0.5 -> window 2
beta = 0.9 -> window 10

approx = 1 / (1 - beta)

## Bias correction

because V0 = 0 not a correct number
maybe V0 = theta is better
