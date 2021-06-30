## Learning objective
- Describe a basic sequence-to-sequence model
- compare and contrast several algo for language translation
- optimize beam serach and analyze it for errors
- use beam serach to identitfy likely translations
- apply BLEU score to machine translated text
-  implemebnt an attention model
- train a trigger word detection model and make predictions
- synthesize and process audio recording to create train/dev datasets
- structure a speech recognition project

## Basic models
- Sequence to sequence
- Machine learning, speech recognition
- encoder -> decoder, input each word a time, output each word a time
### Image captioning
- image -> AlexNet -> 4096D features
- use 4096D features as input, train on RNN to output each word a time
## Picking the most likely sentence
- A language model: predict Probability of a sequence
- x1 -> y1 -> y2 -> y3...
- Machine translation: x1 -> + x2 -> + xT -> y1 -> y2 -> yT
- conditional language model: P(y1, ...yT | x1,...,xT)
- find a sentence y to maximize P given input sentence x
- greedy search not giving an optimal result
- use proximate search algo, else we need to search 10k^n-word
## Beam search
- at softmax output, keep top 3
- next step, feed each of top 3 word to next layer and so on
- at each step, keep only top 3 options
- keep 3 copies of network  
- `# of possible words: 3^n where n= len(sentence)`
- P(y1,y2|x) = P(y1|x)*P(y2|x,y1)
## Beam search refinements
- Length normalization: instead of P(y) < 10^-3, use log(P(y))
- dividing by Ty to avoid penalty to longer sentence
- heuristic way,  1/ Ty^alpha where alpha = 0.7 (0..1) is better 
- beam width B: min 3, normal 10, max 100
- beam search not ganruantee for exact max result
## Error analysis on Beam search
- y*: expected result
- P(y*|x) > P(y^|x) -> beam search fails
- P(y*|x) <= P(y^|x) -> RNN at fault
- go through dev set
## BLEU score
- there are multiple right answers
- Bilingual Evaluation Understudy
- Given reference output1, output2
- check frequent and location of output MT
- clip: 2 words at once
## Attention model
- long sentence doesn't work well with Sequence model
- use nearby, surround words only by Bidirectional RNN
- sum(alpha-<1,t'>, t'), alpha is trained 
- taking quadratic cost Tx.Ty
## Speech recognition
- audio (air pressure over time) -> transcript
- pre-proccess audio -> spectrogram / false back output
- used to using phonemes 
- input usually 300h to 3000 hours of audio
- CTC (connectionist temporal classification): cost for speech recognition
- collapse repeated character not separated by blank" ttt_h_eee____ ____qqqq___ -> the q
- 100hz 10s audio -> 1k points -> reduce to few data point by CTC
## Trigger word detection
- right after the trigger word says, set output label to 1, few more latter is okay