# wordling

Simplistic ranking of guesses for wordle words based on letter + letter-position scoring.

## Allowed words trained on answers

Which of the allowed guess words score highest by sum(letter-position-score * 2 + letter-score) for each letter, for scores based on answer list?

```
(1, 'soare', 3795.0)
(2, 'saine', 3605.5)
(3, 'slane', 3567.5)
(4, 'roate', 3551.0)
(5, 'saice', 3526.5)
(6, 'salet', 3517.5)
(7, 'raile', 3511.5)
(8, 'orate', 3475.0)
(9, 'raine', 3459.5)
(10, 'slier', 3458.5)
```

## Answers trained on answers

Which of the answer words score highest by sum(letter-position-score * 2 + letter-score) for each letter, for scores based on answer list?


```
(1, 'slate', 3601.5)
(2, 'stare', 3580.5)
(3, 'saner', 3516.5)
(4, 'arose', 3514.0)
(5, 'snare', 3513.5)
(6, 'stale', 3500.5)
(7, 'raise', 3495.5)
(8, 'arise', 3494.5)
(9, 'crate', 3493.5)
(10, 'share', 3477.5)
```

