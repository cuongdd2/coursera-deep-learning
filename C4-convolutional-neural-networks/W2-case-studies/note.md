It seems like CONV filter size is converge to 3x3
However we can think about varying filter size 1x1, 3x3, 5x5 or 7x7 depends on
the input size (resolution)
Think about how human see a picture, we need to zoom in and zoom out to see pattern in picture
pattern can be large or small

by conv and max-pool, we identify edge, pattern and group them together, let them fit in smaller matrix


How to zoom-in, zoom-out:
- can same filter size give that effect?