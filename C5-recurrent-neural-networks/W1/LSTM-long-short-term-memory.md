### Long short term memory
- Published 1997 Hochreiter & Schmidhuber
- C~<t> = tanh(Wc[a<t-1>, x<t>] + bc)
- gamma-u (update) = sigmoid(Wu[a<t-1>, x<t>] + bu)
- gamma-f (forget) = sigmoid(Wf[a<t-1>, x<t>] + bf)
- gamma-o (output) = sigmoid(Wo[a<t-1>, x<t>] + bo)
- C<t> = gamma-u * C~<t> + gamma-f * c<t-1>
- a<t> = gamma-o * tanh(c<t>)
- sometime c<t-1> is added to all gamma values, call peepholse connection
- LSTM more flexible and complex -> computational power need
- GRU has only 2 params, so run faster

