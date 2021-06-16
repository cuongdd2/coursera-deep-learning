## Transfer learning
- Apply knowledge from 1 task to use in another task
- Retrain W, b of the last layer
- If you have a lot of data, you can re-train whole network
- From image recognition -> radiology diagnosis: we can fine-tuning to new problem
- Transfer learning when:
    - Transfer from A -> B: A and B has same input X
    - Task A has more data than task B
    - Low level features from A helpful for learning B
