## Error analysis
- Get 100-500 mis-labeled dev set examples
- Count up how many error related to specific use case (dog instead of cat)
- if 10% error, 5/100 examples are dogs, -> 10% down to 9.5% error
- if 50/100 examples are dogs -> 10% down to 5%

### Evaluate multiple ideas in parallel
- Multiple ideas (dogs, bigcats, blurry images)
- Create table of idea -> # error examples
- Count up % of each idea

## Cleaning up incorrectly labeled data
- if incorrectly labeled in training set are random errors -> ok to not fix
- in dev/test sets, we need to fix them
- examine both right examples and wrong examples to make sure right is right and wrong is wrong
- manual analysis error is worth it