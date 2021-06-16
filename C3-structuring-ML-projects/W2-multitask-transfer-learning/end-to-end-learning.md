Audio -> MFCC -> features -> ML -> phonemes -> words -> transcript
Audio -> transcript

Traditional pipeline works with small amount of data
End-to-End training need a lot more data
We can have a hybrid pipeline

### Face recognition
- Image to face
- Crop face
- Face to identity

### Machine translation
Works well with end-to-end

### Child's age estimating 
X-ray image -> bones -> age

## Pros
- Let the data speak
- Less hand-designing of components needed

## Cons
- May need large amount of data
- Excludes potentially useful hand-designed components

Key questions: do you have sufficient data to learn a function of the complexity needed to map X -> Y
Motion planning: Cars, pedestrian -> route
