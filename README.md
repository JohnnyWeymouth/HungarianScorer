# Hungarian Scorer
Often, it is important to find the optimal solution when pairing up items from two different lists. Here are some examples of situations where that is necessary:
- Assigning gymnasts to each event to maximize the team's overall score
- Choosing which worker(s) to hire based on your current team's skillset
- Identifying which words in two different names have the highest coorelation
- Allocating limited resources to the proper areas

## Making it simple
The Hungarian algorithm makes this all possible in O(n<sup>3</sup>) time. However, it can be difficult to create the matrix necessary to execute this algorithm, especially when the two lists are not equivilant in length. This package is meant to make finding optimal combinations using the hungarian algorithm dead simple. No matrices, no mess- just pass in the two lists and the function to score pairs, and you're done.

## 'But I already have the scores!'
If you already have scores, no worries! Just format your scores like so (making sure you don't miss an entry) and you can pass in a lambda to access the scores, as well as the scores themselves, as demonstrated below.
```python
from HungarianScorer.HungarianScorer import HungarianScorer

players = ['wilhelm', 'dave', 'stewart', 'jordan']
events = ['pommel horse', 'floor', 'parallel bars']
scores = {
    ('wilhelm', 'pommel horse'): 90,
    ('wilhelm', 'floor'): 50,
    ('wilhelm', 'parallel bars'): 50,

    ('dave', 'pommel horse'): 70,
    ('dave', 'floor'): 82,
    ('dave', 'parallel bars'): 75,

    ('stewart', 'pommel horse'): 70,
    ('stewart', 'floor'): 79,
    ('stewart', 'parallel bars'): 70,

    ('jordan', 'pommel horse'): 85,
    ('jordan', 'floor'): 68,
    ('jordan', 'parallel bars'): 70,
}

accessScore = lambda player,event,scores: scores[(player, event)]
result = HungarianScorer.getBestCombo(players, events, accessScore, scores)
# [('wilhelm', 'pommel horse', 90.0), ('dave', 'parallel bars', 75.0), ('stewart', 'floor', 79.0)]
```
Note: Jordan is still an amazing athlete. It is advised to take into account risk and standard deviation into your scores, as Jordan may in fact be the better choice for his consistency.

## Passing in functions that take only two arguments
Such simple functions are the easiest to implement. All you need provide are the lists and the function.
```python
from HungarianScorer.HungarianScorer import HungarianScorer
from fuzzywuzzy import fuzz # fuzz.ratio is a simple function that rates how close two strings are from 0-100

listA = ['j', 'john', 'weymouth']
listB = ['steve', 'jon', 'jamison', 'waymouth']

bestCombo = HungarianScorer.getBestCombo(listA, listB, fuzz.ratio)
# [('j', 'jamison', 25.0), ('john', 'jon', 86.0), ('weymouth', 'waymouth', 88.0)]
```


## Using more complex functions
Sometimes you will need to pass in more complex functions, that take more than just the two list item variables. All you have to do is make sure your function has itemA as its first argument, itemB as its second argument, and any other objects you need to use can be appended on at the end, as seen below.
```python
from HungarianScorer.HungarianScorer import HungarianScorer

listA = ['j', 'john', 'weymouth']
listB = ['steve', 'jon', 'jamison', 'waymouth']
def exampleScoringFunc(itemA:str, itemB:str, wildCardLetter) -> float:
    score = 100 - abs(len(itemA) - len(itemB))
    score += itemA.count(wildCardLetter)
    return score

bestCombo = HungarianScorer.getBestCombo(listA, listB, exampleScoringFunc, 'j')
# [('j', 'jon', 99.0), ('john', 'steve', 100.0), ('weymouth', 'waymouth', 100.0)]
```

## Indices
Sometimes it is meaningful to know the indices of the items in each pair. This is especially useful when some of the objects in one of the lists are identical. Here is the code to do that:
```python
from HungarianScorer.HungarianScorer import HungarianScorer
from fuzzywuzzy import fuzz

listA = ['john', 'john', 'weymouth']
listB = ['steve', 'jon', 'jamison', 'waymouth']

bestCombo = HungarianScorer.getBestCombo(listA, listB, fuzz.ratio)
# [('john', 'jon', 86.0), ('john', 'jamison', 55.0), ('weymouth', 'waymouth', 88.0)]

bestComboIndices = HungarianScorer.getBestComboAsIndices(listA, listB, fuzz.ratio)
# [(0, 1, 86.0), (1, 2, 55.0), (2, 3, 88.0)]
```

## Note
Remember that the two lists do not have to be items of the same type. For example, listA could be made of strings, while listB could be made of custom objects. All you need is a function that can return a float when comparing the two different objects.

Enjoy!