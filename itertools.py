from itertools import (
    count,
    cycle,
    repeat,
    product,
    permutations,
    combinations,
    chain,
    compress,
    groupby,
    zip_longest
)


'''count(start, step)
count may take two values- start and step.
It then returns a sequence of values from start,
with intervals the size of step.
'''
for even in count(0, 2):
    if even > 20:
        break
    print(even)


'''cycle(iterable) makes an iterator from elements from an iterable,
and save a copy of each. Once exhausted,
it returns elements from that copy.
This repeats indefinitely.
'''
max = 0
for value in cycle([1 , 2]):
    if max < 10:
        max += 1
        print(value)
    else:
        break


'''repeat(element, times)
This will repeat element elem n-times or endlessly into the iterator.
'''
for e in repeat('luiz', 4):
    print(e)


'''product(*iterables, repeat)
returns the cartesian product of the input iterables.
This is equivalent to a nested for-loop.
'''
for i in product([1,2,3],[4,5,6]):
    print(i)


'''permutations(iterable, r)
returns r-length permutations of elements in the iterable.
It generates all possible permutations in lexicographic order,
and there is no repetition of elements.
'''
for i in permutations('123'):
    print(i)


'''combinations(iterabe, r)
This returns subsequences of length r from the elements of the iterable.
'''
for i in combinations('ABC', 2):
    print(i)


'''chain(iterable)
makes an iterator from elements of the first iterable,
then from the second, and so on.
It moves to the next iterable as one iterable exhausts.
'''
for i in chain('Luiz','Filipy','Brasil'):
    print(i)


'''compress(data, selectors)
This makes an iterator that filters elements,
from data, for which selector values amount to True.
'''
for i in compress('ABCDEF',[1,0,1,True,0,' ']):
    print(i)


'''groupby(iterable, key)
This makes an iterator that takes the iterable,
and returns consecutive keys and groups.
These are sub-iterators grouped by the key.
'''
for i,j in groupby('AAAAABBCCCCCDDDCCCBBA'):
    print(list(j))


'''zip_longest(*iterables, fillvalue)
This makes an iterator by aggregating elements from each iterable.
The fillvalue parameter tells it a value to fill for the remaining
places in the shorter iterable.
'''
for i in zip_longest('ABC','12345', 'luiz', fillvalue='*'):
    print(i)
