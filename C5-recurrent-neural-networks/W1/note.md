### Use cases
- Speech recognition: audio -> text
- Music generation: nothing -> music notes sequences
- Sentiment classification: review text -> rating (1 - 5)
- DNA sequence analysis: ACGCCGTCT -> detect sequence
- Machine translation: Language X -> Language Y
- Video activity recognition: sequence of images -> activities
- Name entity recognition: Text -> name

### Notation
- input: x, output y
- length of input T(x) output T(y)
- `<t> is element of input at index t of length T`
- Vocabulary: words use in input / output : dictionary
- Dictionary size: 30k -> 50k, up to 100k
- x<t> is one-hot index in array of all 0 values, <UNK> = unknown word

### Problems
- input and output has different lengths
- doesn't share features learned across different positions of text

### Recurrent NN
- same activations shared between all input words
- we feed each input word to NN and get a corresponding output word
- The input words won't be used in previous word
- a<0> = 0, a<1> = g(w-aa a<0> + w-ax x<1> + b-a): tanh/relu
- y^ = g(w-ya a<1> + b-y): sigmoid
- Waa | Wax can be stacked together to Wa matrix
- a<t> = g(Wa [a<t-1>, x<t>] + ba)
- [a<t-1>, x<t>] = stacking vertical 

### Backpropagation
- Backprop through time
- L(y^, y) = sum (L (y^, y))

### Different X, Y size
- many -> 1: mapping Y to last X<t>
- 1 -> many: use Y<t-1> as input for Y<t> with Activations
- many -> many, # length: 2 phases encoder and decoder, X from 1 to t, 
  then feed A<t> to calculate Y<1> then A<t+1> to A<t+t'> to calculate Y<t>
  
### Language Model and Sequence Generation
What is language modelling?
- Speech recognition
- audio -> text, P(text) = 10^-10

### Language modelling
- Training set: large corpus of English text, a lot of words
1. step tokenize
- map word to dictionary (vocabulary) to get index
- may append end of sentence token <EOS>
- for word not exist in vocabulary, replace by <UNK> word -> may not translate
- y^ = softmax of (P(word1)P(word2)...P(wordn)) chance of being word in vocabulary
- y^-2 = P(current-word | prev-word)
- P(w1, w2, w3) = P(w1) P(w2 | w1) P(w3 | w1)

### Sampling Novel Sequence
- vocabulary: word level language model
- character level language model -> more computation power

### Vanishing Gradients with RNNs
- Early words have very little effect to last words output
- Exploding  gradients -> gradient clipping (NaN)
