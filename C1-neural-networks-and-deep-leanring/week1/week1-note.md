What is a Neural Network?
- ReLU = rectified linear unit (sigmoid) f(x) = max(0, x)
- Input (x) & Output (y) and hidden layers (unit) are neural network
- Given enough data x and y, neural network can creat mapping function with good accuracy
- Activation function: sigmoid ore ReLU
- Sidmoid is very slow vs ReLU for convergent, gradient descent / slope

Supervised Learning
- Input x and Output y are specified
- Structure data
    - Well defined data
- Unstructured data
    - data with noise
    - raw data (audio, image, text)
- standard NN
    - Real Estate, Online Advertising use
    - prediction, forcasting, pattern recoginition from the data
    - Input is features, category, grouped data
- Convolutional NN
    - Photo tagging use
    - Input is 2-dimentional data (photo, matrix data)
    - Reduce, select subset of data from the input
- Recurrent NN
    - Speech + Machine translation use
    - (sequence data, timeseries) Audio -> temporal sequence
    - 1 dimensional data, mapping 1 on 1
- Autonomous driving : custom, hybird NN

Why Deep Learning
- Traditional learning algo (SUM< logarit, regression): plateau after a threshold
- More data from everywhere : internet, IoT, mobile...
- Scale (size of NN and size of data) improve deep learning progress
- Amount data = labelled data M
- For small training sets, NN may not take advantage

How we develop a Neural Network
- Idea -> Code -> Experiment
- Algorithms + Computation + Data
