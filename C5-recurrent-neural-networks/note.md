Deep learning model with very narrow, specific task may have smaller model. 
The model may not very flexible for different task but it does extreme well on a specified task
The NLP task can be think as structured or semi-structured data problem where text is represented in 
well formated, digital form (a - z....)
text or word or language is also abstract data where human need more time to learn and master
for speech recognition task, the input has more noise, more variety so the model need to more flexible 
and also more general to handle different use case. random text or text on internet is also flexible but still in
a good formated way

In computer vision, edge detection or pattern detection maybe the key to learn and regconize object
For that kind of task, I think color grouping, where we make a picture in different version where each version
only keep and range of color spectrum, say version blue, green red, white, yellow, orange of this picture

Color separated version feed into model, remove noise by downscaling and feature detection 
color separated can be implemented as 1x1 filter
input nxnx3 -> CONV 1x1x3 c-channel -> nxnxc

think about c-channel 64 -> 128 -> 1014 color
color spectrum 400nm violet to 700nm red 
300 channel -> 256 channel could be okay maximum
minimum: 16 channel