
### Gated Recurrent Unit (GRU)
- Help with long range connection
- Published Cho 2014, Chung 2014
- using memory cell: c<t> = a<t>
- C~<t> = tanh(Wc[c<t-1>, x<t>] + bc)
- gamma-u "updated" = sigmoid(Wu[c<t-1>, x<t>] + bu)
- c<t> = gamma-u * c~<t> + (1 - gamma-u)*c<t-1>
- new version C~<t> = tanh(Wc[gamma-r * c<t-1>, x<t>] + bc)
- gamma-r = sigmoid(wr[c<t-1>, x<t>]+br)