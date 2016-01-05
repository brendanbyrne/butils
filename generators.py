'''
reverse_enum

produces value like that of enumerate (i.e. for "abc" (0, "a") -> (1, "b") -> (2,"c") )
but in reverse order. (i.e. (2, "c") -> (1, "b") -> (0, "a") )
'''
def reverse_enum (seq):
    indices = range(len(seq)-1,-1,-1)
    values = reversed(seq)
    for i,v in zip(indices, values):
        yield i,v

'''
window

Sliding window implementation from itertools example recipes.
Given an iterable, produce a sliding window of desired size. Don't yield if
window size is greater than length of sequence.
'''
from itertools import islice
def window (seq, size):
    it = iter(seq)
    result = tuple(islice(it, size))
    if len(result) == size:
        yield result
    for elem in it:
        result = result = result[1:] + (elem,)
        yield result

