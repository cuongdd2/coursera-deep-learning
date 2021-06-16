we need to reduce the number of for loop in training to improve learning speed
vectorization: improve calculating speed without single for loop

the way deep learning try to overcome the current limitation / disadvantages by using modern hardware (GPU, parallel computing...)
and using a lot of training examples doesn't seem right to me
The way human learns is using small number of examples, but try to generalize examples, compare with what human already know about
The brain may have the assumption that what human knows is very limited in the brain. When something new comes up, the brain need to define the new thing 
new object by the existing definitions in the brain
and add a small extra new information to carry over.
The brain has very limited capacity, so it needs to decide which one is important or unique in the new object

It seems like human knowledge is a graph of information,
what algorithm make inserting, updating, searching from graph of data become efficiency 

what is the medium - abstract data is stored in human brain, especially signal data coming from visual data, audio data, 
smell, taste, touching, emotional (chemical ???), and logic reasoning / abstraction data (text / math notation) which translating from 
visual data or language translating from sounds or music notes from a song

how human categorize natural color to 7 (?) basic color or 3 (RGB) in computer
how human categorize sound to 12 notes with different pitch level (octave) from A to G, C0 to C8
440Hz 


Single specialized purpose model is not what human brain is
Human brain is multi models connected together with some common top level abstraction
For example, when we recognize dog, cat, rabbit from visual data
First at all, we recognize animal (moving object, living orgasm)
Then we focus on that single ojbect (ojbect detection here)
we extract some unique features from the object
 - eyes
 - fur
 - ears
 - mouth, fang...
 - nose
 - color
 - size



And we do a matching with our current model of existing dogs, cats, rabbit...
 - if the positive rate is below a threshold, we say it's new species (maybe mouse, fox...)
 - then we store some unique feature of the new object in the model, with some shared features from existing model

Human brain is able to build a 3D model of object, so it can construct the whole object with a partial data it can see
- like a leg of a cat
- top down view, front view...


Knowledge transfer and one-shot learning is interesting topic
Because of small number of examples, learning rate needs to be very high. As the way human learn about something.
Human need evidence to confirm its belief
"Make sense" is how human brain works, if something doesn't make sense, it's very hard to incorporate into the current model

