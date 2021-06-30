### Neural Style Transfer
- C: content image
- S: style image
- G: generated image

### What are deep ConvNets learning?
Published: 2013 Zeiler and Fergus Visualizing and understanding Conv nets
- Find 9 image patches/portions that has max unit's activation values
- Mapping between activation values and what it's really looking into

From observations, layer 1 usually has features of small edges with colors
In deeper layer, the activation will learn larger patches of the images

Layer 2 has more complex features, edges, patterns

The shallow layers detect edges, simple patterns
The deeper layers detect more complicated patterns

### Cost function
J(G) = alpha * J-content(C, G) + beta* J-style(S, G)
alpha, beta can become alpha and (1 - alpha)

How to generated G
1. initiate G randomly: G = 100x100x3
2. Use gradient descent to minimize J(G)
3. G = G - derivative-J(G)

### Content cost function
- Use hidden layer l to compute content cost
- not too shallow, not to deep
- Use pre-trained ConvNet (Eg. VGG network)

### Style cost function
Published 2015 Gatys
- define style as correlation between activations across channels
- how correlated are the activations across different channels

Style matrix:
- G[l] is nC x nC at layer l
- a-jkl is activation at (i,j,k) (H,W,C) of layer l
- G-kk' is correlation between channel k and k'
- G-kk' = sum(nH)(nW)a-ijk * a-ijk'
- calculate the same thing for style image and generated image
- name "gram matrix"
- J-style(S,G) = || G-style - G-gen || ^2
- we can calculate multiple layers as well

