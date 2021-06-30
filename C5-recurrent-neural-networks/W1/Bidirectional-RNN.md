### Bidirectional RNN
- Acyclic graph, not a tree anymore
- we have both -> forward activations and <- backward activations
```
        y<1>            y<2>            y<3>                y<4>
        ->      <-      
        a<1>    a<1>    a<2>    a<2>    a<3>    a<3>        a<1>    a<1>
        x<1>
```
- disadvantages: need to run through the whole input before can return
- with something like speech recognition, live translation we cannot afford that

### Deep RNN
- Annotation a[l]<t> : l layer, t: index of input
- For RNN, 3 layers in the middle is deep enough